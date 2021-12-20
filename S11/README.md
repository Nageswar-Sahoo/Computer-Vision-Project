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

OpenCV GitHub implementation : 

https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/

Annotated image by YOLO
Annotated Video by YOLO


