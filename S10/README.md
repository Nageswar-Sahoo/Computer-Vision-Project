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

The model was trained for 50 epochs -

Highest Training Accuracy achieved - 71

Highest Test Accuracy achieved - 49

![image](https://user-images.githubusercontent.com/70502759/147474410-9f3da5b8-9265-450b-9fb4-34f798b5a368.png)

Few Last Training logs 
----------------------

<utils.util.MetricTracker object at 0x7f212618bd90>

    epoch          : 47
    loss           : 0.8187679586172104
    accuracy       : 77.33625
    val_loss       : 2.7356374886498522
    val_accuracy   : 47.70455756929638


    epoch          : 48
    loss           : 0.7877105013370513
    accuracy       : 78.11375
    val_loss       : 2.720578250600331
    val_accuracy   : 48.51301528073916


    epoch          : 49
    loss           : 0.7713985350131989
    accuracy       : 78.49875
    val_loss       : 2.751128341343357
    val_accuracy   : 48.165422885572134


    epoch          : 50
    loss           : 0.758125228881836
    accuracy       : 78.85
    val_loss       : 2.8003420392587497
    val_accuracy   : 47.90000888415068



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
