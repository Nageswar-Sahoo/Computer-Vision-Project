Assignment 12

Limitations CNN :
----------------
When working on a classification task, it is usually desirable that our system be robust to input variations. By this, we mean to say that should an input undergo a certain “transformation” so to speak, our classification model should in theory spit out the same class label as before that transformation.We have following limitation on CNN

 Limited spatial invariance.
 Max pooling has small spatial support.
 Only deep layers (towards output) achieve invariance.
 No rotation and scaling invariance.

SPATIAL TRANSFORMER NETWORKS 
----------------------------

Spatial Transformer

 A dynamic mechanism that actively spatially transforms an image or feature map by learning appropriate transformation matrix.

 Transformation matrix is capable of including translation, rotation, scaling, cropping and non-rigid deformations.

 Allows for end to end trainable models using standard back-propagation.

![image](https://user-images.githubusercontent.com/70502759/147410552-1cea4f3e-070e-4904-a90f-e4f68418ef42.png)

Spatial Transformer Architecture
--------------------------------
Three differentiable modules:
 Localisation network.
 Parameterised Sampling Grid (Grid Generator).
 Differentiable Image Sampling (Sampler).

![image](https://user-images.githubusercontent.com/70502759/147410614-634698fc-6636-45ab-ba6b-cafed7d0212d.png)







