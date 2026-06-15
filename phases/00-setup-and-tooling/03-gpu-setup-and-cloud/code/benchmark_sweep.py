"""
Phase 00 · Lesson 03 — GPU Setup & Cloud
Sweep across matrix sizes to find where MPS outpaces CPU.
This reveals the crossover point — the GPU only wins when work is large enough
to justify the dispatch overhead.
"""

import torch
import time


def time_matmul(device: torch.device, size: int, repeats: int = 5) -> float:
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)

    # Warm-up
    for _ in range(2):
        _ = a @ b

    if device.type == "mps":
        torch.mps.synchronize()

    start = time.perf_counter()
    for _ in range(repeats):
        _ = a @ b
    if device.type == "mps":
        torch.mps.synchronize()
    elif device.type == "cuda":
        torch.cuda.synchronize()

    return (time.perf_counter() - start) / repeats


if __name__ == "__main__":
    sizes = [512, 1024, 2048, 4096, 6144, 8192]
    cpu = torch.device("cpu")
    mps = torch.device("mps")

    print(f"{'Size':>6}  {'CPU (ms)':>10}  {'MPS (ms)':>10}  {'Speedup':>9}")
    print("-" * 44)

    for size in sizes:
        cpu_t = time_matmul(cpu, size) * 1000
        mps_t = time_matmul(mps, size) * 1000
        speedup = cpu_t / mps_t
        marker = " ◀ MPS wins" if speedup > 1.5 else ""
        print(f"{size:>6}  {cpu_t:>10.1f}  {mps_t:>10.1f}  {speedup:>8.1f}x{marker}")
