import os
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

COVERAGE_JSON_FILE = "coverage.json"
OUTPUT_DIR = "new_tests"
TIMEOUT = 200  # Set a timeout of 60 seconds per module


def get_low_coverage_modules():
    """Reads coverage.json and returns a list of modules with <3% coverage."""
    with open(COVERAGE_JSON_FILE, "r") as f:
        coverage_data = json.load(f)

    low_coverage_modules = []
    for file, details in coverage_data.get("files", {}).items():
        percent_covered = details["summary"]["percent_covered"]
        if percent_covered < 10:  # Change threshold to 3%
            relative_path = os.path.relpath(file, start=".")
            module_name = relative_path.replace(os.sep, ".").rstrip(".py")
            low_coverage_modules.append(module_name)

    return low_coverage_modules


def generate_tests(module_name):
    """Runs Pynguin to generate tests for a specific module."""
    print(f"🔹 Generating tests for {module_name}...")
    try:
        subprocess.run(
            [
                "pynguin",
                "--project-path", ".",
                "--module-name", module_name,
                "--output-path", OUTPUT_DIR,
                "--maximum-search-time", str(TIMEOUT),
            ],
            check=True,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        print(f"⏳ Timeout! Skipping {module_name} (took longer than {TIMEOUT} sec).")
    except subprocess.CalledProcessError:
        print(f"⚠ Error in generating tests for {module_name}. Skipping.")


if __name__ == "__main__":
    os.environ["PYNGUIN_DANGER_AWARE"] = "True"
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    modules = get_low_coverage_modules()

    if modules:
        print(f"📌 Found {len(modules)} modules with <3% coverage. Generating tests...")
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(generate_tests, module): module for module in modules}
            for future in as_completed(futures):
                future.result()
    else:
        print("✅ No low-coverage modules found. No tests need to be generated.")
