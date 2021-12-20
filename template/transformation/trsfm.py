import albumentations as A
from albumentations.pytorch import ToTensorV2


def trsfm(training):
    if training:
        return A.Compose(
            [

                A.HorizontalFlip(),
                A.RandomRotate90(),
                A.Cutout(num_holes=8, max_h_size=8, max_w_size=8, fill_value=0, always_apply=False),
                                A.SmallestMaxSize(max_size=160),
                A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=15, p=0.5),
                A.RandomCrop(height=128, width=128),
                A.RGBShift(r_shift_limit=15, g_shift_limit=15, b_shift_limit=15, p=0.5),
                A.RandomBrightnessContrast(p=0.5),
                A.Normalize(mean=(0.4802, 0.4481, 0.3975), std=(0.2302, 0.2265, 0.2262)),
                ToTensorV2(),
            ]
        )
    else:
        return A.Compose(
            [A.Normalize(mean=(0.4802, 0.4481, 0.3975), std=(0.2302, 0.2265, 0.2262)),
             ToTensorV2(),
             ]
        )

