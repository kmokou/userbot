import os
from pathlib import Path
from importlib import import_module

def load_modules(client):
    modules_path = Path(__file__).parent.parent / "modules"
    for filename in os.listdir(modules_path):
        if filename.endswith(".py") and filename != "__init__.py":
            mod_name = filename[:-3]
            mod = import_module(f"modules.{mod_name}")
            if hasattr(mod, "register"):
                mod.register(client)
                print(f"[✓] Loaded module: {mod_name}")
