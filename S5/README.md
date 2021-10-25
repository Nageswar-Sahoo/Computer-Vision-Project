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

    1 - Target:

         1 - Add Batch-norm to increase model efficiency and make learning easier.
            if there is overfitting, Add Regularization with the help of  Dropout , which interns help us in reducing overfitting

    2 - Results:

         1 - Parameters: 6,864
         2 - Best Training Accuracy: 99.02
         3 - Best Test Accuracy: 99.28
    3 - Analysis:

             1 - We could see batch-norm help us in enhancing the model efficiency 
             2 - We could see Regularization helps us in reducing overfitting . We could see the model perform slightly better on test data .
             3 - If we push this model further there is a high chance we can achieve the target of 99.4
             4 - We are also not using GAP, but depending on a BIG sized kernel at the last layer we will fix this in next step .


Step 3 : 

     1 - Target:

         1 - Add GAP and remove the last BIG size kernel And then Increase model capacity by Adding more layers at the end.

     2 - Results:

         1 - Parameters: 8008

         2 - Best Training Accuracy: 99.40 (At EPOCH -14)

         3 - Best Test Accuracy: 99.37 (At EPOCH -14)
     3 - Analysis:

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

   
    1 - Target: 
     
        1 - IMAGE AUGMENTATION can help us generate more data set , hence we have
         added rotation to the image
        2 - Try LR Scheduler to Achive High Accuracy

    2 - Results:

        1 - Parameters: 8k
        2 - Best Train Accuracy: 99.32 (At EPOCH - 14 , StepLR step_size=2, gamma=0.6)
        3 - Best Test Accuracy: 99.46  (At EPOCH - 11 , StepLR step_size=2, gamma=0.6)

    3 - Analysis: 
     
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


   
         



## Tech Stack

Client: Python, Pytorch, Numpy

  
