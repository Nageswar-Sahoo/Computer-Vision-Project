# S5

Data Overview


MNIST ("Modified National Institute of Standards and Technology") dataset of computer vision. The MNIST database contains 60,000 training images and 10,000 testing images. Half of the training set and half of the test set were taken from NIST's training dataset, while the other half of the training set and the other half of the test set were taken from NIST's testing dataset.This project implements a beginner classification task on MNIST dataset with a Convolutional Neural Network(CNN) model.

![image](https://user-images.githubusercontent.com/70502759/137764343-c1134fa1-94d2-40b0-bf21-dcd78b3ed4e1.png)
  
  This project will automatically dowload and process the MNIST dataset
  
  Design the model architecture for MNIST with following constraint :
    
    99.4% validation accuracy
    Less than 10k Parameters
    Less than 15 Epochs


Step 1: 
   
       


     1 - Changes done:

        1 - Get the basic setup

        2 - Set Transforms

             Model Summary : 
       
        Layer (type)               Output Shape         Param #

            Conv2d-1           [-1, 16, 26, 26]             144
              ReLU-2           [-1, 16, 26, 26]               0
            Conv2d-3           [-1, 32, 24, 24]           4,608
              ReLU-4           [-1, 32, 24, 24]               0
            Conv2d-5           [-1, 64, 22, 22]          18,432
              ReLU-6           [-1, 64, 22, 22]               0
         MaxPool2d-7           [-1, 64, 11, 11]               0
            Conv2d-8           [-1, 16, 11, 11]           1,024
              ReLU-9           [-1, 16, 11, 11]               0
           Conv2d-10             [-1, 64, 9, 9]           9,216
             ReLU-11             [-1, 64, 9, 9]               0
           Conv2d-12             [-1, 64, 7, 7]          36,864
             ReLU-13             [-1, 64, 7, 7]               0
           Conv2d-14             [-1, 10, 7, 7]             640
             ReLU-15             [-1, 10, 7, 7]               0
           Conv2d-16             [-1, 10, 1, 1]           4,900
 
     Total params: 75,828
     Trainable params: 75,828
     Non-trainable params: 0
     Input size (MB): 0.00
     Forward/backward pass size (MB): 1.14
     Params size (MB): 0.29
     Estimated Total Size (MB): 1.43

     2 - Set Data Loader

     3 - Set Basic Working Code

     4 - Set Basic Training & Test Loop

     5 - Results:

         1 - Parameters: 75,828
         2 - Best Training Accuracy: 99.16
         3 - Best Test Accuracy: 98.72

     6 - Inference:

         1 - Model Parameters is more and it's a heavy model . 
         2 - Model is over-fitting , we will make our model lighter in next step


Step 2 : 
    

    1 - Changes done:

         1 - Added Batch-norm to increase model efficiency and make learning easier.
             There is overfitting, hence added Regularization with the help of  Dropout , which interns help us in reducing overfitting

           Model Summary : 
    
        Layer (type)               Output Shape         Param #

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
           Conv2d-16              [-1, 8, 7, 7]           1,152
      BatchNorm2d-17              [-1, 8, 7, 7]              16
          Dropout-18              [-1, 8, 7, 7]               0
             ReLU-19              [-1, 8, 7, 7]               0
           Conv2d-20             [-1, 10, 5, 5]             720
      BatchNorm2d-21             [-1, 10, 5, 5]              20
          Dropout-22             [-1, 10, 5, 5]               0
             ReLU-23             [-1, 10, 5, 5]               0
           Conv2d-24             [-1, 10, 1, 1]           2,500

    Total params: 6,864
    Trainable params: 6,864
    Non-trainable params: 0
    Input size (MB): 0.00
    Forward/backward pass size (MB): 0.41
    Params size (MB): 0.03
    Estimated Total Size (MB): 0.44


    2 - Results:

         1 - Parameters: 6,864
         2 - Best Training Accuracy: 99.02
         3 - Best Test Accuracy: 99.28

    3 - Inference:

             1 - We could see batch-norm help us in enhancing the model efficiency 
             2 - We could see dropout helps us in reducing overfitting . 
                 We could see the model perform slightly better on test data .
             3 - If we push this model further there is a high chance we can achieve the target of 99.4
             4 - We are also not using GAP, but depending on a BIG sized kernel at the last layer we will fix this in next step .


Step 3 : 


     1 - Changes done:

         1 - Added GAP and remove the last gig size kernel And then Increase model capacity by adding more layers at the end.

      Model Summary : 


        Layer (type)               Output Shape         Param #

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

     Total params: 8,008
     Trainable params: 8,008
     Non-trainable params: 0

     Input size (MB): 0.00
     Forward/backward pass size (MB): 0.47
     Params size (MB): 0.03
     Estimated Total Size (MB): 0.50

     2 - Changes done:

         1 - Parameters: 8008

         2 - Best Training Accuracy: 99.40 (At EPOCH -14)

         3 - Best Test Accuracy: 99.37 (At EPOCH -14)

     3 - Inference:

         1 - Adding Global Average Pooling reduces model parameters i.e interns
             reduced model capacity , hence a reduction in performance is expected.
             Then we have decided to further increase the model capacity .
         2 - Value of drop out (.10) did not allow training accuracy beyond 
             98.80 - 99.01. Hence we have decided to keep very low values of 
             dropout(.007) which help us increase the training accuracy .
        3 - The model did not showing over-fitting possibly DropOut can be 
            ignore , rather removing it completely we have decided to keep it 
            with very less dropout percentage

           

Step 4 :
   
    1 - Changes done: 
     
        1 - Image augmentation can help us generate more data set , hence we have
         added rotation to the image
        2 - Try LR Scheduler to Achive High Accuracy

             Model Summary : 

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
           Conv2d-14             [-1, 13, 9, 9]             936
      BatchNorm2d-15             [-1, 13, 9, 9]              26
          Dropout-16             [-1, 13, 9, 9]               0
             ReLU-17             [-1, 13, 9, 9]               0
           Conv2d-18             [-1, 14, 7, 7]           1,638
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

    Total params: 7,852
    Trainable params: 7,852
    Non-trainable params: 0

    Input size (MB): 0.00
    Forward/backward pass size (MB): 0.55
    Params size (MB): 0.03
    Estimated Total Size (MB): 0.59
   

    2 - Results:

        1 - Parameters: 8k
        2 - Best Train Accuracy: 99.32 (At EPOCH - 14 , StepLR step_size=2, gamma=0.6)
        3 - Best Test Accuracy: 99.46  (At EPOCH - 11 , StepLR step_size=2, gamma=0.6)

    3 - Inference: 
     
     1- The model is under-fitting now. This is fine, as we know we have made
        our train data harder by adding image augmentation
     
     2 - The test accuracy is also up, which means our test data had few images
         which had transformation difference w.r.t. train dataset . 
     
     3 - The test  accuracy is not consistent across the different nearby epoch.
         This we have fix by tweaking the value of learning rate .
     
     4-  Finding a good LR schedule is hard.
         Initially we tried with learning rate 0. 01 . Above Learning rate with
         Scheduler help us to achieve the highest train accuracy of 99.10 and
         test accuracy of 99.39. As training accuracy is less if we can somehow
         increase this accuracy then overall model accuracy on test data can 
         also be increased .Hence we have started exploring with learning rate
         0. 1 . We have tried to make it effective by  reducing LR by 0.6 after
         the 2th  epoch.  Above Learning rate with Scheduler help us to achieve
         the highest test  accuracy of 99.46.
 
     5- The model shows consistant 99.4% accuracy for last few epochs


  

## Tech Stack

Client: Python, Pytorch, Numpy

  
