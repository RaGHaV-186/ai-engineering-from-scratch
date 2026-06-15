import torch

def debug_print(name, tensor):
    print(f"{name}: shape={tensor.shape}, dtype={tensor.dtype}, "
          f"device={tensor.device}, "
          f"min={tensor.min().item():.4f}, max={tensor.max().item():.4f}, "
          f"has_nan={tensor.isnan().any().item()}")

# normal tensor
x = torch.randn(3, 4)
debug_print("x", x)

# tensor with a NaN injected
y = torch.randn(3, 4)
y[1, 2] = float('nan')
debug_print("y", y)