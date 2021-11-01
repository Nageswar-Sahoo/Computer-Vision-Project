# S6

Data Overview


MNIST ("Modified National Institute of Standards and Technology") dataset of computer vision. The MNIST database contains 60,000 training images and 10,000 testing images. Half of the training set and half of the test set were taken from NIST's training dataset, while the other half of the training set and the other half of the test set were taken from NIST's testing dataset.This project implements a beginner classification task on MNIST dataset with a Convolutional Neural Network(CNN) model.

![image](https://user-images.githubusercontent.com/70502759/137764343-c1134fa1-94d2-40b0-bf21-dcd78b3ed4e1.png)
  
  This project will automatically dowload and process the MNIST dataset

Normalization

The basic idea behind normalization is to normalize the output of an activation layer to improve the convergence during training.
Also normalization reduces Internal Covariate Shift. It is the change in the distribution of network activations due to the change in network parameters during training. To improve the training, we seek to reduce the internal covariate shift.

Different type of Normalization :

 1 - BatchNormalization
 
 2 - LayerNormalization
 
 3 - GroupNormalization
 
 4 - InstaceNormalization


BatchNorm 

Batch normalization works for each filter seperately using all the output of that filter 
i.e Batch normalization is a method that normalizes activations in a network across the mini-batch of definite size
![1](https://user-images.githubusercontent.com/70502759/139624272-8ecc8dbf-dec7-4769-9658-c8defec4f760.png)

Ex :  

     image1 = [ [[2, 3]], [[5, 7]], [[11, 13]], [[17, 19]] ]
     image2 = [ [[0, 1]], [[1, 2]], [[3, 5]], [[8, 13]] ]
     image3 = [ [[1, 2]], [[3, 4]], [[5, 6]], [[7, 8]] ]

     𝜇1 = mean(2, 3, 0, 1, 1, 2) = 1.5
     𝜇2 = mean(5, 7, 1, 2, 3, 4) = 3.66
     𝜇3 = mean(11, 13, 3, 5, 5, 6) = 7.16
     𝜇4 = mean(17, 19, 8, 13, 7, 8) = 12.0

     𝜎1 = std(2, 3, 0, 1, 1, 2) = .91
     𝜎2 = std(5, 7, 1, 2, 3, 4) = 1.97
     𝜎3 = std(11, 13, 3, 5, 5, 6) = 3.57
     𝜎4 = std(17, 19, 8, 13, 7, 8) = 4.6

    Above mean and std can be used to normalize the output along with 8 learnable params 



   
    1 -  Model Summary
      
        
        Layer (type)               Output Shape         Param #
 
            Conv2d-1            [-1, 8, 26, 26]              72
       BatchNorm2d-2            [-1, 8, 26, 26]              16
           Dropout-3            [-1, 8, 26, 26]               0
              ReLU-4            [-1, 8, 26, 26]               0
            Conv2d-5            [-1, 8, 24, 24]             576
       BatchNorm2d-6            [-1, 8, 24, 24]              16
           Dropout-7            [-1, 8, 24, 24]               0
              ReLU-8            [-1, 8, 24, 24]               0
            Conv2d-9            [-1, 8, 22, 22]             576
      BatchNorm2d-10            [-1, 8, 22, 22]              16
          Dropout-11            [-1, 8, 22, 22]               0
             ReLU-12            [-1, 8, 22, 22]               0
        MaxPool2d-13            [-1, 8, 11, 11]               0
           Conv2d-14             [-1, 12, 9, 9]             864
      BatchNorm2d-15             [-1, 12, 9, 9]              24
          Dropout-16             [-1, 12, 9, 9]               0
             ReLU-17             [-1, 12, 9, 9]               0
           Conv2d-18             [-1, 14, 7, 7]           1,512
      BatchNorm2d-19             [-1, 14, 7, 7]              28
          Dropout-20             [-1, 14, 7, 7]               0
             ReLU-21             [-1, 14, 7, 7]               0
           Conv2d-22              [-1, 8, 7, 7]             112
      BatchNorm2d-23              [-1, 8, 7, 7]              16
          Dropout-24              [-1, 8, 7, 7]               0
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 26, 5, 5]           1,872
      BatchNorm2d-27             [-1, 26, 5, 5]              52
          Dropout-28             [-1, 26, 5, 5]               0
             ReLU-29             [-1, 26, 5, 5]               0
           Conv2d-30             [-1, 50, 5, 5]           1,300
      BatchNorm2d-31             [-1, 50, 5, 5]             100
          Dropout-32             [-1, 50, 5, 5]               0
             ReLU-33             [-1, 50, 5, 5]               0
        AvgPool2d-34             [-1, 50, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             500
 
       Total params: 7,652
       Trainable params: 7,652
       Non-trainable params: 0

       Input size (MB): 0.00
       Forward/backward pass size (MB): 0.55
       Params size (MB): 0.03
       Estimated Total Size (MB): 0.58

 


LayerNorm



![3](https://user-images.githubusercontent.com/70502759/139624298-69fe4231-843c-4e9c-9d34-7da88dcf3770.png)

Layer Normalization work for each input seperately using output of all the filter for that input
The mean and standard deviation is calculated from all activations of a single sample.

     image1 = [ [[2, 3]], [[5, 7]], [[11, 13]], [[17, 19]] ]
     image2 = [ [[0, 1]], [[1, 2]], [[3, 5]], [[8, 13]] ]
     image3 = [ [[1, 2]], [[3, 4]], [[5, 6]], [[7, 8]] ]

     𝜇1 = mean(2, 3, 5, 7, 11, 13, 17, 19) = 9.625
     𝜇2 = mean(0, 1, 1, 2, 3, 5, 8, 13) = 4.125
     𝜇3 = mean(1, 2, 3, 4, 5, 6, 7, 8) = 4.5

     𝜎1 = std(2, 3, 5, 7, 11, 13, 17, 19) = 5.97
     𝜎2 = std(0, 1, 1, 2, 3, 5, 8, 13) = 4.13
     𝜎3 = std(1, 2, 3, 4, 5, 6, 7, 8) = 2.29

    Above mean and std can be used to normalize the output along with 6 learnable params 
   
    1 -  Model Summary
      
        Layer (type)               Output Shape         Param #
            Conv2d-1            [-1, 8, 26, 26]              72
         LayerNorm-2            [-1, 8, 26, 26]              52
           Dropout-3            [-1, 8, 26, 26]               0
              ReLU-4            [-1, 8, 26, 26]               0
            Conv2d-5            [-1, 8, 24, 24]             576
         LayerNorm-6            [-1, 8, 24, 24]              48
           Dropout-7            [-1, 8, 24, 24]               0
              ReLU-8            [-1, 8, 24, 24]               0
            Conv2d-9            [-1, 8, 22, 22]             576
        LayerNorm-10            [-1, 8, 22, 22]              44
          Dropout-11            [-1, 8, 22, 22]               0
             ReLU-12            [-1, 8, 22, 22]               0
        MaxPool2d-13            [-1, 8, 11, 11]               0
           Conv2d-14             [-1, 12, 9, 9]             864
        LayerNorm-15             [-1, 12, 9, 9]              18
          Dropout-16             [-1, 12, 9, 9]               0
             ReLU-17             [-1, 12, 9, 9]               0
           Conv2d-18             [-1, 14, 7, 7]           1,512
        LayerNorm-19             [-1, 14, 7, 7]              14
          Dropout-20             [-1, 14, 7, 7]               0
             ReLU-21             [-1, 14, 7, 7]               0
           Conv2d-22              [-1, 8, 7, 7]             112
        LayerNorm-23              [-1, 8, 7, 7]              14
          Dropout-24              [-1, 8, 7, 7]               0
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 26, 5, 5]           1,872
        LayerNorm-27             [-1, 26, 5, 5]              10
          Dropout-28             [-1, 26, 5, 5]               0
             ReLU-29             [-1, 26, 5, 5]               0
           Conv2d-30             [-1, 50, 5, 5]           1,300
        LayerNorm-31             [-1, 50, 5, 5]              10
          Dropout-32             [-1, 50, 5, 5]               0
             ReLU-33             [-1, 50, 5, 5]               0
        AvgPool2d-34             [-1, 50, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             500

        Total params: 7,594
        Trainable params: 7,594
        Non-trainable params: 0

        Input size (MB): 0.00
        Forward/backward pass size (MB): 0.55
        Params size (MB): 0.03
        Estimated Total Size (MB): 0.58


  GroupNorm


  Group Normalization(GN) divides the channels of your inputs into smaller sub groups and normalizes these values based on their mean and variance. Since GN works on a single example this technique is batchsize independent.

     image1 = [ [[2, 3]], [[5, 7]], [[11, 13]], [[17, 19]] ]
     image2 = [ [[0, 1]], [[1, 2]], [[3, 5]], [[8, 13]] ]
     image3 = [ [[1, 2]], [[3, 4]], [[5, 6]], [[7, 8]] ]

     group of 2 
     𝜇1 = mean(2, 3, 5, 7) = 4.25
     𝜎1 = var(2, 3, 5, 7) = 1.9
     𝜇2 = mean( 11, 13, 17, 19) = 15.0
     𝜎2 = var( 11, 13, 17, 19) = 3.16
     𝜇3 = mean(0, 1, 1, 2) = 1.0
     𝜎3 = var(0, 1, 1, 2) = .70
     𝜇4 = mean(3, 5, 8, 13) = 7.25
     𝜎4 = var(3, 5, 8, 13) = 3.76
     𝜇5 = mean(1, 2, 3, 4) = 2.25
     𝜎5 = var(1, 2, 3, 4) = 1.11
     𝜇6 = mean( 5, 6, 7, 8) = 6.5
     𝜎6 = var( 5, 6, 7, 8) = 1.11

    Above mean and std can be used to normalize the output along with 12 learnable params 


        Layer (type)               Output Shape         Param #

            Conv2d-1            [-1, 8, 26, 26]              72
         GroupNorm-2            [-1, 8, 26, 26]              16
           Dropout-3            [-1, 8, 26, 26]               0
              ReLU-4            [-1, 8, 26, 26]               0
            Conv2d-5            [-1, 8, 24, 24]             576
         GroupNorm-6            [-1, 8, 24, 24]              16
           Dropout-7            [-1, 8, 24, 24]               0
              ReLU-8            [-1, 8, 24, 24]               0
            Conv2d-9            [-1, 8, 22, 22]             576
        GroupNorm-10            [-1, 8, 22, 22]              16
          Dropout-11            [-1, 8, 22, 22]               0
             ReLU-12            [-1, 8, 22, 22]               0
        MaxPool2d-13            [-1, 8, 11, 11]               0
           Conv2d-14             [-1, 12, 9, 9]             864
        GroupNorm-15             [-1, 12, 9, 9]              24
          Dropout-16             [-1, 12, 9, 9]               0
             ReLU-17             [-1, 12, 9, 9]               0
           Conv2d-18             [-1, 14, 7, 7]           1,512
        GroupNorm-19             [-1, 14, 7, 7]              28
          Dropout-20             [-1, 14, 7, 7]               0
             ReLU-21             [-1, 14, 7, 7]               0
           Conv2d-22              [-1, 8, 7, 7]             112
        GroupNorm-23              [-1, 8, 7, 7]              16
          Dropout-24              [-1, 8, 7, 7]               0
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 26, 5, 5]           1,872
        GroupNorm-27             [-1, 26, 5, 5]              52
          Dropout-28             [-1, 26, 5, 5]               0
             ReLU-29             [-1, 26, 5, 5]               0
           Conv2d-30             [-1, 50, 5, 5]           1,300
        GroupNorm-31             [-1, 50, 5, 5]             100
          Dropout-32             [-1, 50, 5, 5]               0
             ReLU-33             [-1, 50, 5, 5]               0
        AvgPool2d-34             [-1, 50, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             500

       Total params: 7,652
       Trainable params: 7,652
       Non-trainable params: 0

       Input size (MB): 0.00
       Forward/backward pass size (MB): 0.55
       Params size (MB): 0.03
       Estimated Total Size (MB): 0.58



![batch1](https://user-images.githubusercontent.com/70502759/139661480-f50e7cdd-b595-4001-9f1e-2ff0b41718e9.png)




Comparision of Accuracy and Loss across the train and test dataset

![image](https://user-images.githubusercontent.com/70502759/139662428-412e49ae-0eea-49a3-87cd-e949367e9012.png)




Misclassified Images
Batch Norm 
Layer Norm
Group Norm 
  

## Tech Stack

Client: Python, Pytorch, Numpy

  

## Tech Stack

Client: Python, Pytorch, Numpy

  
