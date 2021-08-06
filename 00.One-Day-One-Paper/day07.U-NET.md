# U-Net: Convolutional Networks for Biomedical Image Segmentation
- https://arxiv.org/abs/1505.04597
- [Submitted on 18 May 2015]
- MICCAI 2015
---

## Abstract.
In this paper, we present a network and training strategy that relies on the strong use of data augmentation to use the available annotated samples more effciently.


## 1 Introduction
deep convolutional networks로 할 수 있는 다양한 task
- classiffication tasks - the output to an image is a single class label.
> - biomedical image processing, the desired output should include localization(class label is supposed to be assigned to each pixel)
- Ciresan et al. network
> - trained a network in a sliding-window
> - this network can localize.
> - he training data in terms of patches is much larger than the number of training images.
> - 단점 1. it is quite slow because the network must be run separately for each patch and there is a lot of redundancy due to overlapping patches.
> - 단점 2. trade-off between localization accuracy and the use of context.
- In this paper,
> - "fully convolutional network"
> - it works with very few training images
> - yields more precise segmentations
> - to supplement a usual contracting network by successive layers, where pooling operators are replaced by upsampling operators.
> - these layers increase the resolution of the output.
> - high resolution features from the contracting path are combined with the upsampled output
> - upsampling part we have also a large number of feature channels, which allow the network to propagate context information to higher resolution layers.
> - As a consequence, the expansive path is more or less symmetric to the contracting path, and yields a u-shaped architecture.
> - overlap-tile strategy : To predict the pixels in the border region of the image, the missing context is extrapolated by mirroring the input image. (미러링기법을 사용해서 빈 공간을 채운다. 정보 손실을 최고화한다.)
- augmentation
> - our tasks there is very little training data available,
> - we use excessive data augmentation by applying elastic deformations to the available training images.
> - elastic deformations : 이미지에 선형변형을 가한다, 불규칙하게 뒤틀린다, 좀 더 현실에 있음직하게 변형됨
- Segmentation
> - we propose the use of a weighted loss, where the separating background labels between touching cells obtain a large weight in the loss function.

## 2 Network Architecture
- It consists of a contracting path (left side) and an expansive path (right side).

- contracting path
> - two 3x3 convolutions (unpadded convolutions),
> - rectified linear unit (ReLU)
> - 2x2 max pooling- 사이즈를 줄여준다.
> - stride 2 for downsampling

- expansive path
> - 2x2 convolution ("up-convolution")
> - concatenation with the correspondingly cropped feature map from the contracting path,
> - two 3x3 convolutions,
> - ReLU
> - final layer a 1x1 convolution

- seamless tiling of the output segmentation map
> - input tile size such that all 2x2 max-pooling operations

## 3 Training
- large input tiles over a large batch size and hence reduce the batch to a single image.    
- we use a high momentum (0.99)
- energy function is computed by a pixel-wise soft-max over the final feature map combined with the cross entropy loss function.
- The separation border is computed using morphological operations.
- good initialization of the weights is extremely important.

### 3.1 Data Augmentation
Data augmentation is essential to teach the network the desired invariance and robustness properties, when only few training samples are available.
we primarily need shift and rotation invariance as well as robustness to deformations and gray value variations.

## 4 Experiments
three different segmentation
- The first task is the segmentation of neuronal structures in electron microscopic recordings.
> - The u-net (averaged over 7 rotated versions of the input data) achieves without any further pre- or postprocessing a warping error of 0.0003529 (the new best score, see Table 1) and a rand-error of 0.0382.
> - This is signifficantly better than the sliding-window convolutional network result by Ciresan et al.
- We also applied the u-net to a cell segmentation task in light microscopic images.
> - Here we achieve an average IOU (\intersection over union") of 92%, which is signicantly better than the second best algorithm with 83% (see Table 2).
- Here we achieve an average IOU of 77.5% which is signicantly better than the second best algorithm with 46%.

## 5 Conclusion
The u-net architecture achieves very good performance on very dierent bio medical segmentation applications. Thanks to data augmentation with elastic defor-mations, it only needs very few annotated images and has a very reasonable training time of only 10 hours

---
---
---
# U-Net: Convolutional Networks for Biomedical Image Segmentation
- https://arxiv.org/abs/1505.04597
- [Submitted on 18 May 2015]
- MICCAI 2015
---
## Summary
Biomedical Image를 augmentation한 후, Segmentation할 수 있는 U-Net 을 발표했다.

해당 논문에서 제안한 것들
- 적은 훈련 데이터 이미지로 segmentation에 있어 좋은 성능을 보여주었다.
![image](https://user-images.githubusercontent.com/70581043/128465723-e75e9ea1-be01-40ce-92a3-c9dd14aaf3d4.png)
- 전체적으로 CNN으로 이루어진 u-shaped architecture
> **1. contracting network**
> - two 3x3 convolutions (unpadded convolutions),
> - rectified linear unit (ReLU)
> - 2x2 max pooling- 사이즈를 줄여준다.
> - stride 2 for downsampling

> **2. expansive path**
> - 2x2 convolution ("up-convolution")
> - concatenation with the correspondingly cropped feature map from the contracting path,
> - two 3x3 convolutions,
> - ReLU
> - final layer a 1x1 convolution

> **3. overlap-tile strategy** 
> - 가장자리에 있는 비어있는 부분을 mirroring 방법으로 채워 넣었다.
> - 2x2 max-pooling operations

- fully connected layers 없음
- data augmentation 
> - elastic deformations방법을 사용함, 
> - 이 방법은 biomedical segmentation에서 tissue 혹은 현실적인 변형의 모습과 유사함 
> - using random displacement vectors on a coarse 3 by 3 grid.

- cell segmentation tasks : weighted loss를 사용함, background 라벨과 cell 라벨 간 큰 weight를 갖는다.

## Training
- stochastic gradient descent implementation
-  large batch size
- high momentum (0.99)
- energy function : a pixel-wise soft-max over the final feature map combined with the cross entropy loss function. (픽셀 x가 어느 k에 가까운지)
![image](https://user-images.githubusercontent.com/70581043/128466453-3036e372-c6c6-4ed7-89ce-77d07d2c7540.png)
- weight map : separation border is computed using morphological operations. (수식은 이해 못했음ㅠㅠ)
![image](https://user-images.githubusercontent.com/70581043/128466632-3473e779-ab0b-4f4d-a217-d70d616f84bb.png)

## Experiments
![image](https://user-images.githubusercontent.com/70581043/128467526-05b305a7-3357-42f5-bfee-835ca584b3e4.png)
- segmentation 결과 다른 모델들에 비해  warping error 가 작았음

![image](https://user-images.githubusercontent.com/70581043/128467769-ab245dcf-c852-4d6a-b4fc-d38f305da3d6.png)
- PhC-U373 데이터 셋과 DIC-HeLa 데이터 셋으로 cell segmentation한 결과, IOU가 가장 높게 나옴