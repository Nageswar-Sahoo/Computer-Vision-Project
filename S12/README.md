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
 
Here is the result of using a spatial transformer as the first layer of a fully-connected network trained for distorted MNIST digit classification.

![image](https://user-images.githubusercontent.com/70502759/147410552-1cea4f3e-070e-4904-a90f-e4f68418ef42.png)

Notice how it has learned to do exactly what we wanted our theoretical “robust” image classification model to do: by zooming in and eliminating background clutter, it has “standardized” the input to facilitate classification.

Spatial Transformer Architecture
--------------------------------
Three differentiable modules:
 1 - Localisation network.
 
 2 - Parameterised Sampling Grid (Grid Generator).
 
 3 - Differentiable Image Sampling (Sampler).

![image](https://user-images.githubusercontent.com/70502759/147410614-634698fc-6636-45ab-ba6b-cafed7d0212d.png)

Localisation Net
The goal of the localisation network is to spit out the parameters θ of the affine transformation that’ll be applied to the input feature map. The localisation network can take any form, such as a fully-connected network or a convolutional network, but should include a final regression layer to produce the transformation parameters 𝜃:
![image](https://user-images.githubusercontent.com/70502759/147410971-d3777dda-2a47-4d18-901d-95301bffe27e.png)
The size of 𝜃 can vary depending on the transformation that is parameterized, e.g. for an affine transformation 𝜃 is 6-dimensional:
Another way to look at it is that the localisation network learns to store the knowledge of how to transform each training sample in the weights of its layers.








