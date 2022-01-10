Assignment 13 : Part 1 
-----------------------

In this project, we are exploring transformer algorithm, a deep learning model to classify whether images contain either a dog or a cat.

Cat-Dog-Classifier
------------------

This is a common computer vision project to classifier images whether it is cat or dog. While the output is the accuracy, the main objective of this assignments  is not to get a high accuracy but rather to learn how to use vit transformer 

Total Dataset : 37500 images

Training dataset : 20000 images of cats and  dogs

Validation dataset : 5000 images of cats and  dogs

test dataset : 12500 images of cats and  dogs

Data
----
The dataset is available at Kaggle and we have downloaded for training . 

![catanddog](https://user-images.githubusercontent.com/70502759/148720469-d7a58257-7b55-4623-9755-9d6ad9cf7c7a.PNG)


VIT Architecture 
-----------------

![image](https://user-images.githubusercontent.com/70502759/147465620-b23a7883-5c01-4dfe-80e0-4104d5898a73.png)

Training Logs 
-------------



Embeddings layer performed step 1, 2 3, 4 ,5 of the above architecture image 
----------

Below are the task performed in Embeddings layer .

1 - Split an image into patches 

2 - Flatten the patches

3 - The patches are then unrolled (flattened) and sent for further processing into the network

4 - Add positional embeddings

5 - Add the cls token which can be used for classification task 





Attention layer performed step 6 of the above architecture image  
---------
Below are the task performed in Attention layer .

1 - Attention consists of three learnable vectors. Query, Key and Value vectors. 
    The motivation of this reportedly comes from information retrival 
	where you search (query) and the search engine compares your query with a key and responds with a value.

2 - The Q and K representations undergo a dot product matrix multiplication 
    to produce a score matrix which represents how much a patch image has to attend to every other patch image.
	Higher score means more attention and vice-versa.

3 - Then the Score matrix is scaled down according to the dimensions of the Q and K vectors. 
    This is to ensure more stable gradients as multiplication can have exploding effects.


4 - Next the Score matrix is softmaxed to turn attention scores into probabilities. 
    Obviously higher scores are heightened and lower scores are depressed. 
	This ensures the model to be confident on which patch image to attend to.

5 - Then the resultant matrix with probabilites is multiplied with the value vector.
    This will make the higher probaility scores the model has learned to be more important.
	The low scoring patch image will effectively drown out to become irrelevant.

6 - Then, the concatenated output of QK and V vectors are fed into the Linear layer to process further.


![AttentionProcess](https://user-images.githubusercontent.com/70502759/147462295-541e6fc2-fc4a-48c4-b769-580d5924eb95.PNG)


Encoder layer performed step 6 of the above architecture image
-------
Encoder layer consist of stack of Attention , Feed Forward  and Normalizaion layer .  

Below are the task performed in Encoder layer .

1 - Attention layer output value vectors are concatenated and added to the 
    residual connection coming from the input layer  
    
2 - Then the resultant respresentation is passed into a LayerNorm for normalization. 

3 - Further, the output is passed into a point-wise feed forward network to obtain an even richer representation.

MLP layer performed step 7 of the above architecture image
----

Output from the encoder is passed directly into a Feed Forward Neural Network to obtain the classification output.


Block
------

Inside the block layer we are performing task such as Attention , LayerNorm for normalization and classification with MLP layer 







