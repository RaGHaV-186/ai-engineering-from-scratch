import time
import torch

class Timer:
    def __init__(self, name=""):
        self.name = name

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        elapsed = time.perf_counter() - self.start
        print(f"[{self.name}] {elapsed:.4f}s")

# simulating different parts of a training loop
with Timer("data loading"):
    time.sleep(0.1)  # pretend we're loading data
    data = torch.randn(64, 128)

with Timer("forward pass"):
    time.sleep(0.02)  # pretend model forward
    output = torch.randn(64, 10)

with Timer("backward pass"):
    time.sleep(0.03)  # pretend backprop