Assignment 11

Part 1 

Requirement : OpenCV Yolo

1 - Run OpenCV  above code on your laptop or Colab. 

2 - Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 

3 - Run this image through the code above. 

4 - Upload the link to GitHub implementation of this

5 - Upload the annotated image by YOLO. 


![image](https://user-images.githubusercontent.com/70502759/146763671-73ca19e0-1627-4cea-8898-53c6c096e358.png)
![image](https://user-images.githubusercontent.com/70502759/146763758-d7822744-81d3-49e6-8a36-f988522f559b.png)
![image](https://user-images.githubusercontent.com/70502759/146763799-b090a263-2c9d-4ddf-9480-b5e4bd509250.png)
![image](https://user-images.githubusercontent.com/70502759/146763844-cd398b2b-ba2a-4a29-a7a1-3355de260e0d.png)


OpenCV GitHub implementation : 

https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/

Annotated image by YOLO


Part 2 

Requirement : Training Custom Dataset on Colab for YoloV3

1 - Refer to this Colab File:  https://colab.research.google.com/drive/1LbKkQf4hbIuiUHunLlvY-cc0d_sNcAgS#scrollTo=ElYu4RG01NVw

2 - Refer to this GitHub  https://github.com/theschoolofai/YoloV3

3 - Download dataset from web having class -  hardhat vest mask boots

4 - you must follow exact rules to make sure that you can train the model. Steps are explained in the README.md file on github repo link above.

5 - Once you add your additional 100 images, train the model

6 - Download a very small (~10-30sec) video from youtube which shows your classes. 

7 - Use ffmpeg to extract frames from the video. 

8 - Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)

9 -  Infer on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 
     python detect.py --conf-three 0.3 --output output_folder_name
     
10 - Use  ffmpeg  to convert the files in your output folder to video

11 - Upload the video to YouTube. 

12 - Also run the model on 16 images that you have collected (4 for each class)

Vest

![beautiful-construction-worker-girl-buttoning-her-protection-vest-before-M53KGD](https://user-images.githubusercontent.com/70502759/146811155-dd45f831-a575-4ce0-92ec-f0d6b5c717a4.jpg)
![confident-construction-worker-white-helmet-yellow-safety-vest-standing-hands-crossed-over-blue-background-155708353](https://user-images.githubusercontent.com/70502759/146811179-5402cb25-160b-40bc-821c-738e3ec7d1bd.jpg)
![construction-worker-green-safety-vest-1967057](https://user-images.githubusercontent.com/70502759/146811213-0d6dfa82-d093-4468-9497-d162ea93a18e.jpg)
![depositphotos_265381370-stock-photo-serious-construction-worker-safety-vest](https://user-images.githubusercontent.com/70502759/146811241-9ab5e71c-e825-4b7d-917f-81655cbd3064.jpg)
![factory-worker-wearing-uniform-hardhat-operating-industrial-machine-with-push-button-joystick-production-hall_342744-214](https://user-images.githubusercontent.com/70502759/146811273-89fef0ef-501e-456d-9b71-ed384463e034.jpg)
![focused_173619994-stock-photo-construction-worker-construction-site-wearing](https://user-images.githubusercontent.com/70502759/146811302-d325c15b-d5d6-4dc0-93dd-7ec8526b4350.jpg)
![istockphoto-498553469-612x612](https://user-images.githubusercontent.com/70502759/146811357-6d05b940-157a-4c74-b893-1f70547bf0e4.jpg)
![H4bc752a5cd5c4c70845b47968e912b9fB](https://user-images.githubusercontent.com/70502759/146811319-7e31b5c8-4d30-42e9-8900-253e59b40635.jpg)




OpenCV GitHub implementation : 

https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/

Annotated image by YOLO
Annotated Video by YOLO


