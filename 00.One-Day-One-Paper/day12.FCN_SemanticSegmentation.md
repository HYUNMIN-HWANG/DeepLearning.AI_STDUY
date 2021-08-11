# Fully Convolutional Networks for Semantic Segmentation
- https://arxiv.org/abs/1411.4038
- [Submitted on 14 Nov 2014 (v1), last revised 8 Mar 2015 (this version, v2)]
- CVPR (2015)

---

## Abstract
We adapt contemporary classification networks (AlexNet, the VGG net, and GoogLeNet) into fully convolutional networks and transfer their learned representations by fine-tuning to the segmentation task.
We then define a skip architecture that combines semantic information from a deep, coarse layer with appearance information from a shallow, fine layer to produce accurate and detailed segmentations.


## 1 INTRODUCTION
- We show that fully convolutional networks (FCNs) trained end-to-end, pixels-to-pixels on semantic segmentation exceed the previous best results without further machinery.
(1) for pixelwise prediction
(2) from supervised pre-training

- Semantic segmentation faces an inherent tension between semantics and location : what while local information resolves where
- we cast pre-trained networks into fully convolutional form, and augment them with a skip architecture that takes advantage of the full feature spectrum.

## 2 RELATED WORK
### Fully convolutional networks
- the idea of extending a convnet (limited to one-dimensional input strings) -> expand convnet outputs to 2-dimensional maps -> coarse multiclass segmentation 
- Fully convolutional computation : Sliding window detection, semantic segmentation, image restoration

### Dense prediction with convnets
- we do study patchwise training
- “shift-and stitch” dense output from the perspective of FCNs
- We also discuss in-network upsampling
- we adapt and extend deep classification architectures, using image classification as supervised pre-training, and fine-tune fully convolutionally to learn simply and efficiently from whole image inputs and whole image ground thruths.
- R-CNN system : by sampling bounding boxes and/or region proposals for detection, semantic segmentation, and instance segmentation. 

### Combining feature hierarchies
We fuse features across layers to define a nonlinear local-to-global representation that we tune end-to-end.

### FCN extensions
FCNs presented here to further advance the state-of-the-art in semantic segmentation.

## 3 FULLY CONVOLUTIONAL NETWORKS
- Each layer output in a convnet is a three-dimensional array of size h x w x d,
- h and w are spatial dimensions
- d is the feature or channel dimension
- Convnets are inherently translation invariant.
- An FCN naturally operates on an input of any size, and produces an output of corresponding (possibly resampled) spatial dimensions.

### 3.1 Adapting classifiers for dense prediction
- fully connected layers can also be viewed as convolutions with kernels that cover their entire input regions.
- Doing so casts these nets into fully convolutional networks that take input of any size and make spatial output maps
- While our reinterpretation of classification nets as fully convolutional yields output maps for inputs of any size, the output dimensions are typically reduced by subsampling.
- The classification nets subsample to keep filters small and computational requirements reasonable

### 3.2 Shift-and-stitch is filter dilation
- Dense predictions can be obtained from coarse outputs by stitching together outputs from shifted versions of the input.
- Simply decreasing subsampling within a net is a tradeoff: the filters see finer information, but have smaller receptive fields and take longer to compute
- This dilation trick is another kind of tradeoff: the output is denser without decreasing the receptive field sizes of the filters but the filters are prohibited from accessing information at a finer scale than their original design. 
- 해당논문에서는 dilation 안함 -> combined with the skip layer fusion described later on.

### 3.3 Upsampling is (fractionally strided) convolution
- interpolation
- “backward convolution” by reversing the forward and backward passes of more typical input-strided convolution.
- upsampling is performed in-network for end-to-end learning by backpropagation from the pixelwise loss.
- A stack of deconvolution layers and activation functions can even learn a nonlinear upsampling.
- we find that in-network upsampling is fast and effective for learning dense prediction.

### 3.4 Patchwise training is loss sampling
- Whole image fully convolutional training is identical to patchwise training where each batch consists of all the receptive fields of the output units for an image (or collection of images).
- random sampling of patches within an image may be easily recovered
- If the kept patches still have significant overlap, fully convolutional computation will still speed up training.

## 4 SEGMENTATION ARCHITECTURE
skip architecture : learned end-to-end to refine the semantics and spatial precision of the output.

