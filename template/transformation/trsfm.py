import albumentations as A
from albumentations.pytorch import ToTensorV2


def trsfm(training):
    if training:
        return A.Compose(
            [

                A.HorizontalFlip(),
                A.RandomRotate90(),
                A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.5),
                A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.5),
                A.RandomBrightnessContrast(p=0.5),
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
