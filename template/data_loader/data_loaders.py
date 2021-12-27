from transformation import trsfm

import torch
from transformation.Albumentations import Albumentations


# def get_train_data_loader(batch_size=512):
#     trainset = Albumentations(root='./data', train=True, download=True, transform=trsfm(True))
#     return torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)
#
#
# def get_test_data_loader(batch_size=512):
#     testset = Albumentations(root='./data', train=False, download=True, transform=trsfm(False))
#     return torch.utils.data.DataLoader(testset, batch_size=512, shuffle=False, num_workers=2)


def get_train_data_loader(data, targets, batch_size=512):
    trainset = Albumentations(data, targets, transform=trsfm(True))
    return torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=True, num_workers=2)


def get_test_data_loader(data, targets, batch_size=512):
    testset = Albumentations(data, targets, transform=trsfm(False))
    return torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=2)
