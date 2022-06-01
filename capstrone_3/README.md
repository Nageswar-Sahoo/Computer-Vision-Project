







                                                   DETR for Panoptic segmentation
                                                   ------------------------------

Panoptic segmentation
---------------------

 In semantic segmentation, the goal is to classify each pixel into the given classes. In instance segmentation, we care about segmentation of the instances of objects separately. The panoptic segmentation combines semantic and instance segmentation such that all pixels are assigned a class label and all object instances are uniquely segmented.
 
Important terminologies:  

Things – Any countable object is referred to as a thing in . To exemplify – person, cat, car, key, ball are called things.

Stuff – Uncountable region of identical texture is known as stuff. For instance, road, water, sky etc.

 <table>
  <tr>
    <td><img src=https://user-images.githubusercontent.com/70502759/166416601-b126a9f7-5f44-401d-847c-c0d2cd34594a.png width=270 height=480></td>
    <td><img src=https://user-images.githubusercontent.com/70502759/166416632-349924e8-1e8a-4d45-9daa-112ed62a771f.png width=270 height=480></td>
     <td><img src=https://user-images.githubusercontent.com/70502759/166416647-1f28aa14-a0f0-4489-ac06-ce91444b2a6b.png width=270 height=480></td>
  </tr> 
 </table> 
 
                     Left: semantic segmentation, middle: instance segmentation, right: panoptic segmentation
		     
		     

                                                   
About  DETR Panoptic segmentation
---------------------------------------
DETR is short for DEtection TRansformer, and consists of a convolutional backbone  followed by an encoder-decoder Transformer. It can be trained end-to-end to perform object detection .The main contribution of DETR is its simplicity: compared to other models like Faster R-CNN and Mask R-CNN, which rely on several highly engineered things like region proposals, non-maximum suppression procedure and anchor generation. This is possible due to the use of a clever loss function, the so-called bipartite matching loss . The model predicts a box and a binary mask for each object queries. We filter the predictions for which the confidence is < threshold.
Finally, the remaining masks are merged together using a pixel-wise argmax to get the panoptic segmented image . 

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
	
Training Detr For Panoptic Task
-------------------------------
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


