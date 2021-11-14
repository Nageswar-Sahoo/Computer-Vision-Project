import torch.nn as nn
import torch.nn.functional as F
from base import BaseModel


class CIFRModel(BaseModel):
    # epoch: 8
    # loss: 0.73457906589928
    # accuracy: 75.11097301136364
    # val_loss: 0.7309541015685359
    # val_accuracy: 74.72310126582279



    def __init__(self, num_classes=10, normalizationtype='Layer', dropout=.01):
        super().__init__()
        # Input Block

        self.depthwise_separable_conv1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=3, kernel_size=3, groups=3, padding=1, bias=False),
            nn.BatchNorm2d(3),
            #nn.Dropout(.05),
            nn.ReLU(),
            nn.Conv2d(in_channels=3, out_channels=256, kernel_size=1, bias=False),
            nn.BatchNorm2d(256),
            #nn.Dropout(.05),
            nn.ReLU(),
        )  # output_size = 28 receptive field  : 5

        # Input Block
        self.depthwise_separable_conv2 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, groups=256, padding=1,dilation=1, bias=False),
            nn.BatchNorm2d(256),
           #nn.Dropout(.05),
            nn.ReLU(),
            nn.Conv2d(in_channels=256, out_channels=50, kernel_size=1, bias=False),
            nn.BatchNorm2d(50),
            #nn.Dropout(.05),
            nn.ReLU(),
        )  # output_size = 28 receptive field  : 5
        # Input Block

        self.convblock3 = nn.Sequential(
            nn.ConvTranspose2d(in_channels=50, out_channels=128, kernel_size=(3, 3), padding=0, bias=False, dilation=8),
            nn.BatchNorm2d(128),
            #nn.Dropout(.05),
            nn.ReLU(),

        )  # output_size = 26 receptive field  : 7

        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=10, kernel_size=(3, 3), padding=0, bias=False, dilation=16),
            nn.BatchNorm2d(10),
            nn.ReLU()
        )  # output_size = 20 receptive field  : 12

        self.gap = nn.Sequential(
            nn.AvgPool2d(kernel_size=14)
        )  # output_size = 20 receptive field  : 28

    def forward(self, x):
        x = self.depthwise_separable_conv1(x)
        x = self.depthwise_separable_conv2(x)
        x = self.convblock3(x)
        x = self.convblock4(x)
        x = self.gap(x)
        x = x.reshape(-1, 10 * 1 * 1)
        return F.log_softmax(x, dim=-1)