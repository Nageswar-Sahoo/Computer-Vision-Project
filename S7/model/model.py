import torch.nn as nn
import torch.nn.functional as F
from base import BaseModel


class CIFRModel(BaseModel):

    def __init__(self):
        super().__init__()

        self.depthwise_separable_conv1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, groups=3, padding=1, bias=False),
            nn.BatchNorm2d(3),
            nn.ReLU(),
            nn.Conv2d(in_channels=3, out_channels=256, kernel_size=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),
        )

        self.depthwise_separable_conv2 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, groups=256, padding=1, dilation=1, bias=False),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(in_channels=256, out_channels=40, kernel_size=1, bias=False),
            nn.BatchNorm2d(40),
            nn.ReLU(),
        )

        self.transposeconvblock = nn.Sequential(
            nn.ConvTranspose2d(in_channels=40, out_channels=185, kernel_size=(3, 3), padding=0, bias=False, dilation=8),
            nn.BatchNorm2d(185),
            nn.ReLU(),

        )

        self.convblock = nn.Sequential(
            nn.Conv2d(in_channels=185, out_channels=10, kernel_size=(3, 3), padding=0, bias=False, dilation=16),
            nn.BatchNorm2d(10),
            nn.ReLU()
        )

        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=16)
        )

    def forward(self, x):
        x = self.depthwise_separable_conv1(x)
        x = self.depthwise_separable_conv2(x)
        x = self.transposeconvblock(x)
        x = self.convblock(x)
        x = self.gap(x)
        x = x.reshape(-1, 10 * 1 * 1)
        return F.log_softmax(x, dim=-1)
