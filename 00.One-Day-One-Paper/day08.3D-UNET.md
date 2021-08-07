# 3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation
- https://arxiv.org/abs/1606.06650
- [Submitted on 21 Jun 2016]
- MICCAI 2016

---

## Abstract.
This paper introduces a network for volumetric segmentation that learns from sparsely annotated volumetric images
1) semi-automated setup, the user annotates some slices in the volume to be segmented.
2) fully-automated setup, we assume that a representative, sparsely annotated training set exists.
U-NET by replacing all 2D operations with their 3D counterparts.
elastic deformations for effcient data augmentation during training.

## 1 Introduction
Volumetric data is abundant in biomedical data analysis. Annotation of such data with segmentation labels causes diculties, since only 2D slices can be shown on a computer screen.
full annotation of 3D volumes is not an eective way to create large and rich training data sets that would generalize well.
In this paper,
- we suggest a deep network that learns to generate dense volumetric segmentations, but only requires some annotated 2D slices for training.
> 1. the first application case just aims on densification of a sparsely annotated data set
> 2. the second learns from multiple sparsely annotated data sets to generalize to new data.
- The network is based on the previous u-net architecture
> contracting encoder part to analyze the whole image
> a successive expanding decoder part to produce a full-resolution segmentation
- 3D convolutions, 3D max pooling, and 3D up-convolutional layers
- use batch normalization
- A weighted loss function and special data augmentation enable us to train the network with only few manually annotated slices, i.e., from sparsely annotated training data.
- data set : Xenopus kidney 

### 1.1 Related Work
성공적인 CNN 모델들 -> 3D CNNs on biomedical volumetric data
Our work is based on the 2D u-net
The highlight of the present paper is that it can be trained from scratch on sparsely annotated volumes and can work on arbitrarily large volumes due to its seamless tiling strategy.

## 2 Network Architecture
Like the standard u-net,
The architecture has 19069955 parameters in total.
We also introduce batch normalization (\BN") before each ReLU
weighted softmax loss function : Setting the weights of unlabeled pixels to zero makes it possible to learn from only the labelled ones and, hence, to generalize to the whole volume.

## 3 Implementation Details
### 3.1 Data
three samples of Xenopus kidney embryos at Nieuwkoop-Faber stage 36-37
We manually annotated some orthogonal xy, xz, and yz slices in each volume using Slicer3D
the labels 0: "inside the tubule"; 1: "tubule"; 2: :"background", and 3: "unlabeled"

### 3.2 Training
- Besides rotation, scaling and gray value augmentation, we apply a smooth dense deformation field on both data and ground truth labels
- The network output and the ground truth labels are compared using softmax with weighted cross-entropy loss, where we reduce weights for the frequently seen background and increase weights for the inner tubule to reach a balanced influence of tubule and background voxels on the loss.
- stochastic gradient descent

## 4 Experiments
### 4.1 Semi-Automated Segmentation
the user needs a full segmentation of a small number of volumetric images,
- qualitative assessment > trained the network on all three sparsely annotated samples. The network can nd the whole 3D volume segmentation from a few annotated slices and saves experts from full volume annotation.
- assess the quantitative > 
> - 2D vs 3D : Intersection over Union (IoU) is used as accuracy measure to compare dropped out ground truth slices to the predicted 3D volume.
> - semi-automated segmentation 몇 장 했는지에 따른 결과 비교

### 4.2 Fully-automated Segmentation
the user wants to segment a large number of images recorded in a comparable setting.
In this experiment BN also improves the result
The typical use case for the fully-automated segmentation will work on much larger sample sizes, where the same number of sparse labels could be easily distributed over much more data sets to obtain a more representative training data set.

## 5 Conclusion
We achieve an average IoU of 0.863 in 3-fold cross validation experiments for the semi-automated setup


---
---
---
# 3D U-Net: Learning Dense Volumetric Segmentation from Sparse Annotation
- https://arxiv.org/abs/1606.06650
- [Submitted on 21 Jun 2016]
- MICCAI 2016

---

## Summary
U-NET의 3D 버전 논문 !! 바이오 데이터 중 3D 데이터는 많지만 이를 직접 segmentation 하기에는 어려움이 있기 때문에 해당 논문에서 3D annotation 방법을 제안했다.

**해당 논문의 아이디어는 크게 두 가지 부분으로 나눌 수 있다.**
![image](https://user-images.githubusercontent.com/70581043/128590785-e84d252a-1b0c-4def-ac04-6a6c421e3364.png)
1. semi-automated setup, the user annotates some slices in the volume to be segmented. (2D 이미지 몇 개만 annotate 한 후 segmentation을 진행한다.)
2. fully-automated setup, we assume that a representative, sparsely annotated training set exists. (1에서 훈련한 모델을 기반으로 새로운 3D 이미지를 segmentation 한다.)

**모델 및 훈련 특징**
![image](https://user-images.githubusercontent.com/70581043/128590768-a2bce6b0-5dcc-4ebb-9da4-d33e9696e50f.png)
-  The network is based on the previous u-net architecture
- 단, 3D convolutions, 3D max pooling, and 3D up-convolutional layers 사용함
- use batch normalization
- weighted softmax loss function (unlabeld pixels는 weight를 0으로 세팅함, labeld data만 1)
- augmentation : rotation, scaling and gray value augmentation, smooth dense deformation

**결과**
1. Semi-Automated Segmentation
![image](https://user-images.githubusercontent.com/70581043/128590634-983f7b2f-b084-4eb9-a8f6-fd2844ef318d.png)
2d 이미지와 3d 비교했을 때, 3d(with BN)일 때 IOU가 가장 높았다. semi-automated segmentation 몇 장 했는지에 따른 결과를 비교했을 때 S3 성능이 가장 좋았다.

2. Fully-automated Segmentation
![image](https://user-images.githubusercontent.com/70581043/128590642-66359baf-1da7-4845-bece-7785ef7d6831.png)
BN를 할 때(test3을 제외하고) & 샘플 사이즈가 클 때 성능이 좋았다.