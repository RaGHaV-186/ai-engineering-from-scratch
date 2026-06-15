import sys
import importlib.metadata


def get_env_info():
    print("=== Python Environment ===")
    print(f"Python version : {sys.version}")
    print(f"Executable     : {sys.executable}")
    print(f"Prefix         : {sys.prefix}")

    in_venv = sys.prefix != sys.base_prefix
    print(f"Inside venv    : {in_venv}")

    print("\n=== Installed Packages ===")
    packages = sorted(importlib.metadata.packages_distributions().keys())
    for pkg in packages[:20]:
        print(f"  {pkg}")
    print(f"  ... ({len(packages)} total)")


if __name__ == "__main__":
    get_env_info()