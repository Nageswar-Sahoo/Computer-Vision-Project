from typing import Tuple, Any

import cv2
import numpy as np


from PIL import Image
from torchvision.datasets import CIFAR10


class CIFR10Dataset(CIFAR10):
    """__init__ and __len__ functions are the same as in TorchvisionDataset"""

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        """
        Args:
            index (int): Index

        Returns:
            tuple: (image, target) where target is index of the target class.
        """
        img, target = self.data[index], self.targets[index]
        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = np.array(img)
        if self.transform is not None:
            augmented = self.transform(image=img)
            img=augmented['image']

        if self.target_transform is not None:
            target = self.target_transform(target)

        return img, target

    def __len__(self) -> int:
        return len(self.data)