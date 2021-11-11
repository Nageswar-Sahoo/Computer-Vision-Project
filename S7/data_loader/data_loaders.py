from torchvision import datasets, transforms
from base import BaseDataLoader
from transformation import trsfm


class CIFRDataLoader(BaseDataLoader):
    """
    MNIST data loading demo using BaseDataLoader
    """
    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        transformation=trsfm(training)
        self.data_dir = data_dir
        self.dataset = datasets.CIFAR10(self.data_dir, train=training, download=True, transform=transformation)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)
