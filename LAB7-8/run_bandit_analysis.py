import re
import os
import pandas as pd
from collections import defaultdict

# Directory containing Bandit reports
report_directory = "bandit_reports"

# Regular expressions to extract relevant details
commit_pattern = re.compile(r"Run started:(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")
severity_pattern = re.compile(r"Severity:\s*(\w+)")
confidence_pattern = re.compile(r"Confidence:\s*(\w+)")
cwe_pattern = re.compile(r"CWE:\s*(CWE-\d+)")

# Data storage
commit_issues = defaultdict(lambda: {
    "HIGH_Conf": 0, "MEDIUM_Conf": 0, "LOW_Conf": 0,
    "HIGH_Sev": 0, "MEDIUM_Sev": 0, "LOW_Sev": 0,
    "CWEs": set(), "File": ""
})

# Process each report file in the directory
for filename in os.listdir(report_directory):
    file_path = os.path.join(report_directory, filename)

    if os.path.isfile(file_path):  # Ensure it's a file
        with open(file_path, "r", encoding="utf-8") as file:
            current_commit = None

            for line in file:
                # Detect commit run start time (acts as a unique commit identifier)
                commit_match = commit_pattern.search(line)
                if commit_match:
                    current_commit = f"{commit_match.group(1)}_{filename}"  # Unique commit ID
                    commit_issues[current_commit]["File"] = filename  # Store file name
                    continue

                # Extract issue details
                if current_commit:
                    severity_match = severity_pattern.search(line)
                    confidence_match = confidence_pattern.search(line)
                    cwe_match = cwe_pattern.search(line)

                    if severity_match:
                        severity = severity_match.group(1).upper()
                        commit_issues[current_commit][f"{severity}_Sev"] += 1

                    if confidence_match:
                        confidence = confidence_match.group(1).upper()
                        commit_issues[current_commit][f"{confidence}_Conf"] += 1

                    if cwe_match:
                        commit_issues[current_commit]["CWEs"].add(cwe_match.group(1))

# Convert to DataFrame
df = pd.DataFrame.from_dict(commit_issues, orient="index")

# Convert CWE sets to semicolon-separated strings
df["CWEs"] = df["CWEs"].apply(lambda x: ";".join(sorted(x)))  # Sort for consistency

# Save to CSV
output_file = "bandit_analysis.csv"
df.to_csv(output_file, index_label="Commit")

# Print summary
print(f"Analysis complete! Results saved to {output_file}")
print(df.head())  # Display first few rows
