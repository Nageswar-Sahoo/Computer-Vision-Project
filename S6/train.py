import importlib
import data_loader.data_loaders as module_data
from parse_config import ConfigParser
from trainer import Trainer
from utils import prepare_device
import argparse
import collections
import torch
import numpy as np
import model.loss as module_loss
import model.metric as module_metric
import model.model as module_arch
import matplotlib.pyplot as plt
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR
import logging

SEED = 123
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True

torch.backends.cudnn.benchmark = False
np.random.seed(SEED)


def main(config, normalizationtype='Layer'):
    logger = logging.getLogger("trian")
    # setup data_loader instances
    data_loader = module_data.MnistDataLoader(data_dir='data/', batch_size=64, shuffle=True, validation_split=0.1,
                                              num_workers=2, training=True)
    valid_data_loader = data_loader.split_validation()

    # build model architecture, then print to console
    model = module_arch.MnistModel(normalizationtype=normalizationtype)
    logger.info(model)

    # prepare for (multi-device) GPU training
    n_gpu = 1
    device, device_ids = prepare_device(n_gpu)
    model = model.to(device)
    if len(device_ids) > 1:
        model = torch.nn.DataParallel(model, device_ids=device_ids)

    # get function handles of loss and metrics
    loss = module_loss
    criterion = module_loss.nll_loss
    metrics = [module_metric.accuracy]

    # build optimizer, learning rate scheduler. delete every lines containing lr_scheduler for disabling scheduler
    trainable_params = filter(lambda p: p.requires_grad, model.parameters())
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    lr_scheduler = StepLR(optimizer, step_size=3, gamma=0.1)
    trainer = Trainer(model, criterion, metrics, optimizer,
                      config=config,
                      device=device,
                      data_loader=data_loader,
                      valid_data_loader=valid_data_loader,
                      type=normalizationtype,
                      lambda_l1=.01,
                      lr_scheduler=lr_scheduler)

    trainer.train()
    n_samples = len(data_loader.sampler)
    return trainer


if __name__ == '__main__':
    args = argparse.ArgumentParser(description='PyTorch Template')

    # custom cli options to modify configuration from default values given in json file.
    CustomArgs = collections.namedtuple('CustomArgs', 'flags type target')
    options = [
            ]
    config = ConfigParser.from_args(args, options)

    trainer_layer = main(config, 'Layer')
    trainer_batch = main(config, 'Batch')
    trainer_group = main(config, 'Group')
    metrics = [module_metric.accuracy]
    print('Accuracy  List ')
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].plot(trainer_batch.train_losses, color='r', label='BatchNorm')
    axs[0, 0].plot(trainer_layer.train_losses, color='g', label='LayerNorm')
    axs[0, 0].plot(trainer_group.train_losses, color='b', label='GroupNorm')
    axs[0, 0].set_title("Training Loss")
    axs[0, 0].legend(loc='upper right')
    axs[1, 0].plot(trainer_batch.train_acc, color='r', label='BatchNorm')
    axs[1, 0].plot(trainer_layer.train_acc, color='g', label='LayerNorm')
    axs[1, 0].plot(trainer_group.train_acc, color='b', label='GroupNorm')
    axs[1, 0].set_title("Training accuracy")
    axs[1, 0].legend(loc='lower right')
    axs[0, 1].plot(trainer_batch.test_losses, color='r', label='BatchNorm')
    axs[0, 1].plot(trainer_layer.test_losses, color='g', label='LayerNorm')
    axs[0, 1].plot(trainer_group.test_losses, color='b', label='GroupNorm')
    axs[0, 1].set_title("Test Loss")
    axs[0, 1].legend(loc='upper right')
    axs[1, 1].plot(trainer_batch.test_acc, color='r', label='BatchNorm')
    axs[1, 1].plot(trainer_layer.test_acc, color='g', label='LayerNorm')
    axs[1, 1].plot(trainer_group.test_acc, color='b', label='GroupNorm')
    axs[1, 1].set_title("Test Accuracy")
    axs[1, 1].legend(loc='lower right')
    plt.legend()
    plt.show()




