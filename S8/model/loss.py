import torch.nn as nn


def crossentropyloss(output, target):
    criterion = nn.CrossEntropyLoss()
    return criterion(output, target)
