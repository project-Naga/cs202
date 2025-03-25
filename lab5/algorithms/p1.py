import json
import matplotlib.pyplot as plt

# Load coverage data
def load_coverage(file):
    with open(file, "r") as f:
        return json.load(f).get("files", {})

old_coverage = load_coverage("coverage.json")
new_coverage = load_coverage("new_report/coverage.json")

# Identify common files
common_files = sorted(set(old_coverage.keys()) & set(new_coverage.keys()))  # Sorting for consistent ordering

old_coverage_vals = []
new_coverage_vals = []

missing_in_old = []
missing_in_new = []

for file in common_files:
    try:
        old_coverage_vals.append(old_coverage[file]["summary"]["percent_covered"])
        new_coverage_vals.append(new_coverage[file]["summary"]["percent_covered"])
    except KeyError:
        print(f"Skipping {file} due to missing data.")
    
# Check for mismatches
for file in new_coverage.keys():
    if file not in old_coverage:
        missing_in_old.append(file)

for file in old_coverage.keys():
    if file not in new_coverage:
        missing_in_new.append(file)

print(f"Total old coverage files: {len(old_coverage)}")
print(f"Total new coverage files: {len(new_coverage)}")
print(f"Common files: {len(common_files)}")
print(f"Files missing in old coverage: {len(missing_in_old)}")
print(f"Files missing in new coverage: {len(missing_in_new)}")

# Plot the comparison
plt.figure(figsize=(12, 6))
plt.plot(old_coverage_vals, label="Old Coverage", marker='o', linestyle='dashed', alpha=0.7)
plt.plot(new_coverage_vals, label="New Coverage", marker='s', linestyle='solid', alpha=0.7)

plt.ylabel("Coverage Percentage")
plt.title("Comparison of File Coverage")
plt.legend()
plt.tight_layout()
plt.savefig("coverage_report.png")
