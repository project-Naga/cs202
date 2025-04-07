import json
from collections import defaultdict

def calculate_fan_in_out(data):
    fan_in = defaultdict(int)
    fan_out = {}

    for module, info in data.items():
        # Fan-out: Count of unique imports (excluding self)
        imports = set(info.get("imports", [])) - {module}
        fan_out[module] = len(imports)

        # Fan-in: For each import, increment that module's fan-in count
        for imported_module in imports:
            fan_in[imported_module] += 1

    # Fill in fan-in = 0 for modules with no incoming edges
    all_modules = set(data.keys())
    for mod in all_modules:
        fan_in.setdefault(mod, 0)

    # Combine fan-in and fan-out in one dictionary
    results = {}
    for mod in all_modules:
        results[mod] = {
            "fan_in": fan_in[mod],
            "fan_out": fan_out.get(mod, 0)
        }

    return results

# === Main execution ===
if __name__ == "__main__":
    # Load the module dependency JSON
    with open("dependencies.json") as f:
        json_data = json.load(f)

    fan_stats = calculate_fan_in_out(json_data)

    # Save results to a new JSON file
    with open("fan_in_out_results.json", "w") as out_file:
        json.dump(fan_stats, out_file, indent=4)

    print("✅ Fan-in and fan-out results saved to fan_in_out_results.json")
