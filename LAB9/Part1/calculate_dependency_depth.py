import json

def compute_dependency_depth(modules):
    # Build dependency graph (excluding self-imports)
    graph = {mod: set(info.get("imports", [])) - {mod} for mod, info in modules.items()}

    depth_cache = {}

    def dfs(module, visited):
        if module in depth_cache:
            return depth_cache[module]
        if module in visited:
            return 0  # Prevent cycles

        visited.add(module)
        max_depth = 0
        for dep in graph.get(module, []):
            if dep in graph:  # Skip external/unknown modules
                max_depth = max(max_depth, dfs(dep, visited.copy()))
        depth_cache[module] = 1 + max_depth
        return depth_cache[module]

    return {mod: dfs(mod, set()) for mod in graph}

# === Main execution ===
if __name__ == "__main__":
    with open("dependencies.json") as f:
        modules_data = json.load(f)

    depths = compute_dependency_depth(modules_data)

    # Save to a new JSON file
    with open("dependency_depth.json", "w") as out_file:
        json.dump(depths, out_file, indent=4)

    print("✅ Dependency depth saved to dependency_depth.json")
