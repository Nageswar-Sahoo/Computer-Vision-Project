import data_loader.data_loaders as module_data
from parse_config import ConfigParser
from trainer import Trainer
from utils import prepare_device
import torch
import numpy as np
import model.loss as module_loss
import model.metric as module_metric
import model.model as module_arch
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
import logging
import utils.grad_cam as grad_cam
import matplotlib.pyplot as plt

from utils import GradCAM, GuidedBackpropReLUModel
from utils.image import show_cam_on_image
import cv2
import numpy as np
import torch
import model.model as module_arch

SEED = 123
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(SEED)


##Reference Template used for the project : https://github.com/victoresque/pytorch-template
# https://colab.research.google.com/drive/1z6OOQep6vQhSk65tXUbyqF2s6S-_Kz-C#scrollTo=VcqfrY6NQ5ye
# https://github.com/yaleCat/Grad-CAM-pytorch/blob/master/visualization.ipynb


def main():
    # added logger to track change
    logger = logging.getLogger("trian")
    # Read the config.json
    config = ConfigParser.from_args()

    # setup data_loader instances
    data_loader = module_data.CIFRDataLoader(data_dir='data/', batch_size=64, shuffle=True, validation_split=0.1,
                                             num_workers=2, training=True)
    valid_data_loader = data_loader.split_validation()

    print("length")
    print(data_loader.valid_sampler)

    # build model architecture, then print to console
    model = module_arch.resnet34()
    logger.info(model)

    # prepare for (multi-device) GPU training
    n_gpu = 1
    device, device_ids = prepare_device(n_gpu)
    model = model.to(device)
    if len(device_ids) > 1:
        model = torch.nn.DataParallel(model, device_ids=device_ids)

    # get function handles of loss and metrics
    criterion = module_loss.crossentropyloss
    metrics = [module_metric.accuracy]

    optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
    lr_scheduler = StepLR(optimizer, step_size=120, gamma=0.1)
    trainer = Trainer(model, criterion, metrics, optimizer,
                      config=config,
                      device=device,
                      data_loader=data_loader,
                      valid_data_loader=valid_data_loader,
                      lr_scheduler=lr_scheduler)

    trainer.train()
    return trainer


def imshow(img):
    img = img / 2 + 0.5  # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()


if __name__ == '__main__':
    classes = ('plane', 'car', 'bird', 'cat',
               'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    trainer_layer = main()
    model = trainer_layer.model
    target_layers = [model.layer4[-1]]
    img = cv2.imread('C:/Users/NSA301/Desktop/AI_Latest/image/dog.jpg', 1)
    print(img.shape)
    img = np.float32(cv2.resize(img, (32, 32))) / 255
    img = np.moveaxis(img, -1, 0)
    preprocessed_img = torch.from_numpy(img)
    preprocessed_img.unsqueeze_(0)
    input_tensor = preprocessed_img
    # Create an input tensor image for your model..
    # Note: input_tensor can be a batch tensor with several images!

    # Construct the CAM object once, and then re-use it on many images:
    cam = GradCAM(model=model, target_layers=target_layers, use_cuda=args.use_cuda)

    # You can also use it within a with statement, to make sure it is freed,
    # In case you need to re-create it inside an outer loop:
    # with GradCAM(model=model, target_layers=target_layers, use_cuda=args.use_cuda) as cam:
    #   ...

    # If target_category is None, the highest scoring category
    # will be used for every image in the batch.
    # target_category can also be an integer, or a list of different integers
    # for every image in the batch.
    target_category = None

    # You can also pass aug_smooth=True and eigen_smooth=True, to apply smoothing.
    grayscale_cam = cam(input_tensor=input_tensor, target_category=target_category)

    # In this example grayscale_cam has only one image in the batch:
    grayscale_cam = grayscale_cam[0, :]
    visualization = show_cam_on_image(img, grayscale_cam, use_rgb=True)
