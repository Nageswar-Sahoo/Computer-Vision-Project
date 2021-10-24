
# Design Below Neural Network Architecture

   take 2 inputs:
 
     an image from the MNIST dataset (say 5), and
     a random number between 0 and 9, (say 7)
   
   and gives two outputs:
 
    the "number" that was represented by the MNIST image (predict 5), and
    the "sum" of this number with the random number and the input image to the network (predict 5 + 7 = 12)

![image](https://user-images.githubusercontent.com/70502759/136892002-fa6fad37-bab3-4f82-8a48-ef43557526b8.png)


 Input Data

  MNIST Image
   


  ![image](https://user-images.githubusercontent.com/70502759/136895005-4cb01984-b509-43cc-935b-7722036b413b.png)
  
  
  Random Number
  
  We have generate the random number dynamically with the help of following function by giving the batchsize 
     
      def getRandomNumber(batchsize):
         return random.sample(range(0, 10), batchsize)
      
         
      getRandomNumber(10)   
   
      [9, 0, 3, 7, 8, 5, 4, 1, 2, 6]
      
     

    
      
We have input image of shape (1,28,28), where 28*28 is height and  weidht of the image and  we have only one channel as it's a gray image 
We have a single random number which we have to add with the MNIST image number and will try to predicate the respective sum . 


Random Number converted to the one hot vector which can be used as an input to the neural network .

       [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

 


As we can predicate the maximum sum as 18 so including zero we have a total 19 class of prediction for the sum and 10 class of prediction for mnist number and total class is 29. We have prepared the actual labels that can be used for loss calculation after the model predicted handwritten mnist number and sum.


      
    Actual Mnist Number 
      [9, 0, 0, 3, 0, 2, 7, 2, 5, 5]       
    Random Number
      [9, 0, 3, 7, 8, 5, 4, 1, 2, 6]

    One Hot Represenatation 
       [[0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.]])


Model Summery
   
         Layer (type)               Output Shape         Param #
          
            Conv2d-1            [-1, 6, 24, 24]             156         
            Conv2d-2             [-1, 12, 8, 8]           1,812
            Linear-3                   [-1, 20]             220
            Linear-4                   [-1, 40]             840
            Linear-5                  [-1, 120]          27,960
            Linear-6                   [-1, 60]           7,260
            Linear-7                   [-1, 29]           1,769

    Total params: 40,017
    Trainable params: 40,017
    Non-trainable params: 0
    Input size (MB): 0.03
    Forward/backward pass size (MB): 0.03
    Params size (MB): 0.15
    Estimated Total Size (MB): 0.22


Combined The Two Inputs

 Initially we have passed through 2 conv layers  (Conv2d-1  [-1, 6, 24, 24] , Conv2d-2  [-1, 12, 8, 8]) and we have extracted the feature map. We have flatted the feature map into one dimension vector of shape(1,192) . 
 Random number we have passed through two Linear neural layer and concatenated both the outputs which resulted in (1,232) one dimension vector . Again this passed through two linear layer and give the output of (1,29) shapes where the initial 10 digit refer to the mnist prediction and last 19 digit refer to the sum with the random number .  



Loss function

 Since this is a classification problem, the choice of loss function may seem obvious – the CrossEntropy loss with sigmoid or softmax . 
 Softmax makes all predicted probabilities sum to 1, so there couldn’t be several correct answers. In our case we need to have 2 class as prediction .The obvious solution here is to treat each prediction independently. 
 For example, using the Sigmoid function as a normalizer for each logit value separately.  Now we can compare these probabilities with the probabilities of the correct labels (ones) using BCEWithLogitsLoss loss.

Evaluation

Actual Random Number


    [8, 9, 3, 7, 0, 2, 5, 1, 4, 6]

Actual Mnist Number

    [0, 3, 5, 6, 3, 2, 5, 3, 9, 0]

Actual Random Number Sum 


    [ 8, 12,  8, 13,  3,  4, 10,  4, 13,  6]

One Hot Represenatation (Initial 10 digit refer to mnist and Next 19 digit refer to SUM)

        [[1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]

Model Prediction 

 We have 29 class of prediction and we have divided initial 10 index as Mnist 
 prediction and remaining 19 index as Random Number SUM prediction





Mnist Number Prediction 


       [[ 2.6619e+00, -1.0955e+01, -1.1669e+01, -6.3555e+00, -2.2778e+01,
         -4.9235e+01, -1.8543e+00, -9.0359e+01, -5.7980e+00, -5.1865e+01],
        [-4.2893e+00, -3.7112e+00, -2.0963e+00, -1.9110e+00,  2.3672e-01,
         -4.5074e+01, -1.4926e+00, -1.0237e+02, -1.0838e+01, -2.8298e+01],
        [-1.1949e+01, -2.3675e+01, -8.0549e+00, -1.4621e+01, -8.8483e+00,
          3.9560e+00, -9.6652e+00, -4.8440e+00, -5.4975e+00, -5.2019e+00],
        [-3.8916e+00, -6.4306e+00, -3.4264e-01, -4.7761e+00, -2.2905e+00,
         -1.4932e+01, -8.4622e-01, -3.2392e+01, -3.6940e+00, -1.2415e+01],
        [-7.0409e+00, -6.6023e+00, -1.3333e+01,  7.4085e+00, -6.4891e+00,
         -5.1976e+01, -6.9799e+00, -9.5384e+01, -1.6424e+01, -3.6665e+01],
        [-6.9478e+00, -7.1413e+00,  1.5742e+00, -4.0699e+00, -3.7342e+00,
         -4.6974e+01, -1.8004e+00, -9.0904e+01, -6.3342e+00, -5.3803e+01],
        [-1.7879e+01, -3.5392e+01, -1.2449e+01, -2.1921e+01, -1.3376e+01,
          6.1423e+00, -1.5756e+01, -7.1341e+00, -7.9966e+00, -6.8372e+00],
        [-1.4742e+00, -4.4122e-02, -3.8370e+00, -1.6621e+00, -3.9458e+00,
         -7.9166e-01, -4.8277e-01, -4.1011e+00, -1.7170e-01, -4.5948e+00],
        [-2.9712e+01, -1.6006e+01, -6.1942e+01, -1.9138e+01, -4.9803e+01,
         -6.0047e+00, -6.6920e+01, -4.4795e+00, -2.2539e+01,  5.2897e+00],
        [-7.1052e-01, -3.4157e+00, -3.2627e+00, -1.6148e+00, -4.3689e+00,
         -1.0538e+01, -5.0837e-01, -1.6286e+01, -3.3428e+00, -7.6199e+00]]

Random Number Sum Prediction


         [[-5.0966e+01, -5.5155e+01, -4.4233e+01, -1.9949e+01, -1.8520e+01,
         -2.8645e+01, -7.8273e+00, -2.0659e+01,  3.0945e+00, -7.2129e+00,
         -1.5306e+01, -7.6581e+00, -1.3886e+01, -6.0037e+01, -3.1306e+00,
         -2.8740e+01, -4.4290e+01, -4.9727e+01, -2.4900e+02],
        [-6.0808e+01, -6.3199e+01, -4.2120e+01, -5.6907e+01, -4.3610e+01,
         -6.4269e+01, -8.4136e+01, -5.0726e+01, -6.3304e+00, -5.1662e+00,
         -3.0050e+00, -2.2863e+00, -7.9924e-01,  5.6390e-01, -2.3346e+00,
         -2.9186e+00, -2.3525e+01, -1.3908e+01, -5.2580e+01],
        [-8.8028e+01, -8.7574e+01, -7.2907e+01, -2.0590e+01, -1.5528e+01,
         -4.7560e+00, -5.1957e+00, -4.6779e+00, -1.8473e+00, -1.6529e+00,
         -9.5720e-01, -1.5476e+00, -1.6133e+00, -4.3834e+00, -4.0497e+00,
         -6.9568e+00, -1.2207e+01, -3.7186e+01, -1.0004e+02],
        [-2.4761e+01, -2.5514e+01, -2.0323e+01, -5.8872e+00, -5.2390e+00,
         -2.3199e+00, -2.3207e+00, -1.4569e+00, -2.0304e+00, -1.6169e+00,
         -1.7255e+00, -2.3392e+00, -2.6223e+00, -2.7872e+00, -4.1242e+00,
         -4.8438e+00, -1.0857e+01, -1.6771e+01, -6.1034e+01],
        [-1.4717e+01, -1.1919e+01, -1.5721e+01,  5.5630e+00, -4.4568e+00,
         -1.6255e+01, -3.0208e+00, -3.2966e+01, -1.5798e+01, -2.8107e+01,
         -4.1716e+01, -1.3430e+02, -1.7800e+02, -3.2299e+02, -2.0399e+02,
         -2.9007e+02, -2.3200e+02, -2.6939e+02, -2.2402e+02],
        [-1.6160e+02, -4.5466e+01, -6.2648e+00, -3.7370e+00,  1.8741e+00,
         -1.2989e+00, -1.7901e+00, -1.6505e+01, -2.7826e-01, -4.0853e+01,
         -6.9233e+00, -2.6779e+01, -4.5319e+01, -1.2879e+02, -7.5490e+01,
         -1.3078e+02, -1.4754e+02, -2.0444e+02, -1.7858e+02],
        [-1.3256e+02, -1.3181e+02, -1.0986e+02, -3.0301e+01, -2.2709e+01,
         -6.4356e+00, -7.1140e+00, -6.5835e+00, -1.9738e+00, -1.8069e+00,
         -5.2964e-01, -1.4508e+00, -1.5834e+00, -5.9613e+00, -5.3789e+00,
         -9.7232e+00, -1.7564e+01, -5.5096e+01, -1.4977e+02],
        [-6.3858e+00, -2.4639e+00, -2.3164e+00, -6.0894e+00, -4.8257e+00,
         -5.1885e+00, -1.9538e+00, -3.4950e+00, -2.2830e+00, -1.3030e-04,
         -2.3613e+00, -5.3820e+00, -3.4965e+00, -7.7021e+00, -9.6109e-01,
         -3.1820e+00, -3.7592e+00, -3.1402e+00, -1.9100e+01],
        [-9.4846e+01, -2.1095e+01, -2.4798e+01, -1.5668e+01, -2.0803e+01,
         -2.1490e+01, -1.5075e+01, -2.0116e+01, -6.2027e+00, -1.0117e+01,
         -3.5179e+00, -3.5934e+00, -1.9318e+00, -1.0007e+00, -1.3061e+00,
         -1.4330e+00, -2.0433e+00, -1.3113e+01, -5.8124e+00],
        [-7.8502e+00, -4.5586e+00, -4.1296e+00, -2.4482e+00, -2.1486e+00,
         -2.2549e+00, -1.8622e+00, -1.5182e+00, -2.7050e+00, -1.9312e+00,
         -2.1277e+00, -2.3132e+00, -2.4099e+00, -2.1950e+00, -3.1513e+00,
         -4.1621e+00, -1.3014e+01, -9.1615e+00, -2.7350e+01]]
 
 
In the prediction we will use the maximum number index as a prediction label .
We have used ARGMAX to get the required predicted labels .


Mnist Predicted labels 


      [0, 4, 5, 2, 3, 2, 5, 1, 9, 6]

Random Number Sum Predicted Labels 


      [ 8, 13, 10,  7,  3,  4, 10,  9, 13,  7]

We can see the model did correct prediction for 6 Mnist Number and 5 correct prediction for random number sum .


## Tech Stack

**Client:** Python, Pytorch, Numpy


  
