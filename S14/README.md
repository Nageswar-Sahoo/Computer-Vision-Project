Assignment 14 
-------------

DETR
-----
DETR is short for DEtection TRansformer, and consists of a convolutional backbone  followed by an encoder-decoder Transformer. It can be trained end-to-end to perform object detection .The main contribution of DETR is its simplicity: compared to other models like Faster R-CNN and Mask R-CNN, which rely on several highly engineered things like region proposals, non-maximum suppression procedure and anchor generation, DETR is a model that can simply be trained end-to-end, and fine-tuned just like you would fine-tune BERT. This is possible due to the use of a clever loss function, the so-called bipartite matching loss

![image](https://user-images.githubusercontent.com/70502759/149753302-5591d27d-ba80-437b-9ec2-bb4a73de835f.png)
![image](https://user-images.githubusercontent.com/70502759/149759863-3bc41c8a-1b90-4d66-8d3a-0b70269db818.png)

The architecture of DETR has three main components, which are a CNN backbone to extract a compact feture representation, encoder-decoder transformer, Feed-Forward Netoworks.


Encoder-Decoder Architecture
-----------------------------

![image](https://user-images.githubusercontent.com/70502759/149766446-cf294fbe-c1d1-4491-9315-7b09edf6b160.png)


Here, the CNN backbone generates a feature map from the input image. Then the output of the CNN backbone is converted into a one-dimensional feature map that is passed to the Transformer encoder as input. The output of this encoder are N number of fixed length embeddings (vectors), where N is the number of objects in the image assumed by the model.

The Transformer Decoder – takes in Object queries and  decodes these embeddings into bounding box coordinates with the help of self and encoder-decoder attention mechanism.

Finally, the feed-forward neural networks predict the normalized center coordinates, height, and width of the bounding boxes and the linear layer predicts the class label using a softmax function or a no object class.

Bipartite loss, and why we need it
------------------------------------

Issue with Existing Loss function in Object Detection :

Existing object detection models label bounding boxes by matching multiple bounding boxes to one ground truth box with considering the ordering  . 
We are using NMS for above task and this will increase overlapping bounding boxes in image .The predicted results are a set of N predictions. Comparing this N predictions to the ground truth set is non trivial. To assess the loss an optimal Bipartite matching is created between predicted labels and ground truth. This is done by minimizing matching loss between a tuple’s elements by picking one element from predicted labels and another element from ground truth.Once we have this bipartite mapping we can calculate a loss called Hungarian Loss. Bipartite matching loss is designed based on Hungarian algorithm

![image](https://user-images.githubusercontent.com/70502759/149750992-58d412a5-ca14-4389-a7c4-00be64a0fea5.png)


Oobject queries
---------------

![image](https://user-images.githubusercontent.com/70502759/149766548-c9a26fda-5622-4031-8d15-51a6ee4cb5c3.png)

The figure below depicts how N=20 learned object queries  focus on different areas of an image.
An intuitive way of understanding the object queries is by imagining that each object query is a person. And each person can ask the, via attention, about a certain region of the image. So one object query will always ask about what is in the center of an image, and another will always ask about what is on the bottom left, and so on.


Results on Balloon Dataset :
----------------------------
Threshold 0.9

![image](https://user-images.githubusercontent.com/70502759/149768045-52657799-393f-421d-9e7c-1b098b5d0a5e.png)
![image](https://user-images.githubusercontent.com/70502759/149768174-df228e27-0b41-4ab2-b3cc-25f97b046cb9.png)


Threshold 0.7

![image](https://user-images.githubusercontent.com/70502759/149768150-18268caa-f158-4857-9f4c-405bd7e0cad4.png)
![image](https://user-images.githubusercontent.com/70502759/149768197-17ff6c77-e630-4af0-aa28-99e091709384.png)




DETR training logs : 
--------------------


