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

  


 
