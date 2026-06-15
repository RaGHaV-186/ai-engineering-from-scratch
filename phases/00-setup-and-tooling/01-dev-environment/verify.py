import sys
print(f"Python {sys.version}")

import numpy as np
print(f"NumPy {np.__version__}")
a = np.array([1, 2, 3])
print(f"Vector: {a}, dot product: {np.dot(a, a)}")

import torch
print(f"PyTorch {torch.__version__}")
print(f"MPS available: {torch.backends.mps.is_available()}")
if torch.backends.mps.is_available():
    x = torch.tensor([1.0, 2.0, 3.0]).to("mps")
    print(f"Tensor on GPU: {x}")

import matplotlib
print(f"Matplotlib {matplotlib.__version__}")

print("\nAll checks passed!")
