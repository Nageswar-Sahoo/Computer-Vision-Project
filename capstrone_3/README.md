







                                                   DETR for Panoptic segmentation
                                                   ------------------------------
                                                   
About Model  DETR Panoptic segmentation
---------------------------------------
DETR is short for DEtection TRansformer, and consists of a convolutional backbone  followed by an encoder-decoder Transformer. It can be trained end-to-end to perform object detection .The main contribution of DETR is its simplicity: compared to other models like Faster R-CNN and Mask R-CNN, which rely on several highly engineered things like region proposals, non-maximum suppression procedure and anchor generation. This is possible due to the use of a clever loss function, the so-called bipartite matching loss . 

1443 image splitted into train and test split of 80% to 20% ratio . Hence the train set contain 1146 and 297 number of image .


![image](https://user-images.githubusercontent.com/70502759/149753302-5591d27d-ba80-437b-9ec2-bb4a73de835f.png)
![image](https://user-images.githubusercontent.com/70502759/149759863-3bc41c8a-1b90-4d66-8d3a-0b70269db818.png)
![image](https://user-images.githubusercontent.com/70502759/158041859-474702f1-b5e0-4498-abe7-34685cdd8183.png)

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


Converting concrete dataset into COCO Panoptic dataset format 
-------------------------------------------
As the given dataset does not have annotated data from the mask image we have generated the bounding coordinate for thing/instance segment 
and we have inverted the image and generated the bounding coordinate for stuff segment.
We have used cv2 connectedComponents along with pycocotools mask API to get the required bounding box and With the help of custom code we have converted the concret dataset into COCO dataset format .

Details code use to generate bounding box in COCO dataset format from the given mask images can be found here : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_3/MaskToBoundingBox.py. This will generate coco annotated json file instances_train2017 , instances_val2017 , instances_test2017



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
  
  sample data : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/tree/main/capstrone_3/coco_sample

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

We have used panoptic API (https://github.com/cocodataset/panopticapi) to get custom annotated data for panoptic segmentation training . 
We have passed above generated instances_train2017 , instances_val2017 , instances_test2017 json file as an input to panoptic API and its generated 
PNG file along with panoptic custom annotated json file . Details code use can be found here : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_3/panoptic_api/converters/detection2panoptic_coco_format.py


 sample data : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/tree/main/capstrone_3/coco_panoptic_sample

  Sample Annotated Data : 
  
  
     "annotations": [
        {
       "image_id": 1,
      "file_name": "001053.png",
      "segments_info": [
        {
          "iscrowd": 0,
          "bbox": [
            444,
            150,
            437,
            453
          ],
          "category_id": 2,
          "id": 925277,
          "ignore": 0,
          "area": 2121
        },
        {
          "iscrowd": 0,
          "bbox": [
            0,
            0,
            1008,
            754
          ],
          "category_id": 4,
          "id": 2100087,
          "ignore": 0,
          "area": 760032
          }
         ]
        }
	
<table>
  <tr>
    <td><img src=https://user-images.githubusercontent.com/70502759/166414994-5d6c8e6b-d77d-49b5-9b62-fdfc76ff361f.png width=270 height=480></td>
    <td><img src=https://user-images.githubusercontent.com/70502759/166415072-e14eba0e-3f53-4253-ad4d-f0075488cea8.png width=270 height=480></td>
     <td><img src=https://user-images.githubusercontent.com/70502759/166415119-650fa021-dd25-4a78-95fc-50deeb45c3c0.png width=270 height=480></td>
  </tr>  
   <tr>
    <td><img src=https://user-images.githubusercontent.com/70502759/166415173-e38c6742-a5f4-4ae1-8f39-532774d78f96.png width=270 height=480></td>
    <td><img src=https://user-images.githubusercontent.com/70502759/166415221-2ce20cf6-25f5-43b6-8dab-fa27f7448fbd.png width=270 height=480></td>
     <td><img src=https://user-images.githubusercontent.com/70502759/166415270-b0207ac4-847f-4387-a01c-539838b33cc2.png width=270 height=480></td>
  </tr>
 </table>	

 BackBone in DETR 
------------------
        We have used pre-train resnet-50 model as backbone network for DETR.
	
Training Detr 
--------------
     We have used the detr model provided by facebook research open source code .
     We have trained the model from scratch for 400 epochs .We have also change number of object query to 20 
     as the whole object does not contain more than 20 objects in a single image. 
     Below command used for trainig the detr - 
	
     !python -m torch.distributed.launch --nproc_per_node=1 --use_env main.py --coco_path coco --output_dir output_2  
	  --batch_size 4 --epochs 350 --num_queries 20  -lr .00001 --lr_backbone .00001 --resume output_2/checkpoint.pth 
	
	
	
Loss function used 
------------------

     Now we make use of the unique loss that the model uses and for that we need to define the matcher. 

     Classification Loss for labels(its weight can be set by loss_ce , class_error)

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

![image](https://user-images.githubusercontent.com/70502759/159144791-493d61a5-2d0f-4685-85b4-f2bdfc718071.png)
![image](https://user-images.githubusercontent.com/70502759/159144794-300fafe1-a799-401f-9e4b-8d31add2957f.png)
![image](https://user-images.githubusercontent.com/70502759/159144800-59457351-c64d-4277-a1c9-d77270e55af6.png)

     
     

Optimizer
---------
   We have used adam optimizer while training the detr . 
   
   
Inference (With Threshold kept as 0.5) 
--------------------------------------


               Orignal Image                             Ground Truth                              Predicted Bounding Box
------------------------------------------------------------------------------------------------------------------------------------


![81](https://user-images.githubusercontent.com/70502759/159162578-a710a8fe-283d-4e07-afc1-a5a9843bf78f.jpg)
![75](https://user-images.githubusercontent.com/70502759/159162581-33d655af-c404-40cb-a383-2470b0a433bc.jpg)




Evaluation Metrics on Validation Dataset (After 400 epochs of training)
-----------------------------------------------------------------------


     IoU metric: bbox
       Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.179
       Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.320
       Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.178
       Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
       Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.036
       Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.219
       Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.230
       Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.339
       Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.355
       Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.009
       Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.081
       Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.435

Last Training Logs 
------------------

           Epoch: [395]  [  0/297]  eta: 1:51:19  lr: 0.000001  class_error: 16.67  loss: 7.6345 (7.6345)  loss_ce: 0.3645 (0.3645)  loss_bbox: 0.4613 (0.4613)  loss_giou: 0.4754 (0.4754)  loss_ce_0: 0.5075 (0.5075)  loss_bbox_0: 0.4597 (0.4597)  loss_giou_0: 0.5571 (0.5571)  loss_ce_1: 0.4298 (0.4298)  loss_bbox_1: 0.3618 (0.3618)  loss_giou_1: 0.4005 (0.4005)  loss_ce_2: 0.3465 (0.3465)  loss_bbox_2: 0.3156 (0.3156)  loss_giou_2: 0.4726 (0.4726)  loss_ce_3: 0.3633 (0.3633)  loss_bbox_3: 0.3608 (0.3608)  loss_giou_3: 0.4464 (0.4464)  loss_ce_4: 0.3335 (0.3335)  loss_bbox_4: 0.4275 (0.4275)  loss_giou_4: 0.5505 (0.5505)  loss_ce_unscaled: 0.3645 (0.3645)  class_error_unscaled: 16.6667 (16.6667)  loss_bbox_unscaled: 0.0923 (0.0923)  loss_giou_unscaled: 0.2377 (0.2377)  cardinality_error_unscaled: 4.2500 (4.2500)  loss_ce_0_unscaled: 0.5075 (0.5075)  loss_bbox_0_unscaled: 0.0919 (0.0919)  loss_giou_0_unscaled: 0.2786 (0.2786)  cardinality_error_0_unscaled: 5.2500 (5.2500)  loss_ce_1_unscaled: 0.4298 (0.4298)  loss_bbox_1_unscaled: 0.0724 (0.0724)  loss_giou_1_unscaled: 0.2003 (0.2003)  cardinality_error_1_unscaled: 3.2500 
           Test: Total time: 0:00:19 (0.2646 s / it)


 

Training Notebook Link : 
------------------------

https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_3/DETR_Panoptic_Training_From_Scratch.ipynb

# References 
- Official DETR repository (https://github.com/facebookresearch/detr)
- Fine-tunne DETR ( https://github.com/woctezuma/finetune-detr )
- A Github issue regarding training detr on custom data (https://github.com/facebookresearch/detr/issues/9)
- Panoptic API (https://github.com/cocodataset/panopticapi)




   









                                                  
