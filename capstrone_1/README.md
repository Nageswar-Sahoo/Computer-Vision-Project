


                                                   DETR for Panoptic segmentation
                                                   ------------------------------
                                                             
 ![image](https://user-images.githubusercontent.com/70502759/158041859-474702f1-b5e0-4498-abe7-34685cdd8183.png)
 
 Below are the steps perfoqrmed in DETR for Panoptic segmentation : 
 
 
 
 Assuming we have sample image of batch 2 with shape : [batch = 2 , channel = 3 , hight = 768 , width = 1023 ]
 
 step  :  Detr architecture  
 
          we know that the backbone upon accepting an input of above shape  returns out and pos, 
	    where output has intermediate layer  tensors  and positional encoding of following shape 

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
       
         Backbone last layer o/p again pass throw convolution network and 
         project back in to  Size of the embeddings (dimension as required by the transformer)

          i/p  shape      : tensors shape : [batch = 2, channel = 2048, hight = 28, width = 34] 
          projected shape : tensors shape : [batch = 2, channel = 256, hight = 28, width = 34] 
	  
	  These project back embeddings along with positional embedding passed to transformer architecture .
	  Transformer will return output from encoder as encoded image (called as memory ) 
	  and N object queries are transformed into an output embedding by the decoder . 
	  
	  Hence encoded image is the output of transformer encoder of following shape and   is passed to Multi-Head Attention 
	      tensors shape : [batch = 2, embeding vector(d) :256, hight(H) = 28, width(N) = 34]
	        


        
        

 Step  : We also send dxN Box embeddings to the Multi-Head Attention
 
       N object queries are transformed into an output embedding by the decoder of shape and is passed to Multi-Head Attention
         tensors shape : [number of intermediate layer  = 6, batch = 2, object queries zize(N) = 100, embeding vector(d) : 256]

 Step  : We do something here to generate NxMxH/32xW/32 maps
 
 Step  : Then we concatenate these maps with Res5 Block
 
 Step  : Then we perform the above steps
 
 Step  : Finally left with the panoptic segmentation




                                                            
