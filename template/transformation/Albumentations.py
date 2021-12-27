from typing import Tuple, Any

from torch.utils.data import Dataset
import numpy as np

class Albumentations(Dataset):
    """__init__ and __len__ functions are the same as in TorchvisionDataset"""

    def __init__(self, data, targets, transform):
        self.data = data
        self.targets = targets
        self.transform = transform

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        img, target = self.data[index], self.targets[index]
        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = np.array(img)
        if self.transform is not None:
            augmented = self.transform(image=img)
            img=augmented['image']
            img = augmented['image']

        return img, target

    def __len__(self) -> int:
        return len(self.data)


