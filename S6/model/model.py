import torch.nn as nn
import torch.nn.functional as F
from base import BaseModel
from normalization import norm


class MnistModel(BaseModel):
    def __init__(self, num_classes=10, normalizationtype='Layer', dropout=.01):
        super().__init__()
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=1, out_channels=8, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=8, group=2, hight=26, width=26),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 26  receptive field  : 3

        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=8, group=2, hight=24, width=24),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 24 receptive field  : 5

        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=8, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=8, group=2, hight=22, width=22),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 22 receptive field  : 7

        self.pool1 = nn.MaxPool2d(2, 2)  # output_size = 11 receptive field  : 8

        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=12, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=12, group=2, hight=9, width=9),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 9 receptive field  : 12

        self.convblock5 = nn.Sequential(
            nn.Conv2d(in_channels=12, out_channels=14, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=14, group=2, hight=7, width=7),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 7 receptive field  : 16

        self.convblock6 = nn.Sequential(
            nn.Conv2d(in_channels=14, out_channels=8, kernel_size=(1, 1), padding=0, bias=False),
            norm(type=normalizationtype, channels=8, group=2, hight=7, width=7),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 7 receptive field  : 16
        self.convblock7 = nn.Sequential(
            nn.Conv2d(in_channels=8, out_channels=26, kernel_size=(3, 3), padding=0, bias=False),
            norm(type=normalizationtype, channels=26, group=2, hight=5, width=5),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 5 receptive field  : 20

        self.convblock8 = nn.Sequential(
            nn.Conv2d(in_channels=26, out_channels=50, kernel_size=(1, 1), padding=0, bias=False),
            norm(type=normalizationtype, channels=50, group=2, hight=5, width=5),
            nn.Dropout(dropout),
            nn.ReLU()
        )  # output_size = 5 receptive field  : 20

        # OUTPUT BLOCK
        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=5)
        )  # output_size = 1 receptive field  : 28

        self.convblock9 = nn.Sequential(
            nn.Conv2d(in_channels=50, out_channels=num_classes, kernel_size=(1, 1), padding=0, bias=False),

        )  # output_size = 1 receptive field  : 28

    def forward(self, x):
        x = self.convblock1(x)
        x = self.convblock2(x)
        x = self.convblock3(x)
        x = self.pool1(x)
        x = self.convblock4(x)
        x = self.convblock5(x)
        x = self.convblock6(x)
        x = self.convblock7(x)
        x = self.convblock8(x)
        x = self.gap(x)
        x = self.convblock9(x)
        x = x.view(-1, 10)
        return F.log_softmax(x, dim=-1)
