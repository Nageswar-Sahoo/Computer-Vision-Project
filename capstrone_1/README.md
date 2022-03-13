


                                                   DETR for Panoptic segmentation
                                                   ------------------------------
                                                             
 ![image](https://user-images.githubusercontent.com/70502759/158041859-474702f1-b5e0-4498-abe7-34685cdd8183.png)
 Below are the steps perfoqrmed in DETR for Panoptic segmentation : 
 
 Step  : We take the encoded image (dxH/32xW/32) and send it to Multi-Head Attention
 Step  : We also send dxN Box embeddings to the Multi-Head Attention
 Step  : We do something here to generate NxMxH/32xW/32 maps
 Step  : Then we concatenate these maps with Res5 Block
 Step  : Then we perform the above steps
 Step  : Finally left with the panoptic segmentation




                                                            
