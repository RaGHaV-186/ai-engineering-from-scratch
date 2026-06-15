import torch
import torch.nn as nn
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("runs/experiment_1")

model = nn.Linear(4, 2)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
criterion = nn.MSELoss()

for step in range(100):
    x = torch.randn(16, 4)
    y = torch.randn(16, 2)

    output = model(x)
    loss = criterion(output, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    writer.add_scalar("loss/train", loss.item(), step)

    if step % 10 == 0:
        for name, param in model.named_parameters():
            writer.add_histogram(f"weights/{name}", param, step)

writer.close()
print("Done. Run: tensorboard --logdir=runs")