# MPS Device Cheatsheet (Apple Silicon)
## Phase 00 · Lesson 03 Output

### Device Selection (use this in every training script)
```python
def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

DEVICE = get_device()
model = MyModel().to(DEVICE)
x = x.to(DEVICE)
```

### Required env var (add to ~/.zshrc)
```bash
export PYTORCH_ENABLE_MPS_FALLBACK=1
```

### Always sync before timing
```python
torch.mps.synchronize()   # MPS
torch.cuda.synchronize()  # CUDA
# then read time.perf_counter()
```

### M4 MacBook Air benchmark results (4096x4096 float32)
| Device | ms/iter | Notes |
|--------|---------|-------|
| CPU    | ~74 ms  | Apple Accelerate (AMX) — fast for a CPU |
| MPS    | ~53 ms  | 1.4x speedup at this size |

Crossover point: MPS wins at ~2048x2048 and above.
Below that, dispatch overhead dominates.

### MPS limitations
- No multi-GPU / distributed (NCCL not supported)
- float16 / AMP: partial support — use float32 by default
- Some ops fall back to CPU (FALLBACK=1 prevents crashes)
- GPU can use ~75% of system RAM max

### Cloud escape valve
When local MPS isn't enough:
- Free:  Google Colab (T4), Kaggle Notebooks (P100, 30hr/week)
- Paid:  Lambda Labs (~$0.75/hr A10), Vast.ai, RunPod
