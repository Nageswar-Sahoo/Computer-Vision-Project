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
   
       

     1 - Target:

        1 - Get the basic setup

        2 - Set Transforms

     2 - Set Data Loader

     3 - Set Basic Working Code

     4 - Set Basic Training & Test Loop

     5 - Results:

         1 - Parameters: 75,828
         2 - Best Training Accuracy: 99.16
         3 - Best Test Accuracy: 98.72
     6 - Analysis:

         1 - Model Parameters is more and it's a heavy model . 
         2 - Model is over-fitting , we will make our model lighter in next step


Step 2 : 

    1- Target:

      1 - Get the basic skeleton right And Reduce the model paramter so that it will help us make lighter model

    2 - Results:

        1 - Parameters: 6,748
        2 - Best Training Accuracy: 99.05
        3 - Best Test Accuracy: 98.81
    3 - Analysis:

        1 - Model is able to achieve 99 with less number of parameters , so quite a good- model 
        2 - Model is slightly over-fitting , model is capable if pushed further         

Step 3 :


     1 - Target:

         1 - Add Batch-norm to increase model efficiency and making learning easier.

     2 - Results:

         1 - Parameters: 6,864
         2 - Best Training Accuracy: 99.48
         3 - Best Test Accuracy: 99.15
     3 - Analysis:

          1 - We could see batch-norm help us in enhancing the model efficiency 
          2 - Model is over-fitting 
          3 - If we push this model further there is a high chance we can achive the 
              target of 99.4 , but before that we can try to fix over-fitting in next step

Step 4 : 

    1 - Target:

         1 - Add Regularization with the help of Dropout , which interns help us in reducing overfitting

    2 - Results:

         1 - Parameters: 6,864
         2 - Best Training Accuracy: 99.02
         3 - Best Test Accuracy: 99.28
    3 - Analysis:

         1 - We could see Regularization helps us in reducing overfitting . 
             We could see the model perform slightly better on test data .
         2 - If we push this model further there is a high chance we can achieve the target of 99.4
         3 - We are also not using GAP, but depending on a BIG sized kernel at the last layer 

Step 5 : 

     1 - Target:

         1 - Add GAP and remove the last BIG size kernel.

     2 - Results:

         1 - Parameters: 4,764
         2 - Best Training Accuracy: 98.39
         3 - Best Test Accuracy: 98.93
     3 - Analysis:

         1 - Adding Global Average Pooling reduces model parameters i.e interns 
             reduced model capacity , hence a reduction in performance is expected.We
             will increase the model capacity further in next step and we will compare
             the result 

Step 6 : 

     1 - Target:

         1 - Increase model capacity. Add more layers at the end And Increase the Number of kernel.

     2 - Results:

         1 - Parameters: 8008

         2 - Best Training Accuracy: 99.40 (At EPOCH -14)

         3 - Best Test Accuracy: 99.37 (At EPOCH -14)
     3 - Analysis:

         1 - if the model is pushed further, test accuracy might increase further
         2 - Value of drop out (.10) did not allow training accuracy beyond 
             98.80 - 99.01. Hence we have decided to keep very low values of 
             dropout(.007) which help us increase the training accuracy .
         3 - The model did not showing over-fitting possibly DropOut can be 
             ignore , rather removing it completely we have decided to keep it 
             with very less dropout percentage

Step 7 :

     1 - Target:

         1 - IMAGE AUGMENTATION can help us generate more data set , hence we have
             added rotation to the image 

     2 - Results:

         1 - Parameters: 10k

         2 - Best Training Accuracy: 99.12 (At EPOCH -12)

         3 - Best Test Accuracy: 99.42 (At EPOCH -13)
     3 - Analysis:

         1 - if the model is pushed further, test accuracy might increase further
         2- The model is under-fitting now. This is fine, as we know we have made
            our train data harder by adding image augmentation
         3 - The test accuracy is also up, which means our test data had few images
             which had transformation difference w.r.t. train dataset . 
         4 - The test  accuracy is not consistent across the different nearby epoch.
             This we can try to fix by tweaking the value of learning rate in the next
             step.             

