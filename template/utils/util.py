import json
import pandas as pd
from pathlib import Path
from itertools import repeat
from collections import OrderedDict
import matplotlib.pyplot as plt
import cv2
import numpy as np
import torch

from .grad_cam import GradCAM
from .image import show_cam_on_image

SEED = 123
torch.manual_seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
np.random.seed(SEED)

def ensure_dir(dirname):
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)

def read_json(fname):
    fname = Path(fname)
    with fname.open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)


def showandcam_missclassifiedimage(trainer):
    classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog",
               "horse", "ship", "truck"]
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = trainer.model
    missclassifiedimage = []
    missclassifiedimage_actual_label = []
    missclassifiedimage_predicted_label = []
    missclassifiedimage_cam = []
    target_layers = [model.layer2[-1]]
    target_category = None
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(trainer.valid_data_loader):
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            pred = pred.cpu().numpy()
            target = target.cpu().numpy()
            data = data.cpu().numpy()
            for i in range(len(target)):
                if pred[i] != target[i]:
                    missclassifiedimage.append(data[i])
                    missclassifiedimage_actual_label.append(target[i])
                    missclassifiedimage_predicted_label.append(pred[i][0])
    for i in range(20):
        img = np.moveaxis(missclassifiedimage[i], 0, 2)
        img = np.float32(cv2.resize(img, (32, 32))) / 255
        img_r = np.moveaxis(img, -1, 0)
        preprocessed_img = torch.from_numpy(img_r)
        preprocessed_img.unsqueeze_(0)
        cam = GradCAM(model=model, target_layers=target_layers, use_cuda=False)
        grayscale_cam = cam(input_tensor=preprocessed_img, target_category=target_category)
        grayscale_cam = grayscale_cam[0, :]
        cam_image_op = show_cam_on_image(img, grayscale_cam, use_rgb=False)
        missclassifiedimage_cam.append(cam_image_op)

    for idx in np.arange(20):
        print(idx)
        fig, ax1 = plt.subplots(1, 2)
        im = missclassifiedimage[idx]
        im = np.moveaxis(im, 0, 2)
        im_resized = cv2.resize(im, (200, 200), interpolation=cv2.INTER_LINEAR)
        cam_im = missclassifiedimage_cam[idx]
        cam_im_resized = cv2.resize(cam_im, (200, 200), interpolation=cv2.INTER_LINEAR)
        ax1[0].imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
        ax1[0].title.set_text(
            str('Actual Lable ') + classes[missclassifiedimage_actual_label[idx]] + str('\nPredicted Lable ') +
            classes[
                missclassifiedimage_predicted_label[idx]])
        ax1[1].imshow(cv2.cvtColor(cam_im_resized, cv2.COLOR_BGR2RGB))


def write_json(content, fname):
    fname = Path(fname)
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)

def inf_loop(data_loader):
    ''' wrapper function for endless data loader. '''
    for loader in repeat(data_loader):
        yield from loader

def prepare_device(n_gpu_use):
    """
    setup GPU device if available. get gpu device indices which are used for DataParallel
    """
    n_gpu = torch.cuda.device_count()
    if n_gpu_use > 0 and n_gpu == 0:
        print("Warning: There\'s no GPU available on this machine,"
              "training will be performed on CPU.")
        n_gpu_use = 0
    if n_gpu_use > n_gpu:
        print(f"Warning: The number of GPU\'s configured to use is {n_gpu_use}, but only {n_gpu} are "
              "available on this machine.")
        n_gpu_use = n_gpu
    device = torch.device('cuda:0' if n_gpu_use > 0 else 'cpu')
    list_ids = list(range(n_gpu_use))
    return device, list_ids

class MetricTracker:
    def __init__(self, *keys, writer=None):
        self.writer = writer
        self._data = pd.DataFrame(index=keys, columns=['total', 'counts', 'average'])
        self.reset()

    def reset(self):
        for col in self._data.columns:
            self._data[col].values[:] = 0

    def update(self, key, value, n=1):
        if self.writer is not None:
            self.writer.add_scalar(key, value)
        self._data.total[key] += value * n
        self._data.counts[key] += n
        self._data.average[key] = self._data.total[key] / self._data.counts[key]

    def avg(self, key):
        return self._data.average[key]

    def result(self):
        return dict(self._data.average)

