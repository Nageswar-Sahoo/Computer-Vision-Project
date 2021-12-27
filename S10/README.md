# Assignment - 10 

Part 1
-------

Requirement
Download this TINY IMAGENET dataset.

Train ResNet18 on this dataset (70/30 split) for 50 Epochs. Target 50%+ Validation Accuracy.

Approach
There are 3 main parts to this exercise.

Part -1 Preparing dataset with  70/30 split ratio

Part -2 Updating Resnet18 model to fit the new dataset and 200 classes

Data Overview

![image](https://user-images.githubusercontent.com/70502759/146711043-e37e632f-8252-4666-a9e6-37ae8812d8f6.png)

70/30 split ratio

test data shape:  (30000, 64, 64, 3)

test_labels.shape:  (30000, 200)

train data shape:  (80000, 64, 64, 3)

train label shape:  (80000, 200)

Result
------

The model was trained for 50 epochs -

Highest Training Accuracy achieved - 71

Highest Test Accuracy achieved - 49

![image](https://user-images.githubusercontent.com/70502759/147474410-9f3da5b8-9265-450b-9fb4-34f798b5a368.png)

Few Last Training logs 
----------------------

    epoch          : 43
    loss           : 1.1153605556964874
    accuracy       : 70.62625
    val_loss       : 2.397838760794861
    val_accuracy   : 49.702380952380956


    epoch          : 44
    loss           : 1.104582673740387
    accuracy       : 70.6675
    val_loss       : 2.4913750063381723
    val_accuracy   : 49.29815209665956


    epoch          : 45
    loss           : 1.0976585308551787
    accuracy       : 70.97375
    val_loss       : 2.4062800552290895
    val_accuracy   : 49.594660625444206




    epoch          : 46
    loss           : 1.094077666759491
    accuracy       : 71.13625
    val_loss       : 2.4480305488175675
    val_accuracy   : 49.542466240227434


    epoch          : 47
    loss           : 1.0911674251556396
    accuracy       : 71.07
    val_loss       : 2.489283079277478
    val_accuracy   : 49.51914534470505



    epoch          : 48
    loss           : 1.0941763689517976
    accuracy       : 71.10125
    val_loss       : 2.425588367590264
    val_accuracy   : 49.52136638237384

    
	
	epoch          : 49
    loss           : 1.0872478447437286
    accuracy       : 71.17625
    val_loss       : 2.506463077530932
    val_accuracy   : 49.321472992181945

    loss           : 1.0987044699192048
    accuracy       : 70.91375
    val_loss       : 2.431215469516925
    val_accuracy   : 49.65129708599858



Part 2
------
## Requirement

Download  COCO object detection dataset's schema text file.

Identify the values present in the dataset.

Display class distribution with a graph.

Calculate the Anchor Boxes for k = 3, 4, 5, 6 and draw them.


## Analysis

The anchor boxes or templates are computed using K-means clustering with intersection over union (IOU) as the distance measure. The anchors thus computed do not ignore smaller boxes, and ensure that the resulting anchors ensure high IOU between ground truth boxes.

The coco data set has set of image information like image size (Height and Width), labels(Class - ID) and bonding box(Diagonal co-ordinates). 

There are 79 classes . 



The data set was loaded as a dataframe in a notebook and the bonding box size (Height and Width) was calculated using the diagonal coordinates. The bonding box was then plotted with one corner being (0,0) as a scattered plot.

![image](https://user-images.githubusercontent.com/70502759/146709868-f777b8e9-c41b-46f4-ac72-9b8f3a859608.png)

KMeans clustering algorithm was run on X,Y coordinates to find the optimum number of clusters

![image](https://user-images.githubusercontent.com/70502759/146710015-91a82be8-ab04-4c16-abb8-38408a90b586.png)


Then, for cluster values = 3,4,5,6 the centroids were calculated and anchor boxes were generated.
### For K=3
[150,  45],
[218, 214],
[ 48, 181]
![image](https://user-images.githubusercontent.com/70502759/146710088-ec5223f5-17be-47de-956a-c6c43a9f5a2e.png)


### For K=4

[134,  31],
[204, 261],
[213, 105],
[ 44, 177]
![image](https://user-images.githubusercontent.com/70502759/146710181-e6bca0fb-39d6-4597-9c26-ae25110647e6.png)

### For K=5

[139,  28],
[258, 250],
[211,  94],
[ 30, 153],
[102, 231]

![image](https://user-images.githubusercontent.com/70502759/146710225-c3933cd0-3975-4e87-9b90-70cdf3b428ab.png)

### For K=6

[155,  21],
[247,  97],
[ 94,  88],
[ 93, 244],
[248, 256],
[ 20, 144]

![image](https://user-images.githubusercontent.com/70502759/146710265-98f9e298-8342-48c6-83e6-881dea1cfa7b.png)

### For K=7

[147,  23],
[259, 142],
[192,  72],
[134, 249],
[275, 284],
[ 64, 186],
[ 19, 131]
![image](https://user-images.githubusercontent.com/70502759/146710330-5e6adf81-20c3-45ba-afd1-9a1479cb3ce9.png)

Project template repo link : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/tree/main/template
