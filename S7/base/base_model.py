import torch.nn as nn
import numpy as np
from abc import abstractmethod
from torchsummary import summary

class BaseModel(nn.Module):
    """
    Base class for all models
    """
    @abstractmethod
    def forward(self, *inputs):
        """
        Forward pass logic

        :return: Model output
        """
        raise NotImplementedError

    def __str__(self):
        """
        Model prints with number of trainable parameters
        """
        summary(self, input_size=(1, 28, 28))

