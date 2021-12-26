Assignment 12

Limitations CNN :
----------------
When working on a classification task, it is usually desirable that our system be robust to input variations. By this, we mean to say that should an input undergo a certain “transformation” so to speak, our classification model should in theory spit out the same class label as before that transformation.We have following limitation on CNN

 1 - Limited spatial invariance.
 
 2 - Max pooling has small spatial support.
 
 3 - Only deep layers (towards output) achieve invariance.
 
 4 - No rotation and scaling invariance.

SPATIAL TRANSFORMER NETWORKS 
----------------------------

The Spatial Transformer mechanism addresses the issues above by providing Convolutional Neural Networks with explicit spatial transformation capabilities.

 1 - A dynamic mechanism that actively spatially transforms an image or feature map by learning appropriate transformation matrix.

 2 - Transformation matrix is capable of including translation, rotation, scaling, cropping and non-rigid deformations.

 3 - Allows for end to end trainable models using standard back-propagation.
 
 4 - Here is the result of using a spatial transformer as the first layer of a fully-connected network trained for distorted MNIST digit classification.

![image](https://user-images.githubusercontent.com/70502759/147410552-1cea4f3e-070e-4904-a90f-e4f68418ef42.png)

Notice how it has learned to do exactly what we wanted our theoretical “robust” image classification model to do: by zooming in and eliminating background clutter, it has “standardized” the input to facilitate classification.

Spatial Transformer Architecture
--------------------------------
Three differentiable modules:
 1 - Localisation network.
 
 2 - Parameterised Sampling Grid (Grid Generator).
 
 3 - Differentiable Image Sampling (Sampler).

![image](https://user-images.githubusercontent.com/70502759/147410614-634698fc-6636-45ab-ba6b-cafed7d0212d.png)







