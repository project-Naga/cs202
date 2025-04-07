import json
import networkx as nx

# Load the dependency graph
with open("dependencies.json", "r") as f:
    dependencies = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for module, deps in dependencies.items():
    for dep in deps:
        G.add_edge(module, dep)

# Detect cycles
cycles = list(nx.simple_cycles(G))

# Print detected cycles
if cycles:
    print("Cyclic Dependencies Found:")
    for cycle in cycles:
        print(" -> ".join(cycle))
else:
    print("No cyclic dependencies detected.")
