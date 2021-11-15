from torchvision import datasets, transforms
from base import BaseDataLoader
from transformation import trsfm
import albumentations as A
from albumentations.pytorch import ToTensorV2

from transformation.Albumentations import Albumentations


class CIFRDataLoader(BaseDataLoader):
      def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.0, num_workers=1, training=True):
        transformation = trsfm(training)
        self.data_dir = data_dir
        self.dataset = Albumentations(self.data_dir, train=training, download=True, transform=transformation)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)
