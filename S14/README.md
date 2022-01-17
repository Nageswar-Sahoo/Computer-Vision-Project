Assignment 13  
-------------

DETR
-----
Encoder-Decoder Architecture
-----------------------------
Bipartite loss, and why we need it
------------------------------------

Issue with Existing Loss function in Object Detection :

Existing object detection models label bounding boxes by matching multiple bounding boxes to one ground truth box with considering the ordering  . 
We are using NMS for above task and this will increase overlapping bounding boxes in image .The predicted results are a set of N predictions. Comparing this N predictions to the ground truth set is non trivial. To assess the loss an optimal Bipartite matching is created between predicted labels and ground truth. This is done by minimizing matching loss between a tuple’s elements by picking one element from predicted labels and another element from ground truth.Once we have this bipartite mapping we can calculate a loss called Hungarian Loss. Bipartite matching loss is designed based on Hungarian algorithm

![image](https://user-images.githubusercontent.com/70502759/149750992-58d412a5-ca14-4389-a7c4-00be64a0fea5.png)


Oobject queries
---------------
Results
-----------



