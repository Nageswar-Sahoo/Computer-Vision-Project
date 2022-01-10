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

VIT Training Logs 
-----------------

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 1 - loss : 0.6973 - acc: 0.5088 - val_loss : 0.6917 - val_acc: 0.5190

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 2 - loss : 0.6900 - acc: 0.5294 - val_loss : 0.6864 - val_acc: 0.5461

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 3 - loss : 0.6847 - acc: 0.5507 - val_loss : 0.6755 - val_acc: 0.5799

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 4 - loss : 0.6776 - acc: 0.5696 - val_loss : 0.6874 - val_acc: 0.5585

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 5 - loss : 0.6738 - acc: 0.5746 - val_loss : 0.6706 - val_acc: 0.5773

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 6 - loss : 0.6665 - acc: 0.5905 - val_loss : 0.6664 - val_acc: 0.5890

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 7 - loss : 0.6597 - acc: 0.5955 - val_loss : 0.6500 - val_acc: 0.6112

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 8 - loss : 0.6480 - acc: 0.6126 - val_loss : 0.6438 - val_acc: 0.6181

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 9 - loss : 0.6396 - acc: 0.6220 - val_loss : 0.6395 - val_acc: 0.6232

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 10 - loss : 0.6315 - acc: 0.6331 - val_loss : 0.6326 - val_acc: 0.6264

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 11 - loss : 0.6223 - acc: 0.6463 - val_loss : 0.6409 - val_acc: 0.6272

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 12 - loss : 0.6159 - acc: 0.6539 - val_loss : 0.6186 - val_acc: 0.6572

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 13 - loss : 0.6112 - acc: 0.6579 - val_loss : 0.6284 - val_acc: 0.6349

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 14 - loss : 0.6085 - acc: 0.6642 - val_loss : 0.6102 - val_acc: 0.6600

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 15 - loss : 0.6021 - acc: 0.6622 - val_loss : 0.6076 - val_acc: 0.6614

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 16 - loss : 0.5943 - acc: 0.6755 - val_loss : 0.6033 - val_acc: 0.6648

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 17 - loss : 0.5952 - acc: 0.6744 - val_loss : 0.5979 - val_acc: 0.6731

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 18 - loss : 0.5905 - acc: 0.6781 - val_loss : 0.5975 - val_acc: 0.6756

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 19 - loss : 0.5901 - acc: 0.6793 - val_loss : 0.5921 - val_acc: 0.6774

  0%|          | 0/313 [00:00<?, ?it/s]
Epoch : 20 - loss : 0.5821 - acc: 0.6876 - val_loss : 0.5919 - val_acc: 0.6695



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







