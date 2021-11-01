# Session - 6 Assignment

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



  GroupNorm


  Group Normalization(GN) divides the channels of your inputs into smaller sub groups and normalizes these values based on their mean and variance. 

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





![batch1](https://user-images.githubusercontent.com/70502759/139661480-f50e7cdd-b595-4001-9f1e-2ff0b41718e9.png)

  
  ## Requirement

To create 3 versions of models with the best network developed so far.

- Version 1 Model with Batch Normalization and L1 Regularization
- Version 2 Model with Layer Normalization
- Version 3 Model with Group Normalization 

- There must a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include
- A single notebook file to run all the 3 models above for 20 epochs each
- Graph 1: Test/Validation Loss for all 3 models together
- Graph 2: Test/Validation Accuracy for 3 models together
- 10 misclassified images for each of the 3 models, as a 5x2 image matrix in 3 separately annotated images. 


## Approach

The network class was modified to accept a parameter that would decide the type of normalization to be used.
Parameter values as below:
B - For BN + L1 Regularization
L - For Layer Normalization
G - For group Normalization (Group of 4 per layer has been used for this assignment)

The Network class has been saved in a different file named as model.py
A Notebook file was created to create 3 versions of the model.

For L1 regularization the Train function has been modified to use mse loss function. The predicted tensor output from the model has been reshaped(Used argmax) to match with the target tensor shape. This was needed to make it compatible with mse loss function. The train function has also been modified to return a list of train loss and train accuracy.

The Test fucntion has been modified to return a list of test loss and test accuracy. This was needed to plot the graph for all 3 models.


## Model Summary

### Version -1 (Model with BN + L1)
<pre>
The model parameters for Batch Normalization

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              72
       BatchNorm2d-2            [-1, 8, 26, 26]              16
              ReLU-3            [-1, 8, 26, 26]               0
            Conv2d-4            [-1, 8, 24, 24]             576
       BatchNorm2d-5            [-1, 8, 24, 24]              16
              ReLU-6            [-1, 8, 24, 24]               0
            Conv2d-7            [-1, 8, 22, 22]             576
       BatchNorm2d-8            [-1, 8, 22, 22]              16
           Dropout-9            [-1, 8, 22, 22]               0
             ReLU-10            [-1, 8, 22, 22]               0
        MaxPool2d-11            [-1, 8, 11, 11]               0
           Conv2d-12             [-1, 16, 9, 9]           1,152
      BatchNorm2d-13             [-1, 16, 9, 9]              32
          Dropout-14             [-1, 16, 9, 9]               0
             ReLU-15             [-1, 16, 9, 9]               0
           Conv2d-16             [-1, 16, 7, 7]           2,304
      BatchNorm2d-17             [-1, 16, 7, 7]              32
          Dropout-18             [-1, 16, 7, 7]               0
             ReLU-19             [-1, 16, 7, 7]               0
           Conv2d-20              [-1, 8, 7, 7]             128
      BatchNorm2d-21              [-1, 8, 7, 7]              16
          Dropout-22              [-1, 8, 7, 7]               0
             ReLU-23              [-1, 8, 7, 7]               0
           Conv2d-24             [-1, 32, 5, 5]           2,304
      BatchNorm2d-25             [-1, 32, 5, 5]              64
          Dropout-26             [-1, 32, 5, 5]               0
             ReLU-27             [-1, 32, 5, 5]               0
           Conv2d-28             [-1, 16, 5, 5]             512
      BatchNorm2d-29             [-1, 16, 5, 5]              32
          Dropout-30             [-1, 16, 5, 5]               0
             ReLU-31             [-1, 16, 5, 5]               0
        AvgPool2d-32             [-1, 16, 1, 1]               0
           Conv2d-33             [-1, 10, 1, 1]             160
================================================================
Total params: 8,008
Trainable params: 8,008
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.47
Params size (MB): 0.03
Estimated Total Size (MB): 0.50
----------------------------------------------------------------
----------------------------------------------------------------

</pre>

### Version -2 (Model with Layer Normalization)
<pre>
The model parameters for Layer Mormalization

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              72
         LayerNorm-2            [-1, 8, 26, 26]               0
              ReLU-3            [-1, 8, 26, 26]               0
            Conv2d-4            [-1, 8, 24, 24]             576
         LayerNorm-5            [-1, 8, 24, 24]               0
              ReLU-6            [-1, 8, 24, 24]               0
            Conv2d-7            [-1, 8, 22, 22]             576
         LayerNorm-8            [-1, 8, 22, 22]               0
           Dropout-9            [-1, 8, 22, 22]               0
             ReLU-10            [-1, 8, 22, 22]               0
        MaxPool2d-11            [-1, 8, 11, 11]               0
           Conv2d-12             [-1, 16, 9, 9]           1,152
        LayerNorm-13             [-1, 16, 9, 9]               0
          Dropout-14             [-1, 16, 9, 9]               0
             ReLU-15             [-1, 16, 9, 9]               0
           Conv2d-16             [-1, 16, 7, 7]           2,304
        LayerNorm-17             [-1, 16, 7, 7]               0
          Dropout-18             [-1, 16, 7, 7]               0
             ReLU-19             [-1, 16, 7, 7]               0
           Conv2d-20              [-1, 8, 7, 7]             128
        LayerNorm-21              [-1, 8, 7, 7]               0
          Dropout-22              [-1, 8, 7, 7]               0
             ReLU-23              [-1, 8, 7, 7]               0
           Conv2d-24             [-1, 32, 5, 5]           2,304
        LayerNorm-25             [-1, 32, 5, 5]               0
          Dropout-26             [-1, 32, 5, 5]               0
             ReLU-27             [-1, 32, 5, 5]               0
           Conv2d-28             [-1, 16, 5, 5]             512
        LayerNorm-29             [-1, 16, 5, 5]               0
          Dropout-30             [-1, 16, 5, 5]               0
             ReLU-31             [-1, 16, 5, 5]               0
        AvgPool2d-32             [-1, 16, 1, 1]               0
           Conv2d-33             [-1, 10, 1, 1]             160
================================================================
Total params: 7,784
Trainable params: 7,784
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.47
Params size (MB): 0.03
Estimated Total Size (MB): 0.50
----------------------------------------------------------------
----------------------------------------------------------------

</pre>

### Version -3 (Model with Group Normalization)
<pre>
The model parameters for Group Mormalization

----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1            [-1, 8, 26, 26]              72
         GroupNorm-2            [-1, 8, 26, 26]              16
              ReLU-3            [-1, 8, 26, 26]               0
            Conv2d-4            [-1, 8, 24, 24]             576
         GroupNorm-5            [-1, 8, 24, 24]              16
              ReLU-6            [-1, 8, 24, 24]               0
            Conv2d-7            [-1, 8, 22, 22]             576
         GroupNorm-8            [-1, 8, 22, 22]              16
              ReLU-9            [-1, 8, 22, 22]               0
        MaxPool2d-10            [-1, 8, 11, 11]               0
           Conv2d-11             [-1, 16, 9, 9]           1,152
        GroupNorm-12             [-1, 16, 9, 9]              32
          Dropout-13             [-1, 16, 9, 9]               0
             ReLU-14             [-1, 16, 9, 9]               0
           Conv2d-15             [-1, 16, 7, 7]           2,304
        GroupNorm-16             [-1, 16, 7, 7]              32
          Dropout-17             [-1, 16, 7, 7]               0
             ReLU-18             [-1, 16, 7, 7]               0
           Conv2d-19              [-1, 8, 7, 7]             128
        GroupNorm-20              [-1, 8, 7, 7]              16
          Dropout-21              [-1, 8, 7, 7]               0
             ReLU-22              [-1, 8, 7, 7]               0
           Conv2d-23             [-1, 32, 5, 5]           2,304
        GroupNorm-24             [-1, 32, 5, 5]              64
          Dropout-25             [-1, 32, 5, 5]               0
             ReLU-26             [-1, 32, 5, 5]               0
           Conv2d-27             [-1, 16, 5, 5]             512
        GroupNorm-28             [-1, 16, 5, 5]              32
          Dropout-29             [-1, 16, 5, 5]               0
             ReLU-30             [-1, 16, 5, 5]               0
        AvgPool2d-31             [-1, 16, 1, 1]               0
           Conv2d-32             [-1, 10, 1, 1]             160
================================================================
Total params: 8,008
Trainable params: 8,008
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.44
Params size (MB): 0.03
Estimated Total Size (MB): 0.47
----------------------------------------------------------------

</pre>

## Model Results

### Test/Validation Loss for all 3 models together

![](/Images/S6_Images/Loss_Curve.jpg)


### Test/Validation Accuracy for all 3 models together

![](/Images/S6_Images/Acc_Curve.jpg)


### Train/Test Results for Version -1 (BN + L1 Model)
![](/Images/S6_Images/BN_Curve.png)

### Train/Test Results for Version -2 (Layer Normalization Model)
![](/Images/S6_Images/LN_Curve.png)

### Train/Test Results for Version -1 (Group Normalization Model)
![](/Images/S6_Images/GN_Curve.png)



## Misclassified Images

### The details of predicted vs actual value and the corresponding image have been shown in the notebook. The below grid are list of 10 unclassified images by the 3 models.

### Images misclassified by Version -1 Model (BN + L1)
![](/Images/S6_Images/BN_Unclassified.jpg)
### Images misclassified by Version -2 Model (Layer Normalization)
![](/Images/S6_Images/LN_Unclassified.jpg)
### Images misclassified by Version -3 Model (Group Normalization)
![](/Images/S6_Images/GN_Unclassified.jpg)



## Inference

The BN + L1 model behaves poorly. Probably because the L1 regularization is removing key/important features.
The LN and GN model are quite robust and fails on extreme cases as seen on the  misclassified examples.


## Team Members
Member 1: Moulipriya Pal

Member 2: Rahul Tyagi

Member 3: Vyas Dhruv

Member 4: Nageswar Sahoo

## Tech Stack

Client: Python, Pytorch, Numpy  
