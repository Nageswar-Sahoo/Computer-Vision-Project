import albumentations as A
from albumentations.pytorch import ToTensorV2


def trsfm(training):
    if training:
        return A.Compose(
            [
                A.Resize(40, 40),
                A.RandomCrop(32, 32),
                A.HorizontalFlip(),
                A.Cutout(num_holes=8, max_h_size=8, max_w_size=8, fill_value=0, always_apply=False, p=0.5),
                A.Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.2023, 0.1994, 0.2010)),
                ToTensorV2(),
            ]
        )
    else:
        return A.Compose(
            [A.Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.2023, 0.1994, 0.2010)),
             ToTensorV2(),
             ]
        )
