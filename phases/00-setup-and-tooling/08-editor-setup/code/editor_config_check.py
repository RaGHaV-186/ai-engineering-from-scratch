# Phase 00 Lesson 08 — Editor Setup
import sys
import subprocess
from pathlib import Path


def check(label, fn):
    try:
        result = fn()
        print(f"  ✅  {label}: {result}")
    except Exception as e:
        print(f"  ❌  {label}: {e}")


print("\n=== Phase 00 · Lesson 08: Editor Config Check ===\n")

check("Python version",     lambda: sys.version.split()[0])
check("Virtual env active", lambda: Path(sys.prefix).name if sys.prefix != sys.base_prefix else (_ for _ in ()).throw(RuntimeError("not in a venv")))
check("PyTorch importable", lambda: __import__("torch").__version__)
check("MPS available",      lambda: str(__import__("torch").backends.mps.is_available()))
check("dotenv importable",  lambda: __import__("dotenv").__version__)
check("Working directory",  lambda: Path.cwd().name)

print("\n=== Done ===\n")
