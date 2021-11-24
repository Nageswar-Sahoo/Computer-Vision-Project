Design Nenural newtwork architecture with following constarint :


    1>Use architecture  C1C2C3C40 (Use Dilated kernels)
    2>total RF must be more than 52
    3>two of the layers must use Depthwise Separable Convolution
    4>one of the layers must use Dilated Convolution
    5>use GAP
    6>use albumentation library and apply:
      1>horizontal flip
      2>shiftScaleRotate 
      3>coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, 
                         fill_value=(mean of your dataset), mask_fill_value = None)  
      4>grayscale
    7>achieve 87% accuracy, as many epochs as you want. Total Params to be less than 100k.

Data Overview

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

Here are the classes in the dataset, as well as 10 random images from each:
![image](https://user-images.githubusercontent.com/70502759/141685528-79bce9e3-7de7-4613-8beb-b13d1e59d79d.png)
