


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
 
        Multi Head Attention Map will take input of transformer decoder last layer output and encoder encoded image output .
	Transformer decoder last layer output behaves as query and encoder output behaves as key . 
	Then we calculate a self-attention score. The score is calculated by taking the dot product of the query vector with the key vector.           
	The score determines how much focus to place on other parts of the input image at a certain position 
	and Multi Head Attention Map module only returns the attention softmax
	
	  Details coding done in Multi Head Attention Map : 
	  
	  
	def forward(self, q, k, mask: Optional[Tensor] = None):
           
	   q = self.q_linear(q)
	   
           k = F.conv2d(k, self.k_linear.weight.unsqueeze(-1).unsqueeze(-1), self.k_linear.bias)
	   
           #qh 2 100 8 32
           #kh 2 8 32 24 32
           qh = q.view(q.shape[0], q.shape[1], self.num_heads, self.hidden_dim // self.num_heads)
	   
           kh = k.view(k.shape[0], self.num_heads, self.hidden_dim // self.num_heads, k.shape[-2], k.shape[-1])
	   
           #weight 2 100 8 24 32
           weights = torch.einsum("bqnc,bnchw->bqnhw", qh * self.normalize_fact, kh)

           if mask is not None:
              weights.masked_fill_(mask.unsqueeze(1).unsqueeze(1), float("-inf"))
	      
           weights = F.softmax(weights.flatten(2), dim=-1).view(weights.size())
	   
           weights = self.dropout(weights)
	   
           #2 100 8 24 32
           return weights
 
 Step  : Then we concatenate these maps with Res5 Block
 
 Step  : Then we perform the above steps
 
 Step  : Finally left with the panoptic segmentation




                                                            
