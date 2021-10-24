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

         1 - We could see Regularization helps us in reducing overfitting . We could see the model perform slightly better on test data .
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

         1 - Increase model capacity. Add more layers at the end.

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

## Tech Stack

Client: Python, Pytorch, Numpy

  
