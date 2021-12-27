Assignment 12

VIT Architecture 

![image](https://user-images.githubusercontent.com/70502759/147465620-b23a7883-5c01-4dfe-80e0-4104d5898a73.png)


Block
------

Embeddings
----------

Below are the task performed in Embeddings layer .

1 - Split an image into patches 

2 - Flatten the patches

3 - Produce lower-dimensional linear embeddings from the flattened patches

4 - Add positional embeddings

5 - Add the cls token which can be used for classification task 




Attention
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


Encoder
-------
Encoder layer consist of stack of Attention , Feed Forward  and Normalizaion layer .  

Below are the task performed in Encoder layer .

1 - Attention layer output value vectors are concatenated and added to the 
    residual connection coming from the input layer  
    
2 - Then the resultant respresentation is passed into a LayerNorm for normalization. 

3 - Further, the output is passed into a point-wise feed forward network to obtain an even richer representation.

MLP
----

Output from the encoder is passed directly into a Feed Forward Neural Network to obtain the classification output.







