import torch.nn as nn

batch = 'Batch'
layer = 'Layer'
group = 'Group'

def norm(type, channels, group, hight, width):
    if type.upper().__eq__(batch.upper()):
        return nn.BatchNorm2d(channels)
    elif type.upper().__eq__(layer.upper()):
        return nn.LayerNorm(width)
    else:
        return nn.GroupNorm(group, channels)
