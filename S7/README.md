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


Depthwise Separable Convoltion

Normal 2D convolutions require a larger and larger number of parameters as the number of feature maps increases. 
DepthWise Separable are used as an alternative to standard 2D convolutions as a way to reduce the number of parameters. 
These new convolutions help to achieve much smaller footprints and runtimes to run on less powerful hardware.

in depthwise separable convolutions we have convolution per channel. 

![image](https://user-images.githubusercontent.com/70502759/141686156-63d62ab4-cea0-49e3-ac17-72bdedec5542.png)


Afterwards we have maps that model the spatial interactions independently of channels, so we apply another convolution that then models the 
channel interactions. This second operation is often called a pointwise convolution, because it uses a kernel of size 1x1.


![image](https://user-images.githubusercontent.com/70502759/141687691-6529046f-4426-4bb7-9dbb-ceba64481c0b.png)

Transpose convolution

Inorder to achive receptive field of 54 we have used transpose convolution for upsampling the image . 
Transpose convolution can be used when we want to do  image-to-image mapping, like image or instance segmentation, or super-resolution where we need upsampling of the image inorder to map with original image resolution . 

![image](https://user-images.githubusercontent.com/70502759/141686377-39282168-3372-4399-9b78-b763c28226af.png)


Atrous convolution or Dilated convolution

its is akin to the standard convolution except that the weights of an atrous convolution kernel are spaced r locations apart
Dilated convolution is a way of increasing receptive view (global view) of the network exponentially and linear parameter accretion.

![image](https://user-images.githubusercontent.com/70502759/141687747-9763f03d-0e7a-4b8a-93a7-02ea1d1d3f63.png)

Albumentations

Albumentations is a computer vision tool that boosts the performance of deep convolutional neural networks with the help of Image augmentation.
Image augmentation is used in deep learning and computer vision tasks to increase the quality of trained models. 
The purpose of image augmentation is to create new training samples from the existing data.
Albumentations is fast compared to other image augmentation


Model Summery


        Layer (type)               Output Shape         Param #
            Conv2d-1            [-1, 3, 32, 32]              27
       BatchNorm2d-2            [-1, 3, 32, 32]               6
              ReLU-3            [-1, 3, 32, 32]               0
            Conv2d-4          [-1, 256, 32, 32]             768
       BatchNorm2d-5          [-1, 256, 32, 32]             512
              ReLU-6          [-1, 256, 32, 32]               0
            Conv2d-7          [-1, 256, 32, 32]           2,304
       BatchNorm2d-8          [-1, 256, 32, 32]             512
              ReLU-9          [-1, 256, 32, 32]               0
           Conv2d-10           [-1, 40, 32, 32]          10,240
      BatchNorm2d-11           [-1, 40, 32, 32]              80
             ReLU-12           [-1, 40, 32, 32]               0
      ConvTranspose2d-13      [-1, 185, 48, 48]          66,600
      BatchNorm2d-14          [-1, 185, 48, 48]             370
             ReLU-15          [-1, 185, 48, 48]               0
           Conv2d-16           [-1, 10, 16, 16]          16,650
      BatchNorm2d-17           [-1, 10, 16, 16]              20
             ReLU-18           [-1, 10, 16, 16]               0
        AvgPool2d-19             [-1, 10, 1, 1]               0
       
       Total params: 98,089
       Trainable params: 98,089
       Non-trainable params: 0
       Input size (MB): 0.01
       Forward/backward pass size (MB): 22.82
       Params size (MB): 0.37
       Estimated Total Size (MB): 23.21

Repective Field

![receptivefield](https://user-images.githubusercontent.com/70502759/141752462-ab9373db-e000-45f5-bd90-a7d9d3e72b9d.PNG)


Highest Train accuracy 87.18483664772727

Highest Test accuracy  81.94224683544304

Traing Logs from last few Epoch :
           
    epoch          : 101
    loss           : 0.3735793466383422
    accuracy       : 87.20037286931819
    val_loss       : 0.5666442566280123
    val_accuracy   : 80.89398734177215

    epoch          : 102
    loss           : 0.37442579463293607
    accuracy       : 87.17595880681819
    val_loss       : 0.5710155354647697
    val_accuracy   : 81.21044303797468

    epoch          : 103
    loss           : 0.3774511387190697
    accuracy       : 86.99840198863636
    val_loss       : 0.5720348908931394
    val_accuracy   : 80.85443037974683

    epoch          : 104
    loss           : 0.37464344304647634
    accuracy       : 87.17151988636364
    val_loss       : 0.5637746902206277
    val_accuracy   : 80.69620253164557

    epoch          : 105
    loss           : 0.37160827770871535
    accuracy       : 87.24920099431819
    val_loss       : 0.558854008022743
    val_accuracy   : 80.67642405063292

    epoch          : 106
    loss           : 0.37279849736527965
    accuracy       : 87.18483664772727
    val_loss       : 0.5401198875300491
    val_accuracy   : 81.94224683544304

    epoch          : 107
    loss           : 0.37206681455824187
    accuracy       : 87.06720525568181
    val_loss       : 0.5739287771756136
    val_accuracy   : 80.65664556962025

    epoch          : 108
    loss           : 0.375405817207965
    accuracy       : 86.98952414772727
    val_loss       : 0.5642091514943521
    val_accuracy   : 81.28955696202532

    epoch          : 109
    loss           : 0.37125248658809473
    accuracy       : 87.39124644886364
    val_loss       : 0.5463553806648979
    val_accuracy   : 81.40822784810126

    epoch          : 110
    loss           : 0.3708342405840416
    accuracy       : 87.3046875
    val_loss       : 0.5684251975786837
    val_accuracy   : 81.54667721518987

    epoch          : 111
    loss           : 0.3698449735106392
    accuracy       : 87.39790482954545
    val_loss       : 0.5811776005769078
    val_accuracy   : 80.59731012658227

    epoch          : 112
    loss           : 0.36853508521083067
    accuracy       : 87.29137073863636
    val_loss       : 0.5633809627800048
    val_accuracy   : 81.03243670886076

    epoch          : 113
    loss           : 0.37019252675500786
    accuracy       : 87.3202237215909
    val_loss       : 0.5690334782570223
    val_accuracy   : 81.23022151898734
   

## Tech Stack

Client: Python, Pytorch, Numpy


  
