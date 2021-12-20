# Session - 10 Assignment -B




Part 2
## Requirement

Download  COCO object detection dataset's schema text file.

Identify the values present in the dataset.

Display class distribution with a graph.

Calculate the Anchor Boxes for k = 3, 4, 5, 6 and draw them.


## Analysis

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

