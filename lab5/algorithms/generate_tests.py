import os
import subprocess

# Step 1: Run coverage analysis
print("Running coverage analysis...")
subprocess.run("pytest --cov=algorithms --cov-branch --cov-report=term > coverage_report.txt", shell=True)

# Step 2: Extract files with incomplete coverage
uncovered_files = []
with open("coverage_report.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 4 and "%" in parts[3]:  # Check if it contains coverage percentage
            coverage = parts[3].replace("%", "")
            if coverage.isdigit() and int(coverage) < 100:  # If coverage < 100%
                uncovered_files.append(parts[0])  # File name

# Step 3: Convert file paths to module names
modules_to_test = []
for file in uncovered_files:
    if file.endswith(".py") and "site-packages" not in file:
        module_name = file.replace("/", ".").replace(".py", "")
        if module_name.startswith("algorithms."):  # Ensure it's part of the repo
            modules_to_test.append(module_name)

if not modules_to_test:
    print("All files are fully covered. No tests to generate.")
    exit()

print(f"Modules with incomplete coverage: {modules_to_test}")

# Step 4: Run Pynguin for uncovered modules
for module in modules_to_test:
    print(f"Generating tests for {module}...")
    cmd = f"pynguin --project-path=./ --output-path=generated_tests --module-name={module} --maximum-search-time 60 --maximum-sequence-length 10"
    subprocess.run(cmd, shell=True)

print("Test generation complete. Check 'generated_tests' folder.")
