


                                                   DETR for Object and Bounding Box Detection
                                                   ------------------------------------------
                                                   
About Model  DETR
-----------------
DETR is short for DEtection TRansformer, and consists of a convolutional backbone  followed by an encoder-decoder Transformer. It can be trained end-to-end to perform object detection .The main contribution of DETR is its simplicity: compared to other models like Faster R-CNN and Mask R-CNN, which rely on several highly engineered things like region proposals, non-maximum suppression procedure and anchor generation. This is possible due to the use of a clever loss function, the so-called bipartite matching loss

![image](https://user-images.githubusercontent.com/70502759/149753302-5591d27d-ba80-437b-9ec2-bb4a73de835f.png)
![image](https://user-images.githubusercontent.com/70502759/149759863-3bc41c8a-1b90-4d66-8d3a-0b70269db818.png)

The architecture of DETR has three main components, which are a CNN backbone to extract a compact feture representation, encoder-decoder transformer, Feed-Forward Netoworks.

Step 1 : Data Overview
-----------------------------------------------
A dataset with mask labeling of three major types of concrete surface defects: crack, spalling and exposed rebar, was prepared for training and testing of the DETR for
Object and Bounding Box Detection. Data set has total 1443 number of image . Also we have equal number of mask image . Data set does not have all annotated data for bounding box so from mask image we have to generate the bounding box . 

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






Step 2 : Converting dataset into COCO dataset format 
-----------------------------------------------------
As given dataset doest not have annotated data from mask image we have genrate the bounding coordinate .
We have used skimage module label, regionprops, find_contours to get the required bounding box and 
with the help of custom code we have converted the concret dataset into COCO dataset format which can be directly trained in detr . 

Details code use to generate COCO dataset format  can be found here : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_2/MaskToBoundingBox.py 

COCO dataset format After conversion 

           path/to/coco/
               annotations/  # annotation json files
                   -instances_train2017.json
                   -instances_val2017.json
                   -instances_test2017.json      
              train2017/    # train images
              val2017/      # val images
	      test2017/     # test images
  
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



Step 3 : BackBone in DETR 
-------------------------
        We have used resnet-50 model as backbone network for DETR.
	
Step 4 : Training Detr 
-------------------------
        We have used resnet-50 model as backbone network for DETR.
	
Loss function used 
------------------
Now we make use of the unique loss that the model uses and for that we need to define the matcher. DETR calcuates three individual losses :

Classification Loss for labels(its weight can be set by loss_ce)
Bbox Loss (its weight can be set by loss_bbox, loss_giou)
Loss for Background class

loss
map
loss_ce
loss_bbox
loss_giou
class_error

Results
-------

	
COCO Evaluation Metrics on Validation Dataset (After 15 epochs of training)
-----------------------------------------------------------------------------

Metrics Visualization
-----------------------
Augmentation methods
--------------------


   









                                                  
