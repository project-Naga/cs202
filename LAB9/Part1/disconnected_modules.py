import json

def find_disconnected_modules(data):
    disconnected = []

    for module, info in data.items():
        imports = set(info.get("imports", [])) - {module}
        imported_by = set(info.get("imported_by", [])) - {module}

        if not imports and not imported_by:
            disconnected.append(module)

    return disconnected

# === Main execution ===
if __name__ == "__main__":
    with open("dependencies.json") as f:
        json_data = json.load(f)

    disconnected_modules = find_disconnected_modules(json_data)

    if disconnected_modules:
        print("🔌 Disconnected modules found:")
        for mod in disconnected_modules:
            print(f" - {mod}")
    else:
        print("✅ No disconnected modules found.")
