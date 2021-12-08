Design Nenural newtwork architecture with following constarint :

We will be exploring the custom resnet architecture .
![customresnetdesign](https://user-images.githubusercontent.com/70502759/143819267-e474ae39-5dd5-418d-985b-1a5104ecbd49.PNG)


Data Overview

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

Here are the classes in the dataset, as well as 10 random images from each:
![image](https://user-images.githubusercontent.com/70502759/141685528-79bce9e3-7de7-4613-8beb-b13d1e59d79d.png)

Custom Resnet Model Overview : 

      
         Layer (type)               Output Shape         Param #
            Conv2d-1           [-1, 64, 32, 32]           1,728
       BatchNorm2d-2           [-1, 64, 32, 32]             128
              ReLU-3           [-1, 64, 32, 32]               0
            Conv2d-4          [-1, 128, 32, 32]          73,728
         MaxPool2d-5          [-1, 128, 16, 16]               0
       BatchNorm2d-6          [-1, 128, 16, 16]             256
              ReLU-7          [-1, 128, 16, 16]               0
            Conv2d-8          [-1, 128, 16, 16]         147,456
       BatchNorm2d-9          [-1, 128, 16, 16]             256
             ReLU-10          [-1, 128, 16, 16]               0
           Conv2d-11          [-1, 128, 16, 16]         147,456
      BatchNorm2d-12          [-1, 128, 16, 16]             256
             ReLU-13          [-1, 128, 16, 16]               0
             ReLU-14          [-1, 128, 16, 16]               0
    ResidualBlock-15          [-1, 128, 16, 16]               0
           Conv2d-16          [-1, 256, 16, 16]         294,912
        MaxPool2d-17            [-1, 256, 8, 8]               0
      BatchNorm2d-18            [-1, 256, 8, 8]             512
             ReLU-19            [-1, 256, 8, 8]               0
           Conv2d-20            [-1, 512, 8, 8]       1,179,648
        MaxPool2d-21            [-1, 512, 4, 4]               0
      BatchNorm2d-22            [-1, 512, 4, 4]           1,024
             ReLU-23            [-1, 512, 4, 4]               0
           Conv2d-24            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-25            [-1, 512, 4, 4]           1,024
             ReLU-26            [-1, 512, 4, 4]               0
           Conv2d-27            [-1, 512, 4, 4]       2,359,296
      BatchNorm2d-28            [-1, 512, 4, 4]           1,024
             ReLU-29            [-1, 512, 4, 4]               0
             ReLU-30            [-1, 512, 4, 4]               0
    ResidualBlock-31            [-1, 512, 4, 4]               0
        AvgPool2d-32            [-1, 512, 1, 1]               0
           Linear-33                   [-1, 10]           5,130
    Total params: 6,573,130
    Trainable params: 6,573,130
    Non-trainable params: 0

    Input size (MB): 0.01
    Forward/backward pass size (MB): 7.07
    Params size (MB): 25.07
    Estimated Total Size (MB): 32.15

Best LR Finder test for 24 Epoch : 

![LR_Test](https://user-images.githubusercontent.com/70502759/144747966-fc3416e1-31aa-4032-9755-4eee2864149f.PNG)

We have used LR finder to find the max_lr and min_lr. As per the range test for 24 epochs  suggested max_lr=.74 and min_lr=.074 (1/10th of max_lr).
While training with this max_lr with OneCycleLR , google colab is crashing and hence we have trained the model with a much lower learning rate .We are able to train the model with OneCycleLR  where  max_lr=.03.


   
Result

The model was trained for 24 epochs -

Highest Training Accuracy achieved - 92.13%

Highest Test Accuracy achieved - 92.01%

![image](https://user-images.githubusercontent.com/70502759/144750462-70a63b99-6cb5-42b0-9f3b-852f2a923967.png)

Misclassified and GradCam Images Gallery

Misclassified images were generated and for each misclassified image a gradcam image was generated for the misclassified class the model predicted.


![image](https://user-images.githubusercontent.com/70502759/144750833-5887da41-3d00-4eaa-8d2f-3bac2d70ccb0.png)
![image](https://user-images.githubusercontent.com/70502759/144750838-d795c34f-8590-4de3-9fba-ee4ed620d2e5.png)
![image](https://user-images.githubusercontent.com/70502759/144750844-e68b89d1-9776-47a6-be81-9efa55111ca7.png)
![image](https://user-images.githubusercontent.com/70502759/144750854-d32b9b2e-2369-4fce-9608-505738652bc5.png)
![image](https://user-images.githubusercontent.com/70502759/144750856-ab330c0a-94f7-4efc-9bc1-dcd79ef1de47.png)
![image](https://user-images.githubusercontent.com/70502759/144750861-4cda47d5-7829-436b-bee4-7d8a0f277627.png)
![image](https://user-images.githubusercontent.com/70502759/144750868-bf58d25f-16b3-43af-ba3d-ef7e106efc1b.png)
![image](https://user-images.githubusercontent.com/70502759/144750873-23fd16bd-9ae7-4737-8040-752754615c00.png)
![image](https://user-images.githubusercontent.com/70502759/144750874-54e896fc-4195-4f37-8661-7b2b272c25d1.png)
![image](https://user-images.githubusercontent.com/70502759/144750878-a904a374-4d38-43a6-8264-a9d6124316a7.png)
![image](https://user-images.githubusercontent.com/70502759/144750884-1191ccd3-0d26-41dd-b922-8ddcd4931314.png)
![image](https://user-images.githubusercontent.com/70502759/144750895-13b1c01d-a895-4fca-a15d-537f23c5cf28.png)
![image](https://user-images.githubusercontent.com/70502759/144750899-e3026fb8-ccac-4dc5-968a-5aebaf000faf.png)
![image](https://user-images.githubusercontent.com/70502759/144750908-3517ba1c-bbd4-4997-a0e7-0147616f8766.png)
![image](https://user-images.githubusercontent.com/70502759/144750911-97347a52-7d53-46db-9abe-820c7a7aa576.png)
![image](https://user-images.githubusercontent.com/70502759/144750927-d33bc7e4-c331-4d79-81d2-1ca0105e8a47.png)
![image](https://user-images.githubusercontent.com/70502759/144750931-47408f19-c785-4d77-92ba-aa0228a97c59.png)
![image](https://user-images.githubusercontent.com/70502759/144750939-8e0c9c8a-2918-406e-ae6c-dd80f689362b.png)
![image](https://user-images.githubusercontent.com/70502759/144750944-f9994bd4-443f-4498-bcd8-f86b21a26be6.png)
![image](https://user-images.githubusercontent.com/70502759/144750950-66065d8a-1962-45cf-a708-e814093eeab1.png)



 Training logs

      Train Epoch: 1 last_lr_used  0.001200  [0/98 (0%)] Loss: 3.728552
      Train Epoch: 1 last_lr_used  0.001357  [22/98 (22%)] Loss: 1.793159
      Train Epoch: 1 last_lr_used  0.001798  [44/98 (45%)] Loss: 1.742687
      Train Epoch: 1 last_lr_used  0.002514  [66/98 (67%)] Loss: 1.510625
      Train Epoch: 1 last_lr_used  0.003490  [88/98 (90%)] Loss: 1.487778
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 1
    loss           : 1.7804641577662255
    accuracy       : 36.328599520165206
    val_loss       : 1.3241092622280122
    val_accuracy   : 51.97552849264706
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch1.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 2 last_lr_used  0.004016  [0/98 (0%)] Loss: 1.451329
      Train Epoch: 2 last_lr_used  0.005336  [22/98 (22%)] Loss: 1.385200
      Train Epoch: 2 last_lr_used  0.006861  [44/98 (45%)] Loss: 1.240560
      Train Epoch: 2 last_lr_used  0.008561  [66/98 (67%)] Loss: 1.364700
      Train Epoch: 2 last_lr_used  0.010401  [88/98 (90%)] Loss: 1.164342
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 2
    loss           : 1.3283881374767847
    accuracy       : 52.43798970481049
    val_loss       : 1.862415510416031
    val_accuracy   : 49.54446231617647
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch2.pth ...
      Train Epoch: 3 last_lr_used  0.011274  [0/98 (0%)] Loss: 1.456654
      Train Epoch: 3 last_lr_used  0.013251  [22/98 (22%)] Loss: 1.324485
      Train Epoch: 3 last_lr_used  0.015276  [44/98 (45%)] Loss: 1.271581
      Train Epoch: 3 last_lr_used  0.017307  [66/98 (67%)] Loss: 1.243608
      Train Epoch: 3 last_lr_used  0.019305  [88/98 (90%)] Loss: 1.054886
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 3
    loss           : 1.1941001208461062
    accuracy       : 58.38761844023323
    val_loss       : 0.9247550874948501
    val_accuracy   : 67.67118566176471
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch3.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 4 last_lr_used  0.020190  [0/98 (0%)] Loss: 1.026140
      Train Epoch: 4 last_lr_used  0.022067  [22/98 (22%)] Loss: 1.641917
      Train Epoch: 4 last_lr_used  0.023815  [44/98 (45%)] Loss: 0.929765
      Train Epoch: 4 last_lr_used  0.025399  [66/98 (67%)] Loss: 0.851770
      Train Epoch: 4 last_lr_used  0.026788  [88/98 (90%)] Loss: 0.871289
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 4
    loss           : 1.02813913931652
    accuracy       : 64.59766384232265
    val_loss       : 0.8412173002958298
    val_accuracy   : 70.78871783088235
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch4.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 5 last_lr_used  0.027347  [0/98 (0%)] Loss: 0.882325
      Train Epoch: 5 last_lr_used  0.028403  [22/98 (22%)] Loss: 0.865599
      Train Epoch: 5 last_lr_used  0.029204  [44/98 (45%)] Loss: 0.893403
      Train Epoch: 5 last_lr_used  0.029733  [66/98 (67%)] Loss: 0.956922
      Train Epoch: 5 last_lr_used  0.029981  [88/98 (90%)] Loss: 0.892980
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 5
    loss           : 0.8990234221730914
    accuracy       : 68.47544263241011
    val_loss       : 0.856960442662239
    val_accuracy   : 71.15808823529412
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch5.pth ...
      Train Epoch: 6 last_lr_used  0.029999  [0/98 (0%)] Loss: 0.874350
      Train Epoch: 6 last_lr_used  0.029829  [22/98 (22%)] Loss: 0.844554
      Train Epoch: 6 last_lr_used  0.029376  [44/98 (45%)] Loss: 0.794786
      Train Epoch: 6 last_lr_used  0.028648  [66/98 (67%)] Loss: 0.772604
      Train Epoch: 6 last_lr_used  0.027659  [88/98 (90%)] Loss: 0.803088
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 6
    loss           : 0.8420161969807683
    accuracy       : 70.30756499028183
    val_loss       : 0.7795752197504043
    val_accuracy   : 73.04400275735294
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch6.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 7 last_lr_used  0.027129  [0/98 (0%)] Loss: 0.880048
      Train Epoch: 7 last_lr_used  0.025799  [22/98 (22%)] Loss: 0.746284
      Train Epoch: 7 last_lr_used  0.024265  [44/98 (45%)] Loss: 0.789879
      Train Epoch: 7 last_lr_used  0.022558  [66/98 (67%)] Loss: 0.719213
      Train Epoch: 7 last_lr_used  0.020713  [88/98 (90%)] Loss: 0.712782
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 7
    loss           : 0.7690477097521022
    accuracy       : 73.12327274659864
    val_loss       : 0.668506070971489
    val_accuracy   : 77.35696231617648
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch7.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 8 last_lr_used  0.019838  [0/98 (0%)] Loss: 0.612384
      Train Epoch: 8 last_lr_used  0.017857  [22/98 (22%)] Loss: 0.729092
      Train Epoch: 8 last_lr_used  0.015831  [44/98 (45%)] Loss: 0.622342
      Train Epoch: 8 last_lr_used  0.013801  [66/98 (67%)] Loss: 0.657957
      Train Epoch: 8 last_lr_used  0.011806  [88/98 (90%)] Loss: 0.705383
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 8
    loss           : 0.6702599634929579
    accuracy       : 76.55671085398446
    val_loss       : 0.5842037558555603
    val_accuracy   : 79.76102941176471
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch8.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 9 last_lr_used  0.010922  [0/98 (0%)] Loss: 0.754458
      Train Epoch: 9 last_lr_used  0.009050  [22/98 (22%)] Loss: 0.601969
      Train Epoch: 9 last_lr_used  0.007309  [44/98 (45%)] Loss: 0.487170
      Train Epoch: 9 last_lr_used  0.005733  [66/98 (67%)] Loss: 0.527301
      Train Epoch: 9 last_lr_used  0.004354  [88/98 (90%)] Loss: 0.545106
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 9
    loss           : 0.5731438869724468
    accuracy       : 80.04082771501457
    val_loss       : 0.4129775524139404
    val_accuracy   : 85.96852022058823
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch9.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 10 last_lr_used  0.003800  [0/98 (0%)] Loss: 0.450548
      Train Epoch: 10 last_lr_used  0.002755  [22/98 (22%)] Loss: 0.469122
      Train Epoch: 10 last_lr_used  0.001966  [44/98 (45%)] Loss: 0.479432
      Train Epoch: 10 last_lr_used  0.001449  [66/98 (67%)] Loss: 0.409083
      Train Epoch: 10 last_lr_used  0.001215  [88/98 (90%)] Loss: 0.427380
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 10
    loss           : 0.4550883523663696
    accuracy       : 84.22998663751216
    val_loss       : 0.3462504416704178
    val_accuracy   : 88.08421415441177
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch10.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 11 last_lr_used  0.001200  [0/98 (0%)] Loss: 0.472156
      Train Epoch: 11 last_lr_used  0.001199  [22/98 (22%)] Loss: 0.473796
      Train Epoch: 11 last_lr_used  0.001197  [44/98 (45%)] Loss: 0.434031
      Train Epoch: 11 last_lr_used  0.001193  [66/98 (67%)] Loss: 0.453792
      Train Epoch: 11 last_lr_used  0.001187  [88/98 (90%)] Loss: 0.404492
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 11
    loss           : 0.405471530799963
    accuracy       : 85.86603726311952
    val_loss       : 0.3197011351585388
    val_accuracy   : 88.93095128676471
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch11.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 12 last_lr_used  0.001184  [0/98 (0%)] Loss: 0.349010
      Train Epoch: 12 last_lr_used  0.001176  [22/98 (22%)] Loss: 0.332628
      Train Epoch: 12 last_lr_used  0.001167  [44/98 (45%)] Loss: 0.366925
      Train Epoch: 12 last_lr_used  0.001157  [66/98 (67%)] Loss: 0.322545
      Train Epoch: 12 last_lr_used  0.001145  [88/98 (90%)] Loss: 0.374609
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 12
    loss           : 0.3844111090411945
    accuracy       : 86.57544491010691
    val_loss       : 0.3136764168739319
    val_accuracy   : 89.60592830882352
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch12.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 13 last_lr_used  0.001139  [0/98 (0%)] Loss: 0.374474
      Train Epoch: 13 last_lr_used  0.001125  [22/98 (22%)] Loss: 0.370796
      Train Epoch: 13 last_lr_used  0.001110  [44/98 (45%)] Loss: 0.379688
      Train Epoch: 13 last_lr_used  0.001093  [66/98 (67%)] Loss: 0.358563
      Train Epoch: 13 last_lr_used  0.001075  [88/98 (90%)] Loss: 0.340647
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 13
    loss           : 0.3650070364986147
    accuracy       : 87.33410775024295
    val_loss       : 0.3018879473209381
    val_accuracy   : 89.62201286764706
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch13.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 14 last_lr_used  0.001067  [0/98 (0%)] Loss: 0.358460
      Train Epoch: 14 last_lr_used  0.001047  [22/98 (22%)] Loss: 0.310471
      Train Epoch: 14 last_lr_used  0.001026  [44/98 (45%)] Loss: 0.351150
      Train Epoch: 14 last_lr_used  0.001005  [66/98 (67%)] Loss: 0.320763
      Train Epoch: 14 last_lr_used  0.000982  [88/98 (90%)] Loss: 0.353160
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 14
    loss           : 0.35480344751659704
    accuracy       : 87.62755102040816
    val_loss       : 0.29937132596969607
    val_accuracy   : 89.97874540441177
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch14.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 15 last_lr_used  0.000971  [0/98 (0%)] Loss: 0.425660
      Train Epoch: 15 last_lr_used  0.000947  [22/98 (22%)] Loss: 0.347531
      Train Epoch: 15 last_lr_used  0.000922  [44/98 (45%)] Loss: 0.330282
      Train Epoch: 15 last_lr_used  0.000896  [66/98 (67%)] Loss: 0.348563
      Train Epoch: 15 last_lr_used  0.000869  [88/98 (90%)] Loss: 0.331674
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 15
    loss           : 0.33284446292993974
    accuracy       : 88.3327828899417
    val_loss       : 0.2797890745103359
    val_accuracy   : 90.55836397058823
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch15.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 16 last_lr_used  0.000857  [0/98 (0%)] Loss: 0.310596
      Train Epoch: 16 last_lr_used  0.000829  [22/98 (22%)] Loss: 0.295233
      Train Epoch: 16 last_lr_used  0.000801  [44/98 (45%)] Loss: 0.290291
      Train Epoch: 16 last_lr_used  0.000773  [66/98 (67%)] Loss: 0.274164
      Train Epoch: 16 last_lr_used  0.000743  [88/98 (90%)] Loss: 0.347993
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 16
    loss           : 0.3090555482372946
    accuracy       : 89.32993956511176
    val_loss       : 0.28198918625712394
    val_accuracy   : 90.40326286764706
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch16.pth ...
      Train Epoch: 17 last_lr_used  0.000730  [0/98 (0%)] Loss: 0.321080
      Train Epoch: 17 last_lr_used  0.000700  [22/98 (22%)] Loss: 0.280649
      Train Epoch: 17 last_lr_used  0.000671  [44/98 (45%)] Loss: 0.370841
      Train Epoch: 17 last_lr_used  0.000641  [66/98 (67%)] Loss: 0.251170
      Train Epoch: 17 last_lr_used  0.000610  [88/98 (90%)] Loss: 0.291386
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 17
    loss           : 0.29689507171207546
    accuracy       : 89.5952912414966
    val_loss       : 0.28415571004152296
    val_accuracy   : 90.42279411764706
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch17.pth ...
      Train Epoch: 18 last_lr_used  0.000597  [0/98 (0%)] Loss: 0.280280
      Train Epoch: 18 last_lr_used  0.000566  [22/98 (22%)] Loss: 0.305956
      Train Epoch: 18 last_lr_used  0.000536  [44/98 (45%)] Loss: 0.248383
      Train Epoch: 18 last_lr_used  0.000506  [66/98 (67%)] Loss: 0.317397
      Train Epoch: 18 last_lr_used  0.000477  [88/98 (90%)] Loss: 0.280278
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 18
    loss           : 0.2857819258862612
    accuracy       : 90.02235939018465
    val_loss       : 0.27210545167326927
    val_accuracy   : 90.84041819852942
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch18.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 19 last_lr_used  0.000463  [0/98 (0%)] Loss: 0.297022
      Train Epoch: 19 last_lr_used  0.000434  [22/98 (22%)] Loss: 0.259632
      Train Epoch: 19 last_lr_used  0.000405  [44/98 (45%)] Loss: 0.287927
      Train Epoch: 19 last_lr_used  0.000377  [66/98 (67%)] Loss: 0.251006
      Train Epoch: 19 last_lr_used  0.000349  [88/98 (90%)] Loss: 0.252399
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 19
    loss           : 0.2702027832975193
    accuracy       : 90.48387770286686
    val_loss       : 0.2578959845006466
    val_accuracy   : 91.45450367647058
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch19.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 20 last_lr_used  0.000337  [0/98 (0%)] Loss: 0.208282
      Train Epoch: 20 last_lr_used  0.000310  [22/98 (22%)] Loss: 0.235749
      Train Epoch: 20 last_lr_used  0.000284  [44/98 (45%)] Loss: 0.223419
      Train Epoch: 20 last_lr_used  0.000259  [66/98 (67%)] Loss: 0.257766
      Train Epoch: 20 last_lr_used  0.000234  [88/98 (90%)] Loss: 0.282474
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 20
    loss           : 0.25641149723408174
    accuracy       : 91.15855047376093
    val_loss       : 0.2503166474401951
    val_accuracy   : 91.69175091911765
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch20.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 21 last_lr_used  0.000224  [0/98 (0%)] Loss: 0.213002
      Train Epoch: 21 last_lr_used  0.000201  [22/98 (22%)] Loss: 0.267832
      Train Epoch: 21 last_lr_used  0.000179  [44/98 (45%)] Loss: 0.223300
      Train Epoch: 21 last_lr_used  0.000158  [66/98 (67%)] Loss: 0.273129
      Train Epoch: 21 last_lr_used  0.000138  [88/98 (90%)] Loss: 0.232607
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 21
    loss           : 0.2434740618479495
    accuracy       : 91.55439519557822
    val_loss       : 0.2475512646138668
    val_accuracy   : 91.73655790441177
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch21.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 22 last_lr_used  0.000129  [0/98 (0%)] Loss: 0.244671
      Train Epoch: 22 last_lr_used  0.000111  [22/98 (22%)] Loss: 0.242367
      Train Epoch: 22 last_lr_used  0.000094  [44/98 (45%)] Loss: 0.180858
      Train Epoch: 22 last_lr_used  0.000079  [66/98 (67%)] Loss: 0.268158
      Train Epoch: 22 last_lr_used  0.000064  [88/98 (90%)] Loss: 0.233323
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 22
    loss           : 0.23391725639907682
    accuracy       : 91.90174395651118
    val_loss       : 0.2407365284860134
    val_accuracy   : 91.87097886029412
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch22.pth ...
      Saving current best: model_best.pth ...
      Train Epoch: 23 last_lr_used  0.000058  [0/98 (0%)] Loss: 0.207735
      Train Epoch: 23 last_lr_used  0.000046  [22/98 (22%)] Loss: 0.233393
      Train Epoch: 23 last_lr_used  0.000035  [44/98 (45%)] Loss: 0.237875
      Train Epoch: 23 last_lr_used  0.000026  [66/98 (67%)] Loss: 0.180160
      Train Epoch: 23 last_lr_used  0.000018  [88/98 (90%)] Loss: 0.189946
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 23
    loss           : 0.22925959345029326
    accuracy       : 92.06943938289601
    val_loss       : 0.24087431505322457
    val_accuracy   : 91.98816636029412
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch23.pth ...
      Train Epoch: 24 last_lr_used  0.000015  [0/98 (0%)] Loss: 0.222593
      Train Epoch: 24 last_lr_used  0.000009  [22/98 (22%)] Loss: 0.191968
      Train Epoch: 24 last_lr_used  0.000004  [44/98 (45%)] Loss: 0.281866
      Train Epoch: 24 last_lr_used  0.000002  [66/98 (67%)] Loss: 0.234212
      Train Epoch: 24 last_lr_used  0.000000  [88/98 (90%)] Loss: 0.252746
      <utils.util.MetricTracker object at 0x7f85d8716890>
    epoch          : 24
    loss           : 0.22553442160085757
    accuracy       : 92.13814990281827
    val_loss       : 0.24010530784726142
    val_accuracy   : 92.01746323529412
      Saving checkpoint: saved/models/CIFR10/1205_135958/checkpoint-epoch24.pth ...
      Saving current best: model_best.pth ...
       
Project template repo link : https://github.com/Nageswar-Sahoo/Computer-Vision-Project/tree/main/template



