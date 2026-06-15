import torch
import torch.nn as nn

def check_devices(model, *tensors):
    model_device = next(model.parameters()).device
    print(f"Model device: {model_device}")
    for i, t in enumerate(tensors):
        if t.device != model_device:
            print(f"  WARNING: tensor {i} is on {t.device}, but model is on {model_device}")
        else:
            print(f"  tensor {i}: OK ({t.device})")

model = nn.Linear(4, 2)  # on CPU by default

tensor_ok = torch.randn(4)           # also CPU - fine
tensor_bad = torch.randn(4)          # also CPU but pretend it's wrong
# we can't actually put it on GPU without one, so let's just simulate:
print("--- Simulating device check ---")
check_devices(model, tensor_ok, tensor_bad)