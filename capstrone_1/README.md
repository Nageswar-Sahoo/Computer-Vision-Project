


                                                   DETR for Panoptic segmentation
                                                   ------------------------------
                                                             
 ![image](https://user-images.githubusercontent.com/70502759/158041859-474702f1-b5e0-4498-abe7-34685cdd8183.png)
 
 Below are the steps perfoqrmed in DETR for Panoptic segmentation : 
 
 
 
 Assuming we have sample image of batch 2 with shape : [batch = 2 , channel = 3 , hight = 768 , width = 1023 ]
 
 step  :  Backbone architecture return 
 
          we know that the backbone upon accepting an input of above shape  returns out and pos, where output has intermediate layer  tensors  and positional encoding of                   following shape 

         layer 0 :  tensors shape : [batch = 2, channel = 256, hight = 219, width = 265] 
                    mask shape    : [batch = 2,  hight = 219, width = 265 ]
		                pos encoding  : [batch = 2, channel = 256, hight = 219, width = 265] 
		   

         layer 1 :  tensors shape : [batch = 2, channel = 512, hight = 110, width = 113] 
                    mask shape    : [batch = 2,  hight = 110, width = 113 ]
		                pos encoding  : [batch = 2, channel = 256, hight = 110, width = 113] 
		   
         layer 2 :  tensors shape : [batch = 2, channel = 1024, hight = 55, width = 67] 
                    mask shape    : [batch = 2,  hight = 55, width = 67 ]
		                pos encoding  : [batch = 2, channel = 256, hight = 55, width = 67] 



         layer 3 :  tensors shape : [batch = 2, channel = 2048, hight = 28, width = 34] 
                    mask shape    : [batch = 2,  hight = 28, width = 34 ]
		                pos encoding  : [batch = 2, channel = 256, hight = 28, width = 34] 
                    
 
 Step  : We take the encoded image (dxH/32xW/32) and send it to Multi-Head Attention
        

 Step  : We also send dxN Box embeddings to the Multi-Head Attention

 Step  : We do something here to generate NxMxH/32xW/32 maps
 
 Step  : Then we concatenate these maps with Res5 Block
 
 Step  : Then we perform the above steps
 
 Step  : Finally left with the panoptic segmentation




                                                            
