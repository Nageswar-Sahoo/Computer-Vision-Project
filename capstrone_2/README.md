


                                                   DETR for Object and Bounding Box Detection
                                                   ------------------------------------------
                                                   
About Model  DETR
-----------------
DETR is short for DEtection TRansformer, and consists of a convolutional backbone  followed by an encoder-decoder Transformer. It can be trained end-to-end to perform object detection .The main contribution of DETR is its simplicity: compared to other models like Faster R-CNN and Mask R-CNN, which rely on several highly engineered things like region proposals, non-maximum suppression procedure and anchor generation. This is possible due to the use of a clever loss function, the so-called bipartite matching loss . 

1443 image splitted into train and test split of 80% to 20% ratio . Hence the train set contain 1146 and 297 number of image .


![image](https://user-images.githubusercontent.com/70502759/149753302-5591d27d-ba80-437b-9ec2-bb4a73de835f.png)
![image](https://user-images.githubusercontent.com/70502759/149759863-3bc41c8a-1b90-4d66-8d3a-0b70269db818.png)

The architecture of DETR has three main components, which are a CNN backbone to extract a compact feture representation, encoder-decoder transformer, Feed-Forward Netoworks.

Data Overview
--------------
A dataset with mask labeling of three major types of concrete surface defects: crack, spalling and exposed rebar, was prepared for training and testing of the DETR for Object and Bounding Box Detection. Data set has a total 1443 number of images . Also we have an equal number of mask images . Data set does not have all annotated data for the bounding box so from mask image we have generated the bounding box .

<table>
  <tr>
    <td><img src=https://user-images.githubusercontent.com/70502759/159024634-e2c0204f-3815-4413-a238-94d4171d148a.jpg width=270 height=480></td>
    <td><img src=https://user-images.githubusercontent.com/70502759/159024661-bdd03980-6360-426a-9e77-fc23c3a3fb30.jpg width=270 height=480></td>
     <td><img src=https://user-images.githubusercontent.com/70502759/159024692-63623fb6-bd02-428b-a81e-a4c4ac1a827b.jpg width=270 height=480></td>
  </tr>  
   <tr>
    <td><img src=https://user-images.githubusercontent.com/70502759/159025947-5f66ba21-6d49-4f6b-a273-163dbc0815a1.jpg width=270 height=480></td>
    <td><img src=https://user-images.githubusercontent.com/70502759/159025974-d3356910-3429-4a4b-bb4c-42a79861c341.jpg width=270 height=480></td>
     <td><img src=https://user-images.githubusercontent.com/70502759/159025994-5df73f50-492b-42be-811a-53f1bf6cec28.jpg width=270 height=480></td>
  </tr>
 </table>


Converting concrete dataset into COCO dataset format 
-------------------------------------------
As the given dataset does not have annotated data from the mask image we have generated the bounding coordinate .
We have used skimage module label, regionprops, find_contours to get the required bounding box 
and With the help of custom code we have converted the concret dataset into COCO dataset format which can be used for training the detr . 



Details code use to generate COCO dataset format from the given mask images can be found here : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_2/MaskToBoundingBox.py 

COCO dataset format After conversion 

           path/to/coco/
               annotations/  # annotation json files
                   -instances_train2017.json
                   -instances_val2017.json
                   -instances_test2017.json      
              train2017/    # train images
              val2017/      # val images
	      test2017/     # test images
  Note : Both validation and Test contain same set of image .

  Sample Annotated Data : 
  
  
            {
            
        "images": [ 
          {
             "file_name": "0035002.jpg",
             "height": 287,
             "width": 416,
             "id": 1
          }
	     ]
	    "annotations": [
         {
            "area": 12628,
            "iscrowd": 0,
            "image_id": 1,
            "bbox": [
              142,
              0,
              44,
              287
           ],
          "category_id": 1,
          "id": 1,
          "ignore": 0,
          "segmentation": []
	       }
	     ] 
     }	


 BackBone in DETR 
------------------
        We have used resnet-50 model as backbone network for DETR.
	
Training Detr 
--------------
        We have used resnet-50 model as backbone network for DETR.
	
Loss function used 
------------------
Now we make use of the unique loss that the model uses and for that we need to define the matcher. 

Classification Loss for labels(its weight can be set by loss_ce)

Bbox Loss (its weight can be set by loss_bbox, loss_giou)

Loss/Accuracy Score Metric Visualization: 
----------------------------------------
    Classification loss: 
           loss_ce :  denotes the cross entropy loss . 
           class_error : denotes   error for predicting "object" and "no-object"          

    Compute the losses related to the bounding boxes:
        loss_bbox :  L1 regression loss
        loss_giou  : GIoU loss 
                  (   GIoU loss maximizes the overlap area of the ground truth 
		 and predicted the bounding box. It increases the predicted box's 
		 size to overlap with the target box by moving slowly 
		 towards the target box for non-overlapping cases.)

     loss : overall all model loss   

     cardinality_error : Compute the cardinality error, ie the absolute error in the number of predicted non-empty boxes. 
                         This is not really a loss, it is intended for logging purposes only. It doesn't propagate gradients

     mAP error : mean the average of precisions score  , it is intended for accuracy score for object detection problem 
     
     

Optimizer
---------
   We have used adam optimizer while training the detr . 
   
Results
-------

Last Training Logs 
------------------

AWS Training Logs 
------------------ 




   









                                                  
