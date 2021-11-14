Design Nenural newtwork architecture with following constarint :


    1>Use architecture  C1C2C3C40 (Use Dilated kernels)
    2>total RF must be more than 52
    3>two of the layers must use Depthwise Separable Convolution
    4>one of the layers must use Dilated Convolution
    5>use GAP
    6>use albumentation library and apply:
      1>horizontal flip
      2>shiftScaleRotate 
      3>coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)  
      4>grayscale
    7>achieve 87% accuracy, as many epochs as you want. Total Params to be less than 100k.

Data Overview

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

Here are the classes in the dataset, as well as 10 random images from each:
![image](https://user-images.githubusercontent.com/70502759/141685528-79bce9e3-7de7-4613-8beb-b13d1e59d79d.png)


Depthwise Separable Convoltion

Normal 2D convolutions require a larger and larger number of parameters as the number of feature maps increases. 
DepthWise Separable are used as an alternative to standard 2D convolutions as a way to reduce the number of parameters. 
These new convolutions help to achieve much smaller footprints and runtimes to run on less powerful hardware.

in depthwise separable convolutions we have convolution per channel. 

![image](https://user-images.githubusercontent.com/70502759/141686156-63d62ab4-cea0-49e3-ac17-72bdedec5542.png)


Afterwards we have maps that model 
the spatial interactions independently of channels, so we apply another convolution that then models the 
channel interactions. This second operation is often called a pointwise convolution, because it uses a 
kernel of size 1x1.

![image](https://user-images.githubusercontent.com/70502759/141686285-365b3806-f195-4c07-a77c-33e3a4e95779.png)

![image](https://user-images.githubusercontent.com/70502759/141687691-6529046f-4426-4bb7-9dbb-ceba64481c0b.png)


inorder to achive receptive field of 54 we have used transpose convolution for upsampling the image . 
transpose convolution can be used when we want to do  image-to-image mapping, like image or instance segmentation, or super-resolution

![image](https://user-images.githubusercontent.com/70502759/141686377-39282168-3372-4399-9b78-b763c28226af.png)



Atrous convolution or Dilated convolution is akin to the standard convolution except that
the weights of an atrous convolution kernel are spaced r locations apart
Dilated convolution is a way of increasing receptive view (global view) of the network exponentially and linear parameter accretion.

![image](https://user-images.githubusercontent.com/70502759/141687747-9763f03d-0e7a-4b8a-93a7-02ea1d1d3f63.png)



## Tech Stack

Client: Python, Pytorch, Numpy

  

## Tech Stack

Client: Python, Pytorch, Numpy

  