Step 8 :

   
     1 - Target: 
     
        1 - Try LR Scheduler to Achive High Accuracy

     2 - Results:

         1 - Parameters: 10k
         1 - Best Train Accuracy: 99.44 (At EPOCH - 12 , StepLR step_size=2, gamma=0.6)
         1 - Best Test Accuracy: 99.53  (At EPOCH - 12 , StepLR step_size=2, gamma=0.6)
     
     3 - Analysis:

         1 - Finding a good LR schedule is hard.
             Initially we tried with learning rate 0. 01 . Above Learning rate with
             Scheduler help us to achieve the highest train accuracy of 99.10 and test 
             accuracy of 99.39. As training accuracy is less if we can somehow increase
             this accuracy then overall model accuracy on test data can also be
             increased .Hence we have started exploring with learning rate 0. 1 . We 
             have tried to make it effective by  reducing LR by 0.6 after the 2th  
             epoch.  Above Learning rate with Scheduler help us to achieve the highest
             test  accuracy of 99.53.    

Step 9 : 

     
    1 - Target: Make Lighter Model 1
    
        1 - Achive High Accuracy with less then 8K Parameters

    2 - Results:

         1 - Parameters: 8k
         1 - Best Train Accuracy: 99.32 (At EPOCH - 14 , StepLR step_size=2, gamma=0.6)
         1 - Best Test Accuracy: 99.46  (At EPOCH - 11 , StepLR step_size=2, gamma=0.6)

    3 - Analysis:

        1 - We are able to achieve a high accuracy of 99.46 in the test dataset but
        this is slightly lesser than the high accuracy we achieve of 99.53 with
        param 10k . This is expected due to reduced model capacity .

Step 10 :

    1 - Target: 
    
        1 - Achive High Accuracy with less then 5K Parameters

    2 - Results:

        1 - Parameters: 5k
        1 - Best Train Accuracy: 99.16 (At EPOCH - 12 , StepLR step_size=2, gamma=0.5)
        1 - Best Test Accuracy: 99.41  (At EPOCH - 12 , StepLR step_size=2, gamma=0.5)

    3 - Analysis:

        1 - We are able to achieve a high accuracy of 99.41 in the test dataset but
        this is slightly lesser than the high accuracy we achieve of 99.53 with
        param 10k . This is expected due to reduced model capacity .


