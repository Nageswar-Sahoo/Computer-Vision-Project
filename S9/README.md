Design Nenural newtwork architecture with following constarint :

     We will be exploring the resnet architecture with GradCam .

Data Overview

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

Here are the classes in the dataset, as well as 10 random images from each:
![image](https://user-images.githubusercontent.com/70502759/141685528-79bce9e3-7de7-4613-8beb-b13d1e59d79d.png)

Resnet 18 Model Overview : 

      
        Layer (type)               Output Shape         Param #
            Conv2d-1           [-1, 64, 32, 32]           1,728
       BatchNorm2d-2           [-1, 64, 32, 32]             128
            Conv2d-3           [-1, 64, 32, 32]          36,864
       BatchNorm2d-4           [-1, 64, 32, 32]             128
            Conv2d-5           [-1, 64, 32, 32]          36,864
       BatchNorm2d-6           [-1, 64, 32, 32]             128
        BasicBlock-7           [-1, 64, 32, 32]               0
            Conv2d-8           [-1, 64, 32, 32]          36,864
       BatchNorm2d-9           [-1, 64, 32, 32]             128
           Conv2d-10           [-1, 64, 32, 32]          36,864
      BatchNorm2d-11           [-1, 64, 32, 32]             128
       BasicBlock-12           [-1, 64, 32, 32]               0
           Conv2d-13          [-1, 128, 16, 16]          73,728
      BatchNorm2d-14          [-1, 128, 16, 16]             256
           Conv2d-15          [-1, 128, 16, 16]         147,456
      BatchNorm2d-16          [-1, 128, 16, 16]             256
           Conv2d-17          [-1, 128, 16, 16]           8,192
      BatchNorm2d-18          [-1, 128, 16, 16]             256
       BasicBlock-19          [-1, 128, 16, 16]               0
           Conv2d-20          [-1, 128, 16, 16]         147,456
      BatchNorm2d-21          [-1, 128, 16, 16]             256
           Conv2d-22          [-1, 128, 16, 16]         147,456
      BatchNorm2d-23          [-1, 128, 16, 16]             256
       BasicBlock-24          [-1, 128, 16, 16]               0
           Conv2d-25            [-1, 256, 8, 8]         294,912
      BatchNorm2d-26            [-1, 256, 8, 8]             512
           Conv2d-27            [-1, 256, 8, 8]         589,824
      BatchNorm2d-28            [-1, 256, 8, 8]             512
           Conv2d-29            [-1, 256, 8, 8]          32,768
      BatchNorm2d-30            [-1, 256, 8, 8]             512
       BasicBlock-31            [-1, 256, 8, 8]               0
           Conv2d-32            [-1, 256, 8, 8]         589,824
      BatchNorm2d-33            [-1, 256, 8, 8]             512
           Conv2d-34            [-1, 256, 8, 8]         589,824
      BatchNorm2d-35            [-1, 256, 8, 8]             512
       BasicBlock-36            [-1, 256, 8, 8]               0
           Conv2d-37            [-1, 512, 4, 4]       1,179,648
      BatchNorm2d-38            [-1, 512, 4, 4]           1,024
           Conv2d-39            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-40            [-1, 512, 4, 4]           1,024
           Conv2d-41            [-1, 512, 4, 4]         131,072
      BatchNorm2d-42            [-1, 512, 4, 4]           1,024
       BasicBlock-43            [-1, 512, 4, 4]               0
           Conv2d-44            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-45            [-1, 512, 4, 4]           1,024
           Conv2d-46            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-47            [-1, 512, 4, 4]           1,024
       BasicBlock-48            [-1, 512, 4, 4]               0
           Linear-49                   [-1, 10]           5,130
    Total params: 11,173,962  
    Trainable params: 11,173,962
    Non-trainable params: 0

    Input size (MB): 0.01
    Forward/backward pass size (MB): 11.25
    Params size (MB): 42.63
    Estimated Total Size (MB): 53.89
    
Result
The model was trained for 20 epochs -

Highest Training Accuracy achieved - 82.86%
Highest Test Accuracy achieved - 80.63 

![image](https://user-images.githubusercontent.com/70502759/143260076-c895aafd-2e71-49df-a869-8b93358c9c60.png)


Misclassified and GradCam Images Gallery

Misclassified images were generated and for each misclassified image a gradcam image was generated for the misclassified class the model predicted.



![image](https://user-images.githubusercontent.com/70502759/143198134-1f9588a6-16e8-4b2e-bed8-46f2a9d3116b.png)

![image](https://user-images.githubusercontent.com/70502759/143198221-60eb79c1-3734-4d5b-aca9-980714ab28fb.png)

![image](https://user-images.githubusercontent.com/70502759/143198248-e1f07ffd-7b9b-48da-8cff-597d939d0066.png)

![image](https://user-images.githubusercontent.com/70502759/143198348-173c20bd-de65-45ad-8260-ad287b71111d.png)

![image](https://user-images.githubusercontent.com/70502759/143198411-2f1ecfe7-901f-4bab-970a-f48ee369699a.png)

![image](https://user-images.githubusercontent.com/70502759/143198457-397b698f-e64d-45d1-b189-6fb4e866ddb2.png)

![image](https://user-images.githubusercontent.com/70502759/143198485-6152c2d4-49d4-472b-b385-210e34738281.png)

![image](https://user-images.githubusercontent.com/70502759/143198548-d069b37e-281e-47a6-9492-d9f0a5c74864.png)

![image](https://user-images.githubusercontent.com/70502759/143198650-83a7193c-453b-4ac6-baf8-f673027ee81d.png)

![image](https://user-images.githubusercontent.com/70502759/143198939-3ed132b0-0fd2-4ca0-a6db-df5768f6b217.png)

![image](https://user-images.githubusercontent.com/70502759/143199037-5ca5055c-6398-42ac-a6a0-b45102e6785a.png)

![image](https://user-images.githubusercontent.com/70502759/143199093-7b4e275c-97dd-4f3f-9476-5e8c7de8075d.png)

![image](https://user-images.githubusercontent.com/70502759/143199133-bffd7b83-b886-4fc9-a86b-275fce750ebb.png)

![image](https://user-images.githubusercontent.com/70502759/143199164-a8782f8e-0b09-4458-a97c-d014b44a0ecc.png)

![image](https://user-images.githubusercontent.com/70502759/143199194-7491a2d4-9538-497f-910f-7a4c916b06ef.png)

![image](https://user-images.githubusercontent.com/70502759/143199243-1745a5dc-00a3-47b0-b705-25f86d8b0664.png)

![image](https://user-images.githubusercontent.com/70502759/143199314-085aeacb-c7ad-4af7-8719-4faa31f43c9b.png)

![image](https://user-images.githubusercontent.com/70502759/143199449-915f805e-53b9-4999-a29c-3a6a875d70c9.png)

![image](https://user-images.githubusercontent.com/70502759/143199489-529b87c2-4768-4132-a408-3518fcacba21.png)

![image](https://user-images.githubusercontent.com/70502759/143199542-9736a31f-9dc6-4ae3-9834-126bd99ed008.png)

![image](https://user-images.githubusercontent.com/70502759/143199568-9588ac44-972a-4276-9cd6-02ee9cb6364b.png)

![image](https://user-images.githubusercontent.com/70502759/143199589-9f7a5246-cb84-471d-8f8e-8cea1b8be563.png)



Project template repo link : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/tree/main/template



