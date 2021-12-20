import albumentations as A
from albumentations.pytorch import ToTensorV2


def trsfm(training):
    if training:
        return A.Compose(
            [

                A.HorizontalFlip(),
                A.RandomRotate90(),
                A.Cutout(num_holes=8, max_h_size=8, max_w_size=8, fill_value=0, always_apply=False),
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

