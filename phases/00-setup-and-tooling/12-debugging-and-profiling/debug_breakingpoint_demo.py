import torch


def training_step(step, loss_value):
    loss = torch.tensor(loss_value)

    if torch.isnan(loss) or loss.item() > 100:
        breakpoint()

    return loss


# normal steps
training_step(1, 0.9)
training_step(2, 0.7)

# this one triggers the breakpoint
training_step(3, float('nan'))