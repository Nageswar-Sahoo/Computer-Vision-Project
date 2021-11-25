import albumentations as A
from albumentations.pytorch import ToTensorV2

def trsfm(training):
    if training:
        return A.Compose(
            [
                A.Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.2023, 0.1994, 0.2010)),
                ToTensorV2(),
            ]
        )
    else:
        return A.Compose(
            [
                A.Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.2023, 0.1994, 0.2010)),
                ToTensorV2(),
            ]
        )

