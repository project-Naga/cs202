import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

# Load the index.html coverage report
HTML_FILE = "index.html"

with open(HTML_FILE, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Extract coverage data from the table
files = []
line_coverage = []

table = soup.find("table")  # Find the first table in the report
rows = table.find_all("tr")[1:]  # Skip the header row

for row in rows:
    columns = row.find_all("td")
    if len(columns) > 1:
        filename = columns[0].text.strip()
        coverage_text = columns[3].text.strip().replace("%", "")  # Line coverage column

        if coverage_text.isdigit():
            files.append(filename.split("/")[-1])  # Use only filenames for readability
            line_coverage.append(float(coverage_text))

# Convert to NumPy arrays
x = np.arange(len(files))

# Plot line coverage as a bar chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x, line_coverage, color="blue", alpha=0.7, label="Line Coverage")

# Formatting
ax.set_xlabel("Files")
ax.set_ylabel("Coverage %")
ax.set_title("Code Coverage Analysis")
ax.set_xticks(x)
ax.set_xticklabels(files, rotation=45, ha="right")
ax.set_ylim(0, 100)  # Coverage is in percentage
ax.legend()

# Save the visualization
plt.tight_layout()
plt.savefig("coverage_report.png")
plt.show()
