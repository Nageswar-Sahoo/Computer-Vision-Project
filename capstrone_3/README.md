







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
![image](https://user-images.githubusercontent.com/70502759/171456306-903cfd40-07e0-4baf-ac9c-80d44f86599c.png)

     
     

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

IoU metric: segm
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.010
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.012
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.014


Last Training Logs 
------------------

 
 Epoch: [82]  [  0/297]  eta: 1:46:41  lr: 0.000000  class_error: 10.00  loss: 9.2184 (9.2184)  loss_ce: 0.2548 (0.2548)  loss_bbox: 0.3029 (0.3029)  loss_giou: 0.6091 (0.6091)  loss_mask: 0.0707 (0.0707)  loss_dice: 0.6245 (0.6245)  loss_ce_0: 0.4821 (0.4821)  loss_bbox_0: 0.6450 (0.6450)  loss_giou_0: 0.9095 (0.9095)  loss_ce_1: 0.3126 (0.3126)  loss_bbox_1: 0.4918 (0.4918)  loss_giou_1: 0.6355 (0.6355)  loss_ce_2: 0.2479 (0.2479)  loss_bbox_2: 0.4271 (0.4271)  loss_giou_2: 0.7115 (0.7115)  loss_ce_3: 0.2756 (0.2756)  loss_bbox_3: 0.4151 (0.4151)  loss_giou_3: 0.6513 (0.6513)  loss_ce_4: 0.2259 (0.2259)  loss_bbox_4: 0.3373 (0.3373)  loss_giou_4: 0.5881 (0.5881)  loss_ce_unscaled: 0.2548 (0.2548)  class_error_unscaled: 10.0000 (10.0000)  loss_bbox_unscaled: 0.0606 (0.0606)  loss_giou_unscaled: 0.3045 (0.3045)  cardinality_error_unscaled: 3.2500 (3.2500)  loss_mask_unscaled: 0.0707 (0.0707)  loss_dice_unscaled: 0.6245 (0.6245)  loss_ce_0_unscaled: 0.4821 (0.4821)  loss_bbox_0_unscaled: 0.1290 (0.1290)  loss_giou_0_unscaled: 0.4548 (0.4548)  cardinality_error_0_unscaled: 5.5000 (5.5000)  loss_ce_1_unscaled: 0.3126 (0.3126)  loss_bbox_1_unscaled: 0.0984 (0.0984)  loss_giou_1_unscaled: 0.3178 (0.3178)  cardinality_error_1_unscaled: 2.7500 (2.7500)  loss_ce_2_unscaled: 0.2479 (0.2479)  loss_bbox_2_unscaled: 0.0854 (0.0854)  loss_giou_2_unscaled: 0.3558 (0.3558)  cardinality_error_2_unscaled: 4.0000 (4.0000)  loss_ce_3_unscaled: 0.2756 (0.2756)  loss_bbox_3_unscaled: 0.0830 (0.0830)  loss_giou_3_unscaled: 0.3257 (0.3257)  cardinality_error_3_unscaled: 2.7500 (2.7500)  loss_ce_4_unscaled: 0.2259 (0.2259)  loss_bbox_4_unscaled: 0.0675 (0.0675)  loss_giou_4_unscaled: 0.2941 (0.2941)  cardinality_error_4_unscaled: 3.5000 (3.5000)  time: 21.5549  data: 20.4311  max mem: 3373
Epoch: [82]  [ 10/297]  eta: 0:16:10  lr: 0.000000  class_error: 11.11  loss: 5.5193 (7.5002)  loss_ce: 0.2548 (0.2611)  loss_bbox: 0.1496 (0.3510)  loss_giou: 0.2445 (0.4518)  loss_mask: 0.0560 (0.0577)  loss_dice: 0.6062 (0.6361)  loss_ce_0: 0.3548 (0.4007)  loss_bbox_0: 0.2041 (0.4377)  loss_giou_0: 0.2776 (0.5499)  loss_ce_1: 0.2790 (0.2714)  loss_bbox_1: 0.2057 (0.4088)  loss_giou_1: 0.2623 (0.4948)  loss_ce_2: 0.2313 (0.2260)  loss_bbox_2: 0.1674 (0.3821)  loss_giou_2: 0.2187 (0.4888)  loss_ce_3: 0.2405 (0.2336)  loss_bbox_3: 0.1417 (0.3642)  loss_giou_3: 0.2321 (0.4480)  loss_ce_4: 0.2259 (0.2310)  loss_bbox_4: 0.2078 (0.3687)  loss_giou_4: 0.2086 (0.4366)  loss_ce_unscaled: 0.2548 (0.2611)  class_error_unscaled: 9.5238 (8.0123)  loss_bbox_unscaled: 0.0299 (0.0702)  loss_giou_unscaled: 0.1223 (0.2259)  cardinality_error_unscaled: 1.5000 (2.3864)  loss_mask_unscaled: 0.0560 (0.0577)  loss_dice_unscaled: 0.6062 (0.6361)  loss_ce_0_unscaled: 0.3548 (0.4007)  loss_bbox_0_unscaled: 0.0408 (0.0875)  loss_giou_0_unscaled: 0.1388 (0.2749)  cardinality_error_0_unscaled: 3.7500 (3.9091)  loss_ce_1_unscaled: 0.2790 (0.2714)  loss_bbox_1_unscaled: 0.0411 (0.0818)  loss_giou_1_unscaled: 0.1311 (0.2474)  cardinality_error_1_unscaled: 2.7500 (2.7727)  loss_ce_2_unscaled: 0.2313 (0.2260)  loss_bbox_2_unscaled: 0.0335 (0.0764)  loss_giou_2_unscaled: 0.1094 (0.2444)  cardinality_error_2_unscaled: 1.7500 (2.5455)  loss_ce_3_unscaled: 0.2405 (0.2336)  loss_bbox_3_unscaled: 0.0283 (0.0728)  loss_giou_3_unscaled: 0.1160 (0.2240)  cardinality_error_3_unscaled: 1.5000 (2.1364)  loss_ce_4_unscaled: 0.2259 (0.2310)  loss_bbox_4_unscaled: 0.0416 (0.0737)  loss_giou_4_unscaled: 0.1043 (0.2183)  cardinality_error_4_unscaled: 1.5000 (2.2727)  time: 3.3804  data: 2.8114  max mem: 3663
Epoch: [82]  [ 20/297]  eta: 0:11:23  lr: 0.000000  class_error: 12.50  loss: 4.6553 (6.3578)  loss_ce: 0.2407 (0.2568)  loss_bbox: 0.1495 (0.2657)  loss_giou: 0.2301 (0.3661)  loss_mask: 0.0622 (0.0607)  loss_dice: 0.5970 (0.6184)  loss_ce_0: 0.3875 (0.4143)  loss_bbox_0: 0.1577 (0.3251)  loss_giou_0: 0.2183 (0.4221)  loss_ce_1: 0.2790 (0.2871)  loss_bbox_1: 0.1818 (0.2986)  loss_giou_1: 0.2190 (0.3904)  loss_ce_2: 0.2313 (0.2555)  loss_bbox_2: 0.1426 (0.2755)  loss_giou_2: 0.2047 (0.3782)  loss_ce_3: 0.2304 (0.2525)  loss_bbox_3: 0.1417 (0.2621)  loss_giou_3: 0.2062 (0.3536)  loss_ce_4: 0.2085 (0.2473)  loss_bbox_4: 0.1660 (0.2736)  loss_giou_4: 0.1959 (0.3542)  loss_ce_unscaled: 0.2407 (0.2568)  class_error_unscaled: 11.1111 (9.5961)  loss_bbox_unscaled: 0.0299 (0.0531)  loss_giou_unscaled: 0.1150 (0.1831)  cardinality_error_unscaled: 1.5000 (2.1310)  loss_mask_unscaled: 0.0622 (0.0607)  loss_dice_unscaled: 0.5970 (0.6184)  loss_ce_0_unscaled: 0.3875 (0.4143)  loss_bbox_0_unscaled: 0.0315 (0.0650)  loss_giou_0_unscaled: 0.1092 (0.2110)  cardinality_error_0_unscaled: 4.2500 (4.1071)  loss_ce_1_unscaled: 0.2790 (0.2871)  loss_bbox_1_unscaled: 0.0364 (0.0597)  loss_giou_1_unscaled: 0.1095 (0.1952)  cardinality_error_1_unscaled: 2.2500 (2.7381)  loss_ce_2_unscaled: 0.2313 (0.2555)  loss_bbox_2_unscaled: 0.0285 (0.0551)  loss_giou_2_unscaled: 0.1024 (0.1891)  cardinality_error_2_unscaled: 1.7500 (2.4048)  loss_ce_3_unscaled: 0.2304 (0.2525)  loss_bbox_3_unscaled: 0.0283 (0.0524)  loss_giou_3_unscaled: 0.1031 (0.1768)  cardinality_error_3_unscaled: 1.5000 (2.1429)  loss_ce_4_unscaled: 0.2085 (0.2473)  loss_bbox_4_unscaled: 0.0332 (0.0547)  loss_giou_4_unscaled: 0.0979 (0.1771)  cardinality_error_4_unscaled: 1.5000 (2.0476)  time: 1.5137  data: 1.0088  max mem: 4529
Epoch: [82]  [ 30/297]  eta: 0:09:41  lr: 0.000000  class_error: 12.50  loss: 4.9175 (6.6281)  loss_ce: 0.2787 (0.2796)  loss_bbox: 0.1734 (0.2625)  loss_giou: 0.2432 (0.3967)  loss_mask: 0.0633 (0.0618)  loss_dice: 0.6055 (0.6181)  loss_ce_0: 0.4158 (0.4189)  loss_bbox_0: 0.1633 (0.3084)  loss_giou_0: 0.2798 (0.4430)  loss_ce_1: 0.2866 (0.2960)  loss_bbox_1: 0.1644 (0.2943)  loss_giou_1: 0.2815 (0.4155)  loss_ce_2: 0.2816 (0.2771)  loss_bbox_2: 0.1797 (0.2790)  loss_giou_2: 0.2621 (0.4095)  loss_ce_3: 0.2854 (0.2794)  loss_bbox_3: 0.1715 (0.2615)  loss_giou_3: 0.2471 (0.3914)  loss_ce_4: 0.2999 (0.2712)  loss_bbox_4: 0.1736 (0.2733)  loss_giou_4: 0.2428 (0.3908)  loss_ce_unscaled: 0.2787 (0.2796)  class_error_unscaled: 12.5000 (10.9771)  loss_bbox_unscaled: 0.0347 (0.0525)  loss_giou_unscaled: 0.1216 (0.1984)  cardinality_error_unscaled: 1.5000 (2.3065)  loss_mask_unscaled: 0.0633 (0.0618)  loss_dice_unscaled: 0.6055 (0.6181)  loss_ce_0_unscaled: 0.4158 (0.4189)  loss_bbox_0_unscaled: 0.0327 (0.0617)  loss_giou_0_unscaled: 0.1399 (0.2215)  cardinality_error_0_unscaled: 4.2500 (4.2016)  loss_ce_1_unscaled: 0.2866 (0.2960)  loss_bbox_1_unscaled: 0.0329 (0.0589)  loss_giou_1_unscaled: 0.1407 (0.2078)  cardinality_error_1_unscaled: 2.2500 (2.8145)  loss_ce_2_unscaled: 0.2816 (0.2771)  loss_bbox_2_unscaled: 0.0359 (0.0558)  loss_giou_2_unscaled: 0.1311 (0.2047)  cardinality_error_2_unscaled: 2.0000 (2.5081)  loss_ce_3_unscaled: 0.2854 (0.2794)  loss_bbox_3_unscaled: 0.0343 (0.0523)  loss_giou_3_unscaled: 0.1235 (0.1957)  cardinality_error_3_unscaled: 2.0000 (2.2984)  loss_ce_4_unscaled: 0.2999 (0.2712)  loss_bbox_4_unscaled: 0.0347 (0.0547)  loss_giou_4_unscaled: 0.1214 (0.1954)  cardinality_error_4_unscaled: 1.5000 (2.2339)  time: 1.5165  data: 0.9801  max mem: 4529
Epoch: [82]  [ 40/297]  eta: 0:08:44  lr: 0.000000  class_error: 0.00  loss: 6.5469 (7.0658)  loss_ce: 0.2836 (0.2724)  loss_bbox: 0.2142 (0.2920)  loss_giou: 0.3631 (0.4357)  loss_mask: 0.0631 (0.0613)  loss_dice: 0.6322 (0.6285)  loss_ce_0: 0.4237 (0.4262)  loss_bbox_0: 0.2669 (0.3546)  loss_giou_0: 0.4126 (0.4991)  loss_ce_1: 0.2866 (0.2931)  loss_bbox_1: 0.2309 (0.3219)  loss_giou_1: 0.4149 (0.4573)  loss_ce_2: 0.2854 (0.2736)  loss_bbox_2: 0.2417 (0.3046)  loss_giou_2: 0.4040 (0.4504)  loss_ce_3: 0.2854 (0.2711)  loss_bbox_3: 0.2165 (0.2973)  loss_giou_3: 0.3910 (0.4337)  loss_ce_4: 0.2501 (0.2643)  loss_bbox_4: 0.2200 (0.2958)  loss_giou_4: 0.3678 (0.4330)  loss_ce_unscaled: 0.2836 (0.2724)  class_error_unscaled: 10.0000 (10.4068)  loss_bbox_unscaled: 0.0428 (0.0584)  loss_giou_unscaled: 0.1815 (0.2178)  cardinality_error_unscaled: 2.7500 (2.5244)  loss_mask_unscaled: 0.0631 (0.0613)  loss_dice_unscaled: 0.6322 (0.6285)  loss_ce_0_unscaled: 0.4237 (0.4262)  loss_bbox_0_unscaled: 0.0534 (0.0709)  loss_giou_0_unscaled: 0.2063 (0.2495)  cardinality_error_0_unscaled: 4.0000 (4.1890)  loss_ce_1_unscaled: 0.2866 (0.2931)  loss_bbox_1_unscaled: 0.0462 (0.0644)  loss_giou_1_unscaled: 0.2074 (0.2286)  cardinality_error_1_unscaled: 3.0000 (2.9817)  loss_ce_2_unscaled: 0.2854 (0.2736)  loss_bbox_2_unscaled: 0.0483 (0.0609)  loss_giou_2_unscaled: 0.2020 (0.2252)  cardinality_error_2_unscaled: 2.7500 (2.6829)  loss_ce_3_unscaled: 0.2854 (0.2711)  loss_bbox_3_unscaled: 0.0433 (0.0595)  loss_giou_3_unscaled: 0.1955 (0.2168)  cardinality_error_3_unscaled: 2.7500 (2.5305)  loss_ce_4_unscaled: 0.2501 (0.2643)  loss_bbox_4_unscaled: 0.0440 (0.0592)  loss_giou_4_unscaled: 0.1839 (0.2165)  cardinality_error_4_unscaled: 2.7500 (2.4451)  time: 1.5905  data: 1.0348  max mem: 4529
Epoch: [82]  [ 50/297]  eta: 0:08:03  lr: 0.000000  class_error: 0.00  loss: 6.5469 (-3270383814939019.5000)  loss_ce: 0.2710 (0.2937)  loss_bbox: 0.2278 (5957.5027)  loss_giou: 0.3631 (-3233829769357994.0000)  loss_mask: 0.0617 (0.0616)  loss_dice: 0.6353 (0.6308)  loss_ce_0: 0.4388 (0.4390)  loss_bbox_0: 0.3421 (5957.5517)  loss_giou_0: 0.4706 (-60003749004.0544)  loss_ce_1: 0.2901 (0.3083)  loss_bbox_1: 0.2610 (5957.5108)  loss_giou_1: 0.4149 (-135433932237.3543)  loss_ce_2: 0.2705 (0.2878)  loss_bbox_2: 0.2631 (5957.4908)  loss_giou_2: 0.4040 (-301727456155.1776)  loss_ce_3: 0.2799 (0.2851)  loss_bbox_3: 0.2255 (5957.4880)  loss_giou_3: 0.4273 (-1900013132699.1865)  loss_ce_4: 0.2485 (0.2772)  loss_bbox_4: 0.2438 (5957.4899)  loss_giou_4: 0.3406 (-34157027491197.0742)  loss_ce_unscaled: 0.2710 (0.2937)  class_error_unscaled: 10.0000 (10.5931)  loss_bbox_unscaled: 0.0456 (1191.5006)  loss_giou_unscaled: 0.1815 (-1616914884678997.0000)  cardinality_error_unscaled: 2.7500 (2.6078)  loss_mask_unscaled: 0.0617 (0.0616)  loss_dice_unscaled: 0.6353 (0.6308)  loss_ce_0_unscaled: 0.4388 (0.4390)  loss_bbox_0_unscaled: 0.0684 (1191.5104)  loss_giou_0_unscaled: 0.2353 (-30001874502.0272)  cardinality_error_0_unscaled: 3.7500 (4.2843)  loss_ce_1_unscaled: 0.2901 (0.3083)  loss_bbox_1_unscaled: 0.0522 (1191.5021)  loss_giou_1_unscaled: 0.2074 (-67716966118.6771)  cardinality_error_1_unscaled: 3.0000 (2.9951)  loss_ce_2_unscaled: 0.2705 (0.2878)  loss_bbox_2_unscaled: 0.0526 (1191.4982)  loss_giou_2_unscaled: 0.2020 (-150863728077.5888)  cardinality_error_2_unscaled: 3.0000 (2.7696)  loss_ce_3_unscaled: 0.2799 (0.2851)  loss_bbox_3_unscaled: 0.0451 (1191.4976)  loss_giou_3_unscaled: 0.2136 (-950006566349.5933)  cardinality_error_3_unscaled: 3.2500 (2.6373)  loss_ce_4_unscaled: 0.2485 (0.2772)  loss_bbox_4_unscaled: 0.0488 (1191.4980)  loss_giou_4_unscaled: 0.1703 (-17078513745598.5371)  cardinality_error_4_unscaled: 2.7500 (2.5588)  time: 1.6168  data: 1.0604  max mem: 4529
Epoch: [82]  [ 60/297]  eta: 0:07:27  lr: 0.000000  class_error: 0.00  loss: 6.0092 (-26694522063591184.0000)  loss_ce: 0.2834 (0.3003)  loss_bbox: 0.2345 (13024.8766)  loss_giou: 0.3395 (-25624762026321080.0000)  loss_mask: 0.0613 (0.0623)  loss_dice: 0.6280 (0.6328)  loss_ce_0: 0.4180 (0.4369)  loss_bbox_0: 0.3047 (13024.8980)  loss_giou_0: 0.4137 (-110411632035.1762)  loss_ce_1: 0.3136 (0.3198)  loss_bbox_1: 0.2610 (13024.8716)  loss_giou_1: 0.3587 (-141649675851.0903)  loss_ce_2: 0.2753 (0.3006)  loss_bbox_2: 0.2024 (13024.8404)  loss_giou_2: 0.3137 (-459383483408.3590)  loss_ce_3: 0.2838 (0.2920)  loss_bbox_3: 0.2255 (13024.8361)  loss_giou_3: 0.3028 (-13460239930887.9746)  loss_ce_4: 0.2869 (0.2896)  loss_bbox_4: 0.2438 (13024.8603)  loss_giou_4: 0.2884 (-1055586077518327.2500)  loss_ce_unscaled: 0.2834 (0.3003)  class_error_unscaled: 9.0909 (10.5694)  loss_bbox_unscaled: 0.0469 (2604.9753)  loss_giou_unscaled: 0.1698 (-12812381013160540.0000)  cardinality_error_unscaled: 2.2500 (2.7336)  loss_mask_unscaled: 0.0613 (0.0623)  loss_dice_unscaled: 0.6280 (0.6328)  loss_ce_0_unscaled: 0.4180 (0.4369)  loss_bbox_0_unscaled: 0.0609 (2604.9797)  loss_giou_0_unscaled: 0.2068 (-55205816017.5881)  cardinality_error_0_unscaled: 3.7500 (4.2992)  loss_ce_1_unscaled: 0.3136 (0.3198)  loss_bbox_1_unscaled: 0.0522 (2604.9743)  loss_giou_1_unscaled: 0.1794 (-70824837925.5452)  cardinality_error_1_unscaled: 2.2500 (3.0697)  loss_ce_2_unscaled: 0.2753 (0.3006)  loss_bbox_2_unscaled: 0.0405 (2604.9682)  loss_giou_2_unscaled: 0.1569 (-229691741704.1795)  cardinality_error_2_unscaled: 2.7500 (2.8811)  loss_ce_3_unscaled: 0.2838 (0.2920)  loss_bbox_3_unscaled: 0.0451 (2604.9672)  loss_giou_3_unscaled: 0.1514 (-6730119965443.9873)  cardinality_error_3_unscaled: 2.7500 (2.7705)  loss_ce_4_unscaled: 0.2869 (0.2896)  loss_bbox_4_unscaled: 0.0488 (2604.9721)  loss_giou_4_unscaled: 0.1442 (-527793038759163.6250)  cardinality_error_4_unscaled: 2.5000 (2.6926)  time: 1.5822  data: 1.0067  max mem: 4664
Epoch: [82]  [ 70/297]  eta: 0:06:56  lr: 0.000000  class_error: 0.00  loss: 5.7614 (-22934730223648764.0000)  loss_ce: 0.2828 (0.2945)  loss_bbox: 0.2255 (11190.4244)  loss_giou: 0.3033 (-22015640614163180.0000)  loss_mask: 0.0635 (0.0626)  loss_dice: 0.6280 (0.6329)  loss_ce_0: 0.4379 (0.4387)  loss_bbox_0: 0.2545 (11190.4477)  loss_giou_0: 0.3181 (-94860697945.6569)  loss_ce_1: 0.3315 (0.3243)  loss_bbox_1: 0.2522 (11190.4218)  loss_giou_1: 0.2882 (-121699017280.4573)  loss_ce_2: 0.3117 (0.2953)  loss_bbox_2: 0.2246 (11190.3940)  loss_giou_2: 0.2785 (-394681584336.7028)  loss_ce_3: 0.2838 (0.2900)  loss_bbox_3: 0.2357 (11190.3884)  loss_giou_3: 0.2269 (-11564431489917.7852)  loss_ce_4: 0.2842 (0.2853)  loss_bbox_4: 0.2260 (11190.4107)  loss_giou_4: 0.2848 (-906911982093210.7500)  loss_ce_unscaled: 0.2828 (0.2945)  class_error_unscaled: 9.0909 (10.2090)  loss_bbox_unscaled: 0.0451 (2238.0849)  loss_giou_unscaled: 0.1516 (-11007820307081590.0000)  cardinality_error_unscaled: 3.5000 (2.7641)  loss_mask_unscaled: 0.0635 (0.0626)  loss_dice_unscaled: 0.6280 (0.6329)  loss_ce_0_unscaled: 0.4379 (0.4387)  loss_bbox_0_unscaled: 0.0509 (2238.0896)  loss_giou_0_unscaled: 0.1590 (-47430348972.8285)  cardinality_error_0_unscaled: 4.0000 (4.2923)  loss_ce_1_unscaled: 0.3315 (0.3243)  loss_bbox_1_unscaled: 0.0504 (2238.0843)  loss_giou_1_unscaled: 0.1441 (-60849508640.2287)  cardinality_error_1_unscaled: 2.5000 (3.0634)  loss_ce_2_unscaled: 0.3117 (0.2953)  loss_bbox_2_unscaled: 0.0449 (2238.0789)  loss_giou_2_unscaled: 0.1392 (-197340792168.3514)  cardinality_error_2_unscaled: 2.2500 (2.8803)  loss_ce_3_unscaled: 0.2838 (0.2900)  loss_bbox_3_unscaled: 0.0471 (2238.0777)  loss_giou_3_unscaled: 0.1134 (-5782215744958.8926)  cardinality_error_3_unscaled: 2.5000 (2.7817)  loss_ce_4_unscaled: 0.2842 (0.2853)  loss_bbox_4_unscaled: 0.0452 (2238.0822)  loss_giou_4_unscaled: 0.1424 (-453455991046605.3750)  cardinality_error_4_unscaled: 3.2500 (2.7289)  time: 1.5178  data: 0.9577  max mem: 4664
Epoch: [82]  [ 80/297]  eta: 0:06:27  lr: 0.000000  class_error: 12.50  loss: 5.7614 (-30318784133868608.0000)  loss_ce: 0.2499 (0.3185)  loss_bbox: 0.2493 (16577.8547)  loss_giou: 0.2573 (-29343591978228244.0000)  loss_mask: 0.0633 (0.0626)  loss_dice: 0.6189 (0.6331)  loss_ce_0: 0.4722 (0.4481)  loss_bbox_0: 0.3313 (16577.8301)  loss_giou_0: 0.3181 (-113018157485.3549)  loss_ce_1: 0.2653 (0.3331)  loss_bbox_1: 0.3175 (16577.8020)  loss_giou_1: 0.2708 (-188421303965.5901)  loss_ce_2: 0.3127 (0.3071)  loss_bbox_2: 0.2460 (16577.7712)  loss_giou_2: 0.2546 (-700389277493.3151)  loss_ce_3: 0.2454 (0.2950)  loss_bbox_3: 0.2408 (16577.7680)  loss_giou_3: 0.2269 (-13749688405965.0254)  loss_ce_4: 0.2430 (0.2934)  loss_bbox_4: 0.2649 (16577.7864)  loss_giou_4: 0.2614 (-960438104532056.1250)  loss_ce_unscaled: 0.2499 (0.3185)  class_error_unscaled: 11.1111 (10.9719)  loss_bbox_unscaled: 0.0499 (3315.5709)  loss_giou_unscaled: 0.1286 (-14671795989114122.0000)  cardinality_error_unscaled: 2.2500 (2.7068)  loss_mask_unscaled: 0.0633 (0.0626)  loss_dice_unscaled: 0.6189 (0.6331)  loss_ce_0_unscaled: 0.4722 (0.4481)  loss_bbox_0_unscaled: 0.0663 (3315.5661)  loss_giou_0_unscaled: 0.1590 (-56509078742.6774)  cardinality_error_0_unscaled: 4.0000 (4.3025)  loss_ce_1_unscaled: 0.2653 (0.3331)  loss_bbox_1_unscaled: 0.0635 (3315.5603)  loss_giou_1_unscaled: 0.1354 (-94210651982.7951)  cardinality_error_1_unscaled: 2.7500 (3.0216)  loss_ce_2_unscaled: 0.3127 (0.3071)  loss_bbox_2_unscaled: 0.0492 (3315.5543)  loss_giou_2_unscaled: 0.1273 (-350194638746.6575)  cardinality_error_2_unscaled: 2.0000 (2.8148)  loss_ce_3_unscaled: 0.2454 (0.2950)  loss_bbox_3_unscaled: 0.0482 (3315.5536)  loss_giou_3_unscaled: 0.1134 (-6874844202982.5127)  cardinality_error_3_unscaled: 2.0000 (2.7253)  loss_ce_4_unscaled: 0.2430 (0.2934)  loss_bbox_4_unscaled: 0.0530 (3315.5573)  loss_giou_4_unscaled: 0.1307 (-480219052266028.0625)  cardinality_error_4_unscaled: 2.2500 (2.6605)  time: 1.4642  data: 0.9202  max mem: 4664
Epoch: [82]  [ 90/297]  eta: 0:06:10  lr: 0.000000  class_error: 0.00  loss: 5.3821 (-26987049613663264.0000)  loss_ce: 0.2499 (0.3116)  loss_bbox: 0.2396 (14756.1379)  loss_giou: 0.2770 (-26119021431170196.0000)  loss_mask: 0.0641 (0.0629)  loss_dice: 0.6152 (0.6294)  loss_ce_0: 0.4253 (0.4448)  loss_bbox_0: 0.2787 (14756.1200)  loss_giou_0: 0.2951 (-100598579739.6697)  loss_ce_1: 0.2562 (0.3294)  loss_bbox_1: 0.2349 (14756.0901)  loss_giou_1: 0.2532 (-167715666167.1361)  loss_ce_2: 0.2804 (0.3018)  loss_bbox_2: 0.2250 (14756.0644)  loss_giou_2: 0.2845 (-623423422823.6798)  loss_ce_3: 0.2315 (0.2919)  loss_bbox_3: 0.2378 (14756.0610)  loss_giou_3: 0.2553 (-12238733636078.7188)  loss_ce_4: 0.2298 (0.2908)  loss_bbox_4: 0.2303 (14756.0781)  loss_giou_4: 0.2817 (-854895455682379.6250)  loss_ce_unscaled: 0.2499 (0.3116)  class_error_unscaled: 11.1111 (11.0483)  loss_bbox_unscaled: 0.0479 (2951.2276)  loss_giou_unscaled: 0.1385 (-13059510715585098.0000)  cardinality_error_unscaled: 1.7500 (2.6154)  loss_mask_unscaled: 0.0641 (0.0629)  loss_dice_unscaled: 0.6152 (0.6294)  loss_ce_0_unscaled: 0.4253 (0.4448)  loss_bbox_0_unscaled: 0.0557 (2951.2241)  loss_giou_0_unscaled: 0.1476 (-50299289869.8348)  cardinality_error_0_unscaled: 4.0000 (4.3324)  loss_ce_1_unscaled: 0.2562 (0.3294)  loss_bbox_1_unscaled: 0.0470 (2951.2180)  loss_giou_1_unscaled: 0.1266 (-83857833083.5680)  cardinality_error_1_unscaled: 2.2500 (2.9588)  loss_ce_2_unscaled: 0.2804 (0.3018)  loss_bbox_2_unscaled: 0.0450 (2951.2129)  loss_giou_2_unscaled: 0.1422 (-311711711411.8399)  cardinality_error_2_unscaled: 2.0000 (2.7473)  loss_ce_3_unscaled: 0.2315 (0.2919)  loss_bbox_3_unscaled: 0.0476 (2951.2122)  loss_giou_3_unscaled: 0.1276 (-6119366818039.3594)  cardinality_error_3_unscaled: 1.7500 (2.6511)  loss_ce_4_unscaled: 0.2298 (0.2908)  loss_bbox_4_unscaled: 0.0461 (2951.2157)  loss_giou_4_unscaled: 0.1409 (-427447727841189.8125)  cardinality_error_4_unscaled: 1.7500 (2.5989)  time: 1.6406  data: 1.0641  max mem: 4664
Epoch: [82]  [100/297]  eta: 0:05:49  lr: 0.000000  class_error: 0.00  loss: 6.3863 (-30413166231820632.0000)  loss_ce: 0.2533 (0.3199)  loss_bbox: 0.2721 (15335.4885)  loss_giou: 0.3778 (-29469856696228996.0000)  loss_mask: 0.0641 (0.0627)  loss_dice: 0.6174 (0.6327)  loss_ce_0: 0.4253 (0.4446)  loss_bbox_0: 0.2826 (15335.4744)  loss_giou_0: 0.4483 (-96202354728.0770)  loss_ce_1: 0.2923 (0.3342)  loss_bbox_1: 0.2373 (15335.4418)  loss_giou_1: 0.3703 (-156622751642.1778)  loss_ce_2: 0.2944 (0.3084)  loss_bbox_2: 0.2497 (15335.4142)  loss_giou_2: 0.3996 (-621738973041.6407)  loss_ce_3: 0.2858 (0.3029)  loss_bbox_3: 0.2628 (15335.4099)  loss_giou_3: 0.3810 (-13114799705097.7246)  loss_ce_4: 0.2859 (0.3058)  loss_bbox_4: 0.2566 (15335.4334)  loss_giou_4: 0.3830 (-929317975314066.7500)  loss_ce_unscaled: 0.2533 (0.3199)  class_error_unscaled: 11.1111 (11.3020)  loss_bbox_unscaled: 0.0544 (3067.0977)  loss_giou_unscaled: 0.1889 (-14734928348114498.0000)  cardinality_error_unscaled: 1.7500 (2.7178)  loss_mask_unscaled: 0.0641 (0.0627)  loss_dice_unscaled: 0.6174 (0.6327)  loss_ce_0_unscaled: 0.4253 (0.4446)  loss_bbox_0_unscaled: 0.0565 (3067.0949)  loss_giou_0_unscaled: 0.2241 (-48101177364.0385)  cardinality_error_0_unscaled: 4.5000 (4.4257)  loss_ce_1_unscaled: 0.2923 (0.3342)  loss_bbox_1_unscaled: 0.0475 (3067.0883)  loss_giou_1_unscaled: 0.1852 (-78311375821.0889)  cardinality_error_1_unscaled: 2.5000 (3.0545)  loss_ce_2_unscaled: 0.2944 (0.3084)  loss_bbox_2_unscaled: 0.0499 (3067.0829)  loss_giou_2_unscaled: 0.1998 (-310869486520.8204)  cardinality_error_2_unscaled: 2.5000 (2.8540)  loss_ce_3_unscaled: 0.2858 (0.3029)  loss_bbox_3_unscaled: 0.0526 (3067.0820)  loss_giou_3_unscaled: 0.1905 (-6557399852548.8623)  cardinality_error_3_unscaled: 1.7500 (2.7574)  loss_ce_4_unscaled: 0.2859 (0.3058)  loss_bbox_4_unscaled: 0.0513 (3067.0867)  loss_giou_4_unscaled: 0.1915 (-464658987657033.3750)  cardinality_error_4_unscaled: 2.2500 (2.7203)  time: 1.7402  data: 1.1582  max mem: 4664
Epoch: [82]  [110/297]  eta: 0:05:26  lr: 0.000000  class_error: 40.00  loss: 7.1070 (-27673241346071028.0000)  loss_ce: 0.2763 (0.3156)  loss_bbox: 0.2721 (13953.9388)  loss_giou: 0.4933 (-26814914651523680.0000)  loss_mask: 0.0656 (0.0633)  loss_dice: 0.6453 (0.6302)  loss_ce_0: 0.4068 (0.4433)  loss_bbox_0: 0.3648 (13953.9331)  loss_giou_0: 0.6131 (-87535475923.7040)  loss_ce_1: 0.3140 (0.3310)  loss_bbox_1: 0.2882 (13953.8980)  loss_giou_1: 0.5233 (-142512593836.5393)  loss_ce_2: 0.2944 (0.3048)  loss_bbox_2: 0.2604 (13953.8733)  loss_giou_2: 0.5119 (-565726452947.7648)  loss_ce_3: 0.3016 (0.2979)  loss_bbox_3: 0.2628 (13953.8664)  loss_giou_3: 0.4777 (-11933286218151.9512)  loss_ce_4: 0.3025 (0.3062)  loss_bbox_4: 0.2566 (13953.8882)  loss_giou_4: 0.4715 (-845595635195682.2500)  loss_ce_unscaled: 0.2763 (0.3156)  class_error_unscaled: 9.0909 (11.0414)  loss_bbox_unscaled: 0.0544 (2790.7877)  loss_giou_unscaled: 0.2466 (-13407457325761840.0000)  cardinality_error_unscaled: 2.7500 (2.7140)  loss_mask_unscaled: 0.0656 (0.0633)  loss_dice_unscaled: 0.6453 (0.6302)  loss_ce_0_unscaled: 0.4068 (0.4433)  loss_bbox_0_unscaled: 0.0730 (2790.7867)  loss_giou_0_unscaled: 0.3066 (-43767737961.8520)  cardinality_error_0_unscaled: 4.5000 (4.3491)  loss_ce_1_unscaled: 0.3140 (0.3310)  loss_bbox_1_unscaled: 0.0576 (2790.7796)  loss_giou_1_unscaled: 0.2617 (-71256296918.2696)  cardinality_error_1_unscaled: 3.2500 (3.0383)  loss_ce_2_unscaled: 0.2944 (0.3048)  loss_bbox_2_unscaled: 0.0521 (2790.7747)  loss_giou_2_unscaled: 0.2560 (-282863226473.8824)  cardinality_error_2_unscaled: 3.2500 (2.8378)  loss_ce_3_unscaled: 0.3016 (0.2979)  loss_bbox_3_unscaled: 0.0526 (2790.7733)  loss_giou_3_unscaled: 0.2389 (-5966643109075.9756)  cardinality_error_3_unscaled: 3.2500 (2.7455)  loss_ce_4_unscaled: 0.3025 (0.3062)  loss_bbox_4_unscaled: 0.0513 (2790.7777)  loss_giou_4_unscaled: 0.2358 (-422797817597841.1250)  cardinality_error_4_unscaled: 3.5000 (2.7252)  time: 1.5251  data: 0.9779  max mem: 4664
 

Training Notebook Link : 
------------------------

https://github.com/Nageswar-Sahoo/Computer-Vision-Project/blob/main/capstrone_3/DETR_Panoptic_Training_From_Scratch.ipynb

# References 
- Official DETR repository (https://github.com/facebookresearch/detr)
- Fine-tunne DETR ( https://github.com/woctezuma/finetune-detr )
- A Github issue regarding training detr on custom data (https://github.com/facebookresearch/detr/issues/9)
- Panoptic API (https://github.com/cocodataset/panopticapi)
                                              