Model Summary And Traing Test Logs :  


   With 5k Param :

     
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
           Conv2d-14             [-1, 10, 9, 9]             720
      BatchNorm2d-15             [-1, 10, 9, 9]              20
          Dropout-16             [-1, 10, 9, 9]               0
             ReLU-17             [-1, 10, 9, 9]               0
           Conv2d-18             [-1, 12, 7, 7]           1,080
      BatchNorm2d-19             [-1, 12, 7, 7]              24
          Dropout-20             [-1, 12, 7, 7]               0
             ReLU-21             [-1, 12, 7, 7]               0
           Conv2d-22              [-1, 8, 7, 7]              96
      BatchNorm2d-23              [-1, 8, 7, 7]              16
          Dropout-24              [-1, 8, 7, 7]               0
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 16, 5, 5]           1,152
      BatchNorm2d-27             [-1, 16, 5, 5]              32
          Dropout-28             [-1, 16, 5, 5]               0
             ReLU-29             [-1, 16, 5, 5]               0
           Conv2d-30             [-1, 32, 5, 5]             512
      BatchNorm2d-31             [-1, 32, 5, 5]              64
          Dropout-32             [-1, 32, 5, 5]               0
             ReLU-33             [-1, 32, 5, 5]               0
        AvgPool2d-34             [-1, 32, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             320
     
     Total params: 5,308
     Trainable params: 5,308
     Non-trainable params: 0
     Input size (MB): 0.00
     Forward/backward pass size (MB): 0.52
     Params size (MB): 0.02
     Estimated Total Size (MB): 0.55


    EPOCH: 0
 
      Loss=0.0519770123064518 Batch_id=468 Accuracy=92.05: 100%|██████████| 469/469 [00:21<00:00, 21.78it/s]

      Test set: Average loss: 0.0537, Accuracy: 9831/10000 (98.31%)

    EPOCH: 1

      Loss=0.014366374351084232 Batch_id=468 Accuracy=97.74: 100%|██████████| 469/469 [00:21<00:00, 21.67it/s]

      Test set: Average loss: 0.0471, Accuracy: 9845/10000 (98.45%)

    EPOCH: 2

      Loss=0.05963161215186119 Batch_id=468 Accuracy=98.54: 100%|██████████| 469/469 [00:21<00:00, 21.75it/s]

      Test set: Average loss: 0.0272, Accuracy: 9918/10000 (99.18%)

    EPOCH: 3

     Loss=0.06378480046987534 Batch_id=468 Accuracy=98.65: 100%|██████████| 469/469 [00:21<00:00, 21.63it/s]

     Test set: Average loss: 0.0300, Accuracy: 9908/10000 (99.08%)

    EPOCH: 4

     Loss=0.0970480814576149 Batch_id=468 Accuracy=98.84: 100%|██████████| 469/469 [00:21<00:00, 21.39it/s]

     Test set: Average loss: 0.0227, Accuracy: 9925/10000 (99.25%)

    EPOCH: 5

     Loss=0.06696075946092606 Batch_id=468 Accuracy=98.85: 100%|██████████| 469/469 [00:22<00:00, 21.27it/s]

     Test set: Average loss: 0.0212, Accuracy: 9936/10000 (99.36%)

    EPOCH: 6

     Loss=0.015708083286881447 Batch_id=468 Accuracy=98.97: 100%|██████████| 469/469 [00:22<00:00, 21.11it/s]

     Test set: Average loss: 0.0203, Accuracy: 9934/10000 (99.34%)

    EPOCH: 7

     Loss=0.008445821702480316 Batch_id=468 Accuracy=99.00: 100%|██████████| 469/469 [00:21<00:00, 21.82it/s]

    Test set: Average loss: 0.0201, Accuracy: 9938/10000 (99.38%)

    EPOCH: 8

     Loss=0.01822311244904995 Batch_id=468 Accuracy=99.05: 100%|██████████| 469/469 [00:21<00:00, 21.79it/s]

     Test set: Average loss: 0.0198, Accuracy: 9938/10000 (99.38%)

    EPOCH: 9

     Loss=0.006252346094697714 Batch_id=468 Accuracy=99.01: 100%|██████████| 469/469 [00:21<00:00, 21.70it/s]

     Test set: Average loss: 0.0198, Accuracy: 9938/10000 (99.38%)

    EPOCH: 10

     Loss=0.0035867823753505945 Batch_id=468 Accuracy=99.11: 100%|██████████| 469/469 [00:21<00:00, 21.43it/s]

     Test set: Average loss: 0.0193, Accuracy: 9936/10000 (99.36%)

    EPOCH: 11

     Loss=0.038432370871305466 Batch_id=468 Accuracy=99.11: 100%|██████████| 469/469 [00:22<00:00, 21.12it/s]

     Test set: Average loss: 0.0194, Accuracy: 9941/10000 (99.41%)

-   EPOCH: 12

     Loss=0.023406578227877617 Batch_id=468 Accuracy=99.16: 100%|██████████| 469/469 [00:21<00:00, 21.47it/s]

     Test set: Average loss: 0.0193, Accuracy: 9941/10000 (99.41%)

    EPOCH: 13

     Loss=0.02461189590394497 Batch_id=468 Accuracy=99.15: 100%|██████████| 469/469 [00:22<00:00, 21.24it/s]

     Test set: Average loss: 0.0192, Accuracy: 9938/10000 (99.38%)

    EPOCH: 14

     Loss=0.07370241731405258 Batch_id=468 Accuracy=99.16: 100%|██████████| 469/469 [00:22<00:00, 20.91it/s]

     Test set: Average loss: 0.0192, Accuracy: 9940/10000 (99.40%)


                               
  2 With 10k Param :
     
     
        
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
           Conv2d-14             [-1, 16, 9, 9]           1,152
      BatchNorm2d-15             [-1, 16, 9, 9]              32
          Dropout-16             [-1, 16, 9, 9]               0
             ReLU-17             [-1, 16, 9, 9]               0
           Conv2d-18             [-1, 16, 7, 7]           2,304
      BatchNorm2d-19             [-1, 16, 7, 7]              32
          Dropout-20             [-1, 16, 7, 7]               0
             ReLU-21             [-1, 16, 7, 7]               0
           Conv2d-22              [-1, 8, 7, 7]             128
      BatchNorm2d-23              [-1, 8, 7, 7]              16
          Dropout-24              [-1, 8, 7, 7]               0
             ReLU-25              [-1, 8, 7, 7]               0
           Conv2d-26             [-1, 32, 5, 5]           2,304
      BatchNorm2d-27             [-1, 32, 5, 5]              64
          Dropout-28             [-1, 32, 5, 5]               0
             ReLU-29             [-1, 32, 5, 5]               0
           Conv2d-30             [-1, 64, 5, 5]           2,048
      BatchNorm2d-31             [-1, 64, 5, 5]             128
          Dropout-32             [-1, 64, 5, 5]               0
             ReLU-33             [-1, 64, 5, 5]               0
        AvgPool2d-34             [-1, 64, 1, 1]               0
           Conv2d-35             [-1, 10, 1, 1]             640

     Total params: 10,120
     Trainable params: 10,120
     Non-trainable params: 0
     Input size (MB): 0.00
     Forward/backward pass size (MB): 0.58
     Params size (MB): 0.04
     Estimated Total Size (MB): 0.62

       
          EPOCH: 0

           Loss=0.07584894448518753 Batch_id=468 Accuracy=93.28: 100%|██████████| 469/469 [00:22<00:00, 20.74it/s]

           Test set: Average loss: 0.0614, Accuracy: 9807/10000 (98.07%)

          EPOCH: 1

          Loss=0.05673813819885254 Batch_id=468 Accuracy=98.08: 100%|██████████| 469/469 [00:22<00:00, 20.82it/s]

          Test set: Average loss: 0.0361, Accuracy: 9881/10000 (98.81%)

          EPOCH: 2
           Loss=0.07445203512907028 Batch_id=468 Accuracy=98.70: 100%|██████████| 469/469 [00:22<00:00, 20.52it/s]

           Test set: Average loss: 0.0256, Accuracy: 9921/10000 (99.21%)
 
          EPOCH: 3

           Loss=0.0026412748266011477 Batch_id=468 Accuracy=98.89: 100%|██████████| 469/469 [00:22<00:00, 20.70it/s]

           Test set: Average loss: 0.0294, Accuracy: 9907/10000 (99.07%)

          EPOCH: 4

           Loss=0.00681330868974328 Batch_id=468 Accuracy=99.02: 100%|██████████| 469/469 [00:22<00:00, 20.61it/s]

           Test set: Average loss: 0.0227, Accuracy: 9930/10000 (99.30%)

          EPOCH: 5

           Loss=0.020798491314053535 Batch_id=468 Accuracy=99.13: 100%|██████████| 469/469 [00:22<00:00, 20.84it/s]

           Test set: Average loss: 0.0231, Accuracy: 9924/10000 (99.24%)

          EPOCH: 6

            Loss=0.005443560425192118 Batch_id=468 Accuracy=99.25: 100%|██████████| 469/469 [00:22<00:00, 20.46it/s]

            Test set: Average loss: 0.0188, Accuracy: 9941/10000 (99.41%)

          EPOCH: 7

           Loss=0.006054149940609932 Batch_id=468 Accuracy=99.27: 100%|██████████| 469/469 [00:22<00:00, 20.87it/s]

           Test set: Average loss: 0.0175, Accuracy: 9946/10000 (99.46%)

          EPOCH: 8

           Loss=0.022747160866856575 Batch_id=468 Accuracy=99.31: 100%|██████████| 469/469 [00:22<00:00, 20.64it/s]

           Test set: Average loss: 0.0180, Accuracy: 9945/10000 (99.45%)

          EPOCH: 9

           Loss=0.010960395447909832 Batch_id=468 Accuracy=99.34: 100%|██████████| 469/469 [00:22<00:00, 20.76it/s]

           Test set: Average loss: 0.0171, Accuracy: 9947/10000 (99.47%)

          EPOCH: 10

            Loss=0.04422583803534508 Batch_id=468 Accuracy=99.36: 100%|██████████| 469/469 [00:22<00:00, 20.76it/s]

            Test set: Average loss: 0.0170, Accuracy: 9943/10000 (99.43%)

          EPOCH: 11

            Loss=0.0024763590190559626 Batch_id=468 Accuracy=99.36: 100%|██████████| 469/469 [00:22<00:00, 20.83it/s]

            Test set: Average loss: 0.0157, Accuracy: 9951/10000 (99.51%)

          EPOCH: 12

           Loss=0.0008387898560613394 Batch_id=468 Accuracy=99.44: 100%|██████████| 469/469 [00:22<00:00, 20.70it/s]

            Test set: Average loss: 0.0163, Accuracy: 9953/10000 (99.53%)

          EPOCH: 13
            
           Loss=0.0013749400386586785 Batch_id=468 Accuracy=99.42: 100%|██████████| 469/469 [00:22<00:00, 20.66it/s]

           Test set: Average loss: 0.0164, Accuracy: 9951/10000 (99.51%)

          EPOCH: 14

           Loss=0.009129290468990803 Batch_id=468 Accuracy=99.44: 100%|██████████| 469/469 [00:22<00:00, 20.70it/s]

           Test set: Average loss: 0.0159, Accuracy: 9951/10000 (99.51%)



      
       
         



## Tech Stack

Client: Python, Pytorch, Numpy

  
