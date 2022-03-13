


                                                   DETR for Panoptic segmentation
                                                   ------------------------------
                                                             
 ![image](https://user-images.githubusercontent.com/70502759/158041859-474702f1-b5e0-4498-abe7-34685cdd8183.png)
 
 Below are the steps perfoqrmed in DETR for Panoptic segmentation : 
 
 
 
 Assuming we have sample image of batch 2 with shape : [batch = 2 , channel = 3 , hight = 768 , width = 1023 ]
 
 step 1  :  BackBone in DETR architecture  
 
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

                    
 
 Step 2 : We take the encoded image (dxH/32xW/32) and send it to Multi-Head Attention
       
         Backbone last layer o/p again pass throw convolution network and 
         project back in to  Size of the embeddings (dimension as required by the transformer)

          i/p  shape      : tensors shape : [batch = 2, channel = 2048, hight = 28, width = 34] 
          projected shape : tensors shape : [batch = 2, channel = 256, hight = 28, width = 34] 
	  
	  These project back embeddings along with positional embedding passed to transformer architecture .
	  Transformer will return output from encoder as encoded image (called as memory ) 
	  and N object queries are transformed into an output embedding by the decoder . 
	  
	  Hence encoded image is the output of transformer encoder of following shape and   is passed to Multi-Head Attention 
	      tensors shape : [batch = 2, embeding vector(d) :256, hight(H) = 28, width(N) = 34]
	        


        
        

 Step 3 : We also send dxN Box embeddings to the Multi-Head Attention
 
       N object queries are transformed into an output embedding by the decoder of shape and is passed to Multi-Head Attention
         tensors shape : [number of intermediate layer  = 6, batch = 2, object queries zize(N) = 100, embeding vector(d) : 256]

 Step 4 : We do something here to generate NxMxH/32xW/32 maps
 
        Multi Head Attention Map will take input of transformer decoder last layer output and encoder encoded image output .
	Transformer decoder last layer output behaves as query and encoder output behaves as key . 
	Then we calculate a self-attention score. The score is calculated by taking the dot 
	product of the query vector with the key vector. 
	The score determines how much focus to place on other parts of the input image at a certain position 
	and Multi Head Attention Map module only returns the attention softmax
	
	  Details coding done in Multi Head Attention Map : 
	  
	  
	 def forward(self, q, k, mask: Optional[Tensor] = None):  # q = [2 100 256 ] k = [2 256 24 32]  mask = [2 24 32]
	 
           q = self.q_linear(q)  # q will be projected
	   
           k = F.conv2d(k, self.k_linear.weight.unsqueeze(-1).unsqueeze(-1), self.k_linear.bias)  # k will be projected
	    
           qh = q.view(q.shape[0], q.shape[1], self.num_heads, self.hidden_dim // self.num_heads)	   
           # qq rehsape based on number of heads to optimize the matrix multiplication qh = [2 100 8 32]
	  
           kh = k.view(k.shape[0], self.num_heads, self.hidden_dim // self.num_heads, k.shape[-2], k.shape[-1])
           # kh rehsape based on number of heads to optimize the matrix multiplication  kh [2 8 32 24 32]

           weights = torch.einsum("bqnc,bnchw->bqnhw", qh * self.normalize_fact, kh)  # self attention weight = [2 100 8 24 32 ]

           if mask is not None:
              weights.masked_fill_(mask.unsqueeze(1).unsqueeze(1), float("-inf"))

           weights = F.softmax(weights.flatten(2), dim=-1).view(weights.size())  # attention softmax 

           weights = self.dropout(weights)  # dropout

           return weights  # Batch N = 2 Object Query M = 100 No of Head= 8 Hight = 24 width = 32
	   

![Capture_4](https://user-images.githubusercontent.com/70502759/158050222-87865ae1-a803-4364-9115-c25a4753deba.PNG)

 
 Step 5 : Then we concatenate these maps with Res5 Block
         
	 
	 Attention map from step 4 and resnet BackBone block from step 1 will concatenate and will do upsampling  using a FPN approach . 
	 
![Capture_1](https://user-images.githubusercontent.com/70502759/158048086-61efa3ba-525f-4f70-80f5-c7848a3ccf70.PNG)

	 
	 
 
 Step  : Then we perform the below steps
 
         We filter the predictions for which the confidence is less then certain threshold .
         Finally, the remaining masks are merged together using a pixel-wise argmax . 
	 

	 
![Capture_3](https://user-images.githubusercontent.com/70502759/158048064-107b938c-a5bd-46c9-b326-dcedcb0e3e86.PNG)

 
 Step  : Finally left with the panoptic segmentation




                                                            
