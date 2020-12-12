import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()


def train_model(itera):
    for epoch in range(itera):
        y1 = model(x)
        loss = criterion(y1, y)
        writer.add_scalar("Loss/train", loss, epoch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


# 这里的8定义的是训练的epoch数字
train_model(8)
writer.flush()
