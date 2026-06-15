"""
Phase 00 · Lesson 03 — GPU Setup & Cloud
Device detection and selection for Apple Silicon (MPS) + cloud awareness.
"""

import torch
import platform
import sys


def get_best_device() -> torch.device:
    """
    Returns the best available compute device.
    Priority: CUDA > MPS > CPU
    On M4 MacBook Air, this will return 'mps'.
    """
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print(f"✅ CUDA available — GPU: {torch.cuda.get_device_name(0)}")
    elif torch.backends.mps.is_available():
        device = torch.device("mps")
        print(f"✅ MPS available — Apple Silicon GPU active")
    else:
        device = torch.device("cpu")
        print(f"⚠️  No GPU found — using CPU")
    return device


def print_system_info():
    print("=" * 50)
    print("SYSTEM REPORT")
    print("=" * 50)
    print(f"Platform     : {platform.platform()}")
    print(f"Python       : {sys.version.split()[0]}")
    print(f"PyTorch      : {torch.__version__}")
    print(f"CUDA built   : {torch.backends.cuda.is_built()}")
    print(f"MPS built    : {torch.backends.mps.is_built()}")
    print(f"MPS available: {torch.backends.mps.is_available()}")
    print("=" * 50)


def run_smoke_test(device: torch.device):
    """
    Creates two tensors on the device, multiplies them.
    Verifies the GPU is actually doing work.
    """
    print(f"\n🔥 Running smoke test on: {device}")
    a = torch.randn(1000, 1000, device=device)
    b = torch.randn(1000, 1000, device=device)
    c = a @ b  # matrix multiply — the core of all neural net ops
    print(f"   Input  device : {a.device}")
    print(f"   Output device : {c.device}")
    print(f"   Output shape  : {c.shape}")
    print(f"   Output dtype  : {c.dtype}")
    print("✅ Smoke test passed\n")
    return c


if __name__ == "__main__":
    print_system_info()
    device = get_best_device()
    run_smoke_test(device)
