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
----------------

The goal of the localisation network is to spit out the parameters θ of the transformation that’ll be applied to the input feature map. The localisation network can take any form, such as a fully-connected network or a convolutional network, but should include a final regression layer to produce the transformation parameters 𝜃:

![image](https://user-images.githubusercontent.com/70502759/147410971-d3777dda-2a47-4d18-901d-95301bffe27e.png)

The size of 𝜃 can vary depending on the transformation that is parameterized, e.g. for an affine transformation 𝜃 is 6-dimensional:


Another way to look at it is that the localisation network learns to store the knowledge of how to transform each training sample in the weights of its layers.

Parameterised Sampling Grid (Grid Generator).
---------------------------------------------

The grid generator’s job is to output a parametrised sampling grid, which is a set of points where the input map should be sampled to produce the desired transformed output.

![Affine](https://user-images.githubusercontent.com/70502759/147411246-a9e3d95e-3b07-4324-ac58-168b8fec61b3.PNG)


Differentiable Image Sampling (Sampler).
----------------------------------------

The sampler iterates over the entries of the sampling grid and extracts the corresponding pixel values from the input map using bilinear interpolation.


Both the grid generator and the sampler are parameter less operations, i.e. they don’t have any trainable parameters. In this regard they are comparable to a max-pooling layer. The brainpower of a spatial transformer module hence comes from the localisation net, which must learn to detect the pose of the input feature map (such as its orientation, scale etc.) in order to produce an appropriate transformation.

Visualizing the Spatial Transformations Done by the STN Model
-------------------------------------------------------------

The following image shows the results after the 5 epoch.
--------------------------------------------------------

![image](https://user-images.githubusercontent.com/70502759/147414125-1dcab0cd-5b5c-4f1a-a6e1-1bd02d8181f8.png)


The following image shows the results after the 10 epoch.
---------------------------------------------------------

![image](https://user-images.githubusercontent.com/70502759/147414269-c7e459f3-e0d6-49bd-a56b-0c12ac8a54e2.png)


The following image shows the results after the 20 epoch.
---------------------------------------------------------

![image](https://user-images.githubusercontent.com/70502759/147414441-a36cff58-3174-4e21-a449-c1c0191d407c.png)


The following image shows the results after the 40 epoch.
---------------------------------------------------------
![image](https://user-images.githubusercontent.com/70502759/147414804-54c5d502-a483-4d23-9bc3-d6ef268e6734.png)


The following image shows the results after the 50 epoch.
--------------------------------------------------------
![image](https://user-images.githubusercontent.com/70502759/147415073-6803b9cb-b2f9-4dc2-bae4-6e937670ae76.png)


Spatial Transformer Network model has cropped and resized most of the images to the center.
It has rotated many of the images to an orientation that it feels will be helpful. 
Although some of the orientations are not centered. 
We can see that after each epoch, the neural network is resizing, cropping, and centering the images a bit better.

Google Colab file : 
-------------------

https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/S12/Assignment8.ipynb









