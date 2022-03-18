


                                                   DETR for Object and Bounding Box Detection
                                                   ------------------------------------------
                                                   
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








                                                  
