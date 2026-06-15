import torch

def detect_nan(model, loss, step):
    if torch.isnan(loss):
        print(f"NaN loss at step {step}")
        for name, param in model.named_parameters():
            if param.grad is not None:
                if torch.isnan(param.grad).any():
                    print(f"  NaN gradient in {name}")
        return True
    return False

# simple model
model = torch.nn.Linear(4, 2)
loss_normal = torch.tensor(0.5)
loss_nan = torch.tensor(float('nan'))

# simulate gradients
model.weight.grad = torch.randn(2, 4)
model.bias.grad = torch.tensor([float('nan'), 0.5])

detect_nan(model, loss_normal, step=1)
detect_nan(model, loss_nan, step=2)