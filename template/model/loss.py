import torch.nn as nn


def crossentropyloss(output, target):
    print("crossentropyloss")
    print(output.shape)
    print(target.shape)
    print(output)
    print(target)
    criterion = nn.CrossEntropyLoss()
    return criterion(output, target)
