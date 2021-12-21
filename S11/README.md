Assignment - 11

Part 1 

Requirement : OpenCV Yolo

1 - Run OpenCV  above code on your laptop or Colab. 

2 - Take an image of yourself, holding another object which is there in COCO data set (search for COCO classes to learn). 

3 - Run this image through the code above. 

4 - Upload the link to GitHub implementation of this

5 - Upload the annotated image by YOLO. 

Annotated image by YOLO



![image](https://user-images.githubusercontent.com/70502759/146763671-73ca19e0-1627-4cea-8898-53c6c096e358.png)
![image](https://user-images.githubusercontent.com/70502759/146763758-d7822744-81d3-49e6-8a36-f988522f559b.png)
![image](https://user-images.githubusercontent.com/70502759/146763799-b090a263-2c9d-4ddf-9480-b5e4bd509250.png)
![image](https://user-images.githubusercontent.com/70502759/146763844-cd398b2b-ba2a-4a29-a7a1-3355de260e0d.png)


OpenCV GitHub implementation : 

https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/



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


Annotated image for custom image collected  :



Vest



![beautiful-construction-worker-girl-buttoning-her-protection-vest-before-M53KGD](https://user-images.githubusercontent.com/70502759/146811155-dd45f831-a575-4ce0-92ec-f0d6b5c717a4.jpg)
![confident-construction-worker-white-helmet-yellow-safety-vest-standing-hands-crossed-over-blue-background-155708353](https://user-images.githubusercontent.com/70502759/146811179-5402cb25-160b-40bc-821c-738e3ec7d1bd.jpg)
![construction-worker-green-safety-vest-1967057](https://user-images.githubusercontent.com/70502759/146811213-0d6dfa82-d093-4468-9497-d162ea93a18e.jpg)
![depositphotos_265381370-stock-photo-serious-construction-worker-safety-vest](https://user-images.githubusercontent.com/70502759/146811241-9ab5e71c-e825-4b7d-917f-81655cbd3064.jpg)
![factory-worker-wearing-uniform-hardhat-operating-industrial-machine-with-push-button-joystick-production-hall_342744-214](https://user-images.githubusercontent.com/70502759/146811273-89fef0ef-501e-456d-9b71-ed384463e034.jpg)
![focused_173619994-stock-photo-construction-worker-construction-site-wearing](https://user-images.githubusercontent.com/70502759/146811302-d325c15b-d5d6-4dc0-93dd-7ec8526b4350.jpg)
![istockphoto-498553469-612x612](https://user-images.githubusercontent.com/70502759/146811357-6d05b940-157a-4c74-b893-1f70547bf0e4.jpg)
![H4bc752a5cd5c4c70845b47968e912b9fB](https://user-images.githubusercontent.com/70502759/146811319-7e31b5c8-4d30-42e9-8900-253e59b40635.jpg)



Mask 



![41b6oNz1h6L](https://user-images.githubusercontent.com/70502759/146812374-9ca60578-6148-450a-b5ba-92f86d6faa05.jpg)
![b23587f1e3b87e780205a8b94b9d30a19c](https://user-images.githubusercontent.com/70502759/146812443-0b92ca71-0f9f-43bd-ae0d-9714ce5b15ce.jpg)
![survey-says-90-indians-aware-but-only-44-wearing-a-mask-discomfort-key-reason-for-non-compliance](https://user-images.githubusercontent.com/70502759/146812506-26d7f2b2-84be-4f09-a547-fdd4e4c9ef02.jpg)
![xU94NDWTKt7HfSZHdeY3Rn-1200-80](https://user-images.githubusercontent.com/70502759/146812524-3265b186-7461-4bd8-bf17-ab5059a8b1d8.jpg)
![s75-jir-0335-eye_1](https://user-images.githubusercontent.com/70502759/146814781-14e09e05-c0ad-41ef-ace3-bf6ba4c07f34.jpg)
![PPE-100_1](https://user-images.githubusercontent.com/70502759/146814805-1f64c3e6-de97-4069-94c1-34effdde3c3f.jpg)




HardHat



![3d03b888bca2460a278c7f895aa22bb5](https://user-images.githubusercontent.com/70502759/146812111-555632d4-83d7-47e1-a705-eb1ad07ccf1c.jpg)
![60901_app2](https://user-images.githubusercontent.com/70502759/146812139-1560b7c9-4456-4c03-8ccb-3c3bc155c406.jpg)
![helmet tmb-th600hq](https://user-images.githubusercontent.com/70502759/146812177-a85fb7d2-65b5-4b6b-8381-ac77c509351b.jpg)
![How-to-Adjust-Hard-Hat-Height](https://user-images.githubusercontent.com/70502759/146812208-9141ec9b-a9d0-480b-abdf-641f1615f245.jpg)
![poll2-1](https://user-images.githubusercontent.com/70502759/146812247-4765a502-bd08-41b3-99a5-fcea14cda574.jpg)
![white-plastic-safety-helmet-isolated-260nw-1905566200](https://user-images.githubusercontent.com/70502759/146812266-be9a239e-a46d-410b-bc0d-ff1e6750b9ea.jpg)




Boot 



![12_m_boots_520x650](https://user-images.githubusercontent.com/70502759/146811864-ec511051-0a89-4144-84bf-050b18f04d7b.jpg)
![5400_12_0 20210906000243](https://user-images.githubusercontent.com/70502759/146811903-3eafabff-490d-4f94-a2e8-3a61f5cf8d14.jpg)
![boots-women-water-resistant-photo](https://user-images.githubusercontent.com/70502759/146811939-21350224-2e3c-49d8-afb2-b8445846166a.jpg)
![BR00288-300x300](https://user-images.githubusercontent.com/70502759/146811952-1eee9c2e-54da-4947-a7e6-0d624ebea048.jpg)
![elegant-outfit-closeup-stylish-boots-260nw-1373562521](https://user-images.githubusercontent.com/70502759/146811990-8b9827d9-8f8b-42bb-9b66-be238a7a101a.jpg)
![men-fashion-brown-leather-boots-260nw-314506853](https://user-images.githubusercontent.com/70502759/146812008-f973cd0f-b5c9-4d2d-bdd8-1991378dedbd.jpg)
![men-fashion-leather-boots-close-260nw-526165960](https://user-images.githubusercontent.com/70502759/146812023-8d72e492-2773-4f50-b28b-082c51f33692.jpg)
![mens-boots-black-combat-shoes-260nw-1920418622](https://user-images.githubusercontent.com/70502759/146812048-94b944f5-1c86-48af-9c8b-f05d2f564fd9.jpg)


Annotated Video by YOLO

https://youtu.be/V058NjF4usA

https://youtu.be/A5RssWTyJn4


OpenCV GitHub implementation : 

https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/



