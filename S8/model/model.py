import torch.nn.functional as F
from base import BaseModel

from torchvision import models
import torch.nn as nn


class CIFRModel(BaseModel):

    def __init__(self):
        super(CIFRModel, self).__init__()

        self.model = models.resnet34(pretrained=True)
        self.model.fc = nn.Linear(512, 10)

    def forward(self, x):
        x = self.model(x)
        return F.log_softmax(x, dim=-1)
