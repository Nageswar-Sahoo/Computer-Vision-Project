import torch.nn as nn
import torch.nn.functional as F
from base import BaseModel

from torchvision import models
import torch.nn as nn


class CIFRModel(BaseModel):

    def __init__(self):

        super().__init__()
        self.model_ft = models.resnet34(pretrained=True)
        num_ftrs = self.model_ft.fc.in_features
    # Here the size of each output sample is set to 2.
    # Alternatively, it can be generalized to nn.Linear(num_ftrs, len(class_names)).
        self.model_ft.fc = nn.Linear(num_ftrs, 10)

    def forward(self, x):
        x = self.model_ft(x)
        return F.log_softmax(x, dim=-1)
