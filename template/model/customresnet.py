


import torch.nn as nn

# Residual block
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.conv2 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(out_channels)
        self.relu = nn.ReLU()
        self.droput = nn.Dropout(0.05)

    def forward(self, x):
        residual = x
        out = self.conv1(x.clone())
        out = self.bn1(out)
        out = self.droput(out)
        out = self.relu(out)
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.droput(out)
        out = self.relu(out)
        out = residual + out
        out = self.relu(out)
        return out


# ResNet
class ResNet(nn.Module):
    def __init__(self, block, num_classes=10):
        super(ResNet, self).__init__()
        self.preplayer = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.Dropout(0.05),
            nn.ReLU()
        )
        self.conv_X1 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(3, 3), stride=1, padding=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(128),
            nn.Dropout(0.05),
            nn.ReLU()
        )
        self.layer1 = block(128, 128, 1)
        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(3, 3), stride=1, padding=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(256),
            nn.Dropout(0.05),
            nn.ReLU()
        )
        self.conv_X2 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=(3, 3), stride=1, padding=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(512),
            nn.Dropout(0.05),
            nn.ReLU()
        )
        self.layer3 = block(512, 512, 1)
        self.avg_pool = nn.AvgPool2d(4)
        self.fc = nn.Linear(512, num_classes)

    def forward(self, x):
        out = self.preplayer(x)
        out = self.conv_X1(out)
        out = self.layer1(out)
        out = self.layer2(out)
        out = self.conv_X2(out)
        out = self.layer3(out)
        out = self.avg_pool(out)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        return out


def CustomResnet():
    return ResNet(ResidualBlock)

