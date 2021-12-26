from torch.optim.lr_scheduler import StepLR

from parse_config import ConfigParser
from trainer import Trainer
from utils import prepare_device
from utils import get_splited_data
import model.loss as module_loss
import model.metric as module_metric
import torch.optim as optim
import logging
import numpy as np
import torch
import model.stn as module_stn
import utils
SEED = 123
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(SEED)
import torch
import data_loader.data_loaders as data_loaders
import torchvision.models as models
import torch.nn as nn



def main():
    # added logger to track change
    logger = logging.getLogger("trian")
    # Read the config.json
    config = ConfigParser.from_args()

    data_loader = data_loaders.get_train_data_loader(512)

    valid_data_loader = data_loaders.get_test_data_loader(512)

    # build model architecture, then print to console
    model = module_stn.STNModel()

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

    # optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    # lr_scheduler = StepLR(optimizer, step_size=20, gamma=0.1)
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    lr_scheduler = StepLR(optimizer, step_size=15, gamma=0.1)

    trainer = Trainer(model, criterion, metrics, optimizer,
                      config=config,
                      device=device,
                      data_loader=data_loader,
                      valid_data_loader=valid_data_loader,
                      lr_scheduler=lr_scheduler)

    trainer.train()
    # utils.showandcam_missclassifiedimage(trainer)
    # utils.showaccuracy_and_loss_curve(trainer)
   # utils.showandcam_missclassifiedimage(trainer)
   # utils.showaccuracy_and_loss_curve(trainer)

    return trainer


if __name__ == '__main__':
    trainer = main()
    # utils.showandcam_missclassifiedimage(trainer)

