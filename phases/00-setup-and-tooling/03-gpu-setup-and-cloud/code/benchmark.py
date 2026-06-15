"""
Phase 00 · Lesson 03 — GPU Setup & Cloud
CPU vs MPS timing benchmark.
"""

import torch
import time


def benchmark_matmul(device: torch.device, size: int = 4096, repeats: int = 10) -> float:
    """Warm up then time matrix multiplication."""
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)

    # Warm-up: first MPS call is slower due to Metal shader compilation
    for _ in range(3):
        _ = a @ b

    # Sync before starting the clock
    if device.type == "mps":
        torch.mps.synchronize()

    start = time.perf_counter()
    for _ in range(repeats):
        c = a @ b

    # Must sync BEFORE reading the clock — GPU runs async
    # Without this you measure dispatch time, not compute time
    if device.type == "mps":
        torch.mps.synchronize()
    elif device.type == "cuda":
        torch.cuda.synchronize()

    elapsed = time.perf_counter() - start
    return elapsed / repeats


if __name__ == "__main__":
    size = 4096
    repeats = 10
    print(f"Benchmarking {size}x{size} matrix multiply ({repeats} iterations)\n")

    cpu_time = benchmark_matmul(torch.device("cpu"), size, repeats)
    print(f"CPU : {cpu_time * 1000:.1f} ms/iter")

    if torch.backends.mps.is_available():
        mps_time = benchmark_matmul(torch.device("mps"), size, repeats)
        print(f"MPS : {mps_time * 1000:.1f} ms/iter")
        print(f"\n🚀 MPS speedup: {cpu_time / mps_time:.1f}x faster than CPU")
    else:
        print("MPS not available")