### 4.1 From classifier to dense FCN
FCN-AlexNet FCN-VGG16 FCN-GoogLeNet
- SGD with momentum
- fixed learning rates of 10-3, 10-4, and 5-5 for FCN-AlexNet,FCN-VGG16, and FCN-GoogLeNet,
- momentum 0:9, weight decay of 5􀀀4 or 2􀀀4, and doubled learning rate for biases
- Dropout is included where used in the original classifier nets
- Fine-tuning from classification to segmentation gives reasonable predictions from each net.
- We select FCN-VGG16 as our base network

### 4.2 Image-to-image learning
- The image-to-image learning setting includes high effective batch size and correlated inputs. This optimization requires some attention to properly tune FCNs.
- We do not normalize the loss
- every pixel has the same weight regardless of the batch and image dimensions.
- we use a small learning rate since the loss is summed spatially over all pixels.
1. gradients are accumulated over 20 images
> - Accumulation reduces the memory required and respects the different dimensions of each input by reshaping the network.
2. batch size one is used for online learning.
> - higher accuracy and faster convergence
> - momentum of 0.99
> - increases the weight on recent gradients in a similar way to batching.

### 4.3 Combining what and where
- We define a new fully convolutional net for segmentation that combines layers of the feature hierarchy and refines the spatial precision of the output.
- We address this by adding skips that fuse layer outputs, in particular to include shallower layers with finer strides in prediction.
- 



---
---
---
# Fully Convolutional Networks for Semantic Segmentation
- https://arxiv.org/abs/1411.4038
- [Submitted on 14 Nov 2014 (v1), last revised 8 Mar 2015 (this version, v2)]
- CVPR (2015)

---

## Summary
**1.  Fully Convolutional Networks**
- FCN의 특징은 어떠한 인풋 사이즈 이미지가 들어왔던, 해당 이미지에 대응되는 아웃풋 이미지를 만들어내는 것
- patch-by-patch 대신 layer-by-layer로 전체 이미지를 계산할 때 더 효율적이다.
- fully connected layer 대신에 사용
-  subsampling을 했기 때문에 input size 보다 차원이 줄어든다.

**2. Upsampling**
- FCN으로 차원이 줄어들었기 때문에 in-network upsampling을 사용 (?? pixelwise loss 로  역전파를 하는 것?) 

**3. Segmentation architecture**
- classification model은 VGG16 network를 사용한 게 가장 성능이 좋았다.
![image](https://user-images.githubusercontent.com/70581043/129031705-ebbf7789-6cef-4fdb-8855-eabe4c662207.png)
- Skip Architectures for Segmentation : skip architecture를 추가함으로써  local 정보를 더 정확하게 예측 
> - stride 32를 사용해서 한 번에 인풋 사이즈로 돌아가는 것 > FCN-32s
> - 마지막 레이어 + pool4에서 stride 16  > FCN-16s
> - 마지막 레이어 + pool4에서 stride 16 + pool3에서 stride 8 > FCN-8s      

![image](https://user-images.githubusercontent.com/70581043/129032741-a310e97c-675e-4082-bc01-756293cd1f43.png)
FCN-8s의 결과가 정답과 가장 유사하다.

## Results
1. PASCAL VOC
![image](https://user-images.githubusercontent.com/70581043/129033716-d61f79d6-ca72-4af1-b9eb-69fdb5984264.png)
mean IU 값이 가장 좋았고, 시간도 114배 아낄 수 있었다.
 
2. NYUDv2
![image](https://user-images.githubusercontent.com/70581043/129033879-8890edb0-7280-4ab4-923b-f9c8e4894328.png)
- RGB images
- GBD : RGB에 depth information이 추가
- HHA : 3 dimensional
- RGB-HHA : combine color and depth > 성능이 가장 좋았음

3. SIFT Flow
![image](https://user-images.githubusercontent.com/70581043/129034322-9126140c-26ee-43d1-a8fb-1058f929f8f6.png)
- 33 semantic classes & 3 geometric classes
- FCN-8s 가 성능이 가장 좋았다.

4. PASCAL-Context
![image](https://user-images.githubusercontent.com/70581043/129034904-2dfd6eaf-a323-4556-bc5e-ebb02b93df98.png)
![image](https://user-images.githubusercontent.com/70581043/129034594-ddf75aeb-498d-486e-a204-6d28b58c9282.png)
- 가장 많이 등장한 59 class만 사용함
- FCN이 다른 모델에 비해 성능이 좋았음
 
---

참고자료 : https://www.youtube.com/watch?v=_52dopGu3Cw