![54](https://user-images.githubusercontent.com/70502759/171445203-61920bee-fbaf-4d09-803c-850f78f6b0d0.jpg)
![61](https://user-images.githubusercontent.com/70502759/171445214-cf87a7a2-ceb9-4630-82ff-ad425df857de.jpg)
![62](https://user-images.githubusercontent.com/70502759/171445248-50356d6c-85af-40e2-952a-19968d87cac5.jpg)
![77](https://user-images.githubusercontent.com/70502759/171445258-428b91b1-dc21-4e93-a7b9-28f642bf2106.jpg)
![83](https://user-images.githubusercontent.com/70502759/171445273-7806977b-ed13-492b-bbc0-2c35ea04c7bc.jpg)
![85](https://user-images.githubusercontent.com/70502759/171445289-2b25034b-a24c-45f0-bd41-a7de0a4d4921.jpg)
![89](https://user-images.githubusercontent.com/70502759/171445304-2ce5221e-cda2-41e6-86fb-1710f3bdef46.jpg)
![92](https://user-images.githubusercontent.com/70502759/171445318-23cb9133-bb4e-4aeb-a60b-e7d4b5566fef.jpg)
![133](https://user-images.githubusercontent.com/70502759/171445506-e55ec5ac-dd9e-4f1a-b06d-a116e365f6bb.jpg)
![137](https://user-images.githubusercontent.com/70502759/171445531-650da94b-73bb-44e5-88f6-ce2835afb24e.jpg)

![99](https://user-images.githubusercontent.com/70502759/171445334-3ba2e62f-14cd-417a-86ab-4d39929cb3ad.jpg)
![102](https://user-images.githubusercontent.com/70502759/171445359-2b08f293-3bb3-4803-9306-e5b89610c389.jpg)
![105](https://user-images.githubusercontent.com/70502759/171445365-3718a781-5185-4f2f-81fa-644be515f87b.jpg)
![107](https://user-images.githubusercontent.com/70502759/171445377-4df2b369-3264-463f-bfcd-52f2376d83e6.jpg)
![108](https://user-images.githubusercontent.com/70502759/171445387-e0279aef-1b18-4810-b6d7-7811521db761.jpg)
![109](https://user-images.githubusercontent.com/70502759/171445398-20c98ea5-a7cf-484c-a3fe-128ab00fcb82.jpg)
![110](https://user-images.githubusercontent.com/70502759/171445403-b6589541-5b95-422f-8480-f79dac6451a5.jpg)
![112](https://user-images.githubusercontent.com/70502759/171445414-ab9902db-cf43-4118-af66-d488c1a692b4.jpg)
![114](https://user-images.githubusercontent.com/70502759/171445421-42cc3f54-d890-4341-956e-c80a195420cd.jpg)
![117](https://user-images.githubusercontent.com/70502759/171445436-2f7f8546-3e6a-4ba6-b16a-e400b5f8cdc3.jpg)
![121](https://user-images.githubusercontent.com/70502759/171445441-ec99c4db-005f-49d4-b159-c6b4b2c2c44a.jpg)
![124](https://user-images.githubusercontent.com/70502759/171445452-ee38890c-9273-4dba-8577-5354f9ce572a.jpg)
![130](https://user-images.githubusercontent.com/70502759/171445457-9f0355df-8911-4c2d-be50-82da83710d66.jpg)
![138](https://user-images.githubusercontent.com/70502759/171445639-36aa671d-acd8-4ca7-92c1-bba4bc414f32.jpg)
![139](https://user-images.githubusercontent.com/70502759/171445649-fa475cca-4daa-460c-8212-50c25a425f43.jpg)
![144](https://user-images.githubusercontent.com/70502759/171445653-44590bcb-25df-46ad-8779-1199a7873a96.jpg)
![149](https://user-images.githubusercontent.com/70502759/171445655-7e57a233-9a0b-4520-a0ed-1908cefdd667.jpg)
![151](https://user-images.githubusercontent.com/70502759/171445661-1e122017-122f-4182-9d3f-a75be37f9539.jpg)
![154](https://user-images.githubusercontent.com/70502759/171445662-50802604-dd71-4e92-b5a0-5b24c5b69b7e.jpg)
![155](https://user-images.githubusercontent.com/70502759/171445672-a0abc49e-7970-4d8f-b4d4-31e2d7ff68bd.jpg)
![158](https://user-images.githubusercontent.com/70502759/171445673-42ebe5b3-9760-4bac-b783-afd0a92526cd.jpg)
![169](https://user-images.githubusercontent.com/70502759/171445679-97e1ffd2-f3dc-495a-ab11-bd8c00809aab.jpg)
![172](https://user-images.githubusercontent.com/70502759/171445687-d6679ee2-7bd5-41e5-9917-f37b04a85add.jpg)
![173](https://user-images.githubusercontent.com/70502759/171445689-646dbdd8-aabf-4fdc-988e-642d92efb04e.jpg)
![175](https://user-images.githubusercontent.com/70502759/171445692-660b6ab3-744a-4dc2-b1bb-092e4df92cb4.jpg)
![176](https://user-images.githubusercontent.com/70502759/171445695-42cb1677-d7e1-464d-bffd-4dd6569cad3e.jpg)
![177](https://user-images.githubusercontent.com/70502759/171445702-c6133a1c-6d80-4b2d-8323-88d7a3bf467e.jpg)
![189](https://user-images.githubusercontent.com/70502759/171445705-90072945-f746-413b-96a6-f6c67d306805.jpg)
![196](https://user-images.githubusercontent.com/70502759/171445709-8552fe49-f94c-4f9b-a6ac-1167dd1dbf99.jpg)
![202](https://user-images.githubusercontent.com/70502759/171445711-f2245916-dc07-4708-857d-0d32d88224c8.jpg)
![203](https://user-images.githubusercontent.com/70502759/171445715-9a137341-6123-4f11-90bd-a07587056f3a.jpg)
![214](https://user-images.githubusercontent.com/70502759/171445724-59f2ca56-7fd3-4a22-a750-ffef6a1ef4eb.jpg)
![218](https://user-images.githubusercontent.com/70502759/171445734-2cfbd59c-b6d1-490e-8bb1-934c6300c208.jpg)
![228](https://user-images.githubusercontent.com/70502759/171445751-f00ab4b7-ee44-4343-aa92-dbc921557700.jpg)
![233](https://user-images.githubusercontent.com/70502759/171445761-d5eb47e7-0ec7-4a5b-a59d-7ef6b7513afe.jpg)
![234](https://user-images.githubusercontent.com/70502759/171445775-e12c31a9-f5f7-4bd3-a3d8-af9a75c7581b.jpg)
![240](https://user-images.githubusercontent.com/70502759/171445784-1dcc4f95-6dee-488b-b210-f0f7a9d4a66a.jpg)
![241](https://user-images.githubusercontent.com/70502759/171445802-a19f2edc-58b7-4712-9288-a23013636804.jpg)
![242](https://user-images.githubusercontent.com/70502759/171445818-16cd5f67-b22f-4295-8674-178d704c1be1.jpg)
![243](https://user-images.githubusercontent.com/70502759/171445821-8c6e7858-5e08-47f7-a9b5-f3f71b161605.jpg)
![9](https://user-images.githubusercontent.com/70502759/171445825-5c4adcb9-44e0-42ad-8b74-5a5df18eb455.jpg)
![12](https://user-images.githubusercontent.com/70502759/171445838-9637f17c-7335-4cbf-9677-acd9c9b82c5a.jpg)
![16](https://user-images.githubusercontent.com/70502759/171445844-125dd31e-3b57-46bc-96d6-965760fc524e.jpg)
![19](https://user-images.githubusercontent.com/70502759/171445853-18f18a10-0d36-4000-af68-31c18ee08940.jpg)
![27](https://user-images.githubusercontent.com/70502759/171445859-d4895ff4-0840-41f0-9daa-f811fc38fd4a.jpg)
![35](https://user-images.githubusercontent.com/70502759/171445874-100f2956-f9fa-482c-a256-686da31e5099.jpg)
![36](https://user-images.githubusercontent.com/70502759/171445884-45437036-b337-418d-be57-19a0525c59d8.jpg)
![46](https://user-images.githubusercontent.com/70502759/171445896-2cbcc932-8fca-4c5c-827f-5ac227abb678.jpg)
![48](https://user-images.githubusercontent.com/70502759/171445909-67acb4a8-5f0f-4efd-b646-efa0fb7c36f8.jpg)
![51](https://user-images.githubusercontent.com/70502759/171445921-9e18ce6a-dd84-4f98-8c6f-8590248c9d70.jpg)

![72](https://user-images.githubusercontent.com/70502759/171450822-f01a4ddf-8240-4b74-824e-cae3547c0e54.jpg)
![93](https://user-images.githubusercontent.com/70502759/171450844-b8f7dfe6-e817-4c1d-984f-98dba7443001.jpg)
![96](https://user-images.githubusercontent.com/70502759/171450899-37f19b9d-0b02-4ae9-ae6a-3831300fd47f.jpg)
![106](https://user-images.githubusercontent.com/70502759/171450916-15829e5f-316a-456a-8b7f-c959d5267579.jpg)
![112](https://user-images.githubusercontent.com/70502759/171450990-f6373cdd-eb6c-438c-bd93-9962d6e1c6cf.jpg)
![116](https://user-images.githubusercontent.com/70502759/171450998-d913ba0a-9d9c-443b-93af-46005f500632.jpg)
![121](https://user-images.githubusercontent.com/70502759/171451012-75685f17-d627-441b-a0d0-dc85cd3ac7b1.jpg)
![148](https://user-images.githubusercontent.com/70502759/171451024-4938d8de-5d99-4327-aed9-296078df33db.jpg)
![156](https://user-images.githubusercontent.com/70502759/171451031-3a5900d9-9a39-4da1-b1cc-72f7ebc3f0bd.jpg)
![169](https://user-images.githubusercontent.com/70502759/171451038-d6f4b0b2-7173-47c3-bc7b-907120fd5540.jpg)
![171](https://user-images.githubusercontent.com/70502759/171451074-b5c0f7ec-27a6-45d1-8427-2fb484e08f0a.jpg)
![173](https://user-images.githubusercontent.com/70502759/171451123-ed1304c0-18ba-478a-b036-6113be18fc08.jpg)
![180](https://user-images.githubusercontent.com/70502759/171451130-58e4ec69-b920-4443-bed9-2e5127f874d7.jpg)
![182](https://user-images.githubusercontent.com/70502759/171451147-c5616a06-077a-44d2-af4f-a2cf8bcb1121.jpg)
![184](https://user-images.githubusercontent.com/70502759/171451165-9de6f52c-88c3-4cf7-aebc-8b651da8298f.jpg)
![187](https://user-images.githubusercontent.com/70502759/171451202-f5143a5e-af50-46f8-a7c5-ec679b16c606.jpg)
![189](https://user-images.githubusercontent.com/70502759/171451215-54805dfe-6141-4263-8dc3-e22c038cd48f.jpg)
![194](https://user-images.githubusercontent.com/70502759/171451223-6cbbfdfa-c4a0-4003-9148-f98506f9b4e6.jpg)
![199](https://user-images.githubusercontent.com/70502759/171451234-9cca2139-3c50-4ba0-a251-6c699dc48ba9.jpg)
![205](https://user-images.githubusercontent.com/70502759/171451237-629107d2-e72a-4fb0-b792-71675117cb13.jpg)
![209](https://user-images.githubusercontent.com/70502759/171451248-4eb7c91a-c579-4841-90fd-4f6099baf588.jpg)
![219](https://user-images.githubusercontent.com/70502759/171451258-50e8fdb2-ba5f-41f1-92ed-8221c10caea5.jpg)
![225](https://user-images.githubusercontent.com/70502759/171451279-6f83e670-af48-4f60-82ee-6265b41f9992.jpg)
![231](https://user-images.githubusercontent.com/70502759/171451299-34e9dd29-70e4-48b7-88c8-5816536578d6.jpg)
![237](https://user-images.githubusercontent.com/70502759/171451327-f8874b20-bbb1-4f8f-8bf9-79c111bc0e30.jpg)
![238](https://user-images.githubusercontent.com/70502759/171451359-1beb6389-05b5-4114-a56a-ddd3eff81823.jpg)
![239](https://user-images.githubusercontent.com/70502759/171451371-8bc53ead-3486-4255-b505-4dc51383ec72.jpg)
![240](https://user-images.githubusercontent.com/70502759/171451375-2cb472eb-fb46-4f85-b4d2-58edc33f8d18.jpg)
![241](https://user-images.githubusercontent.com/70502759/171451385-efd6f2bc-6c7e-40f9-8f4d-3d2d1235fd20.jpg)
![242](https://user-images.githubusercontent.com/70502759/171451398-2fd1f651-66fc-4671-8bdd-fad21801f429.jpg)
![243](https://user-images.githubusercontent.com/70502759/171451409-73ce42be-7553-4de3-bdf8-60a8bf2c5023.jpg)
![244](https://user-images.githubusercontent.com/70502759/171451416-d87a2de1-46a1-4e90-ac72-665e26a8f3f5.jpg)
![245](https://user-images.githubusercontent.com/70502759/171451428-75718357-4169-45ad-ab14-1eca84446007.jpg)
![246](https://user-images.githubusercontent.com/70502759/171451442-1c13af28-3a5f-4627-bc53-3393a5c437ed.jpg)
![247](https://user-images.githubusercontent.com/70502759/171451450-37eab0ca-766d-4d4f-8b84-501df2db6d92.jpg)


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




   









                                                  
