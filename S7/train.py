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

SEED = 123
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(SEED)


##Reference Template used for the project : https://github.com/victoresque/pytorch-template
# https://colab.research.google.com/drive/1z6OOQep6vQhSk65tXUbyqF2s6S-_Kz-C#scrollTo=VcqfrY6NQ5ye


def main():
    # added logger to track change
    logger = logging.getLogger("trian")
    # Read the config.json
    config = ConfigParser.from_args()

    # setup data_loader instances
    data_loader = module_data.CIFRDataLoader(data_dir='data/', batch_size=64, shuffle=True, validation_split=0.1,
                                             num_workers=2, training=True)
    valid_data_loader = data_loader.split_validation()

    # build model architecture, then print to console
    model = module_arch.CIFRModel()
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


if __name__ == '__main__':
    trainer_layer = main()
