# Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization
- https://arxiv.org/abs/1703.06868
- code : https://github.com/xunhuang1995/AdaIN-style
- [Submitted on 20 Mar 2017 (v1), last revised 30 Jul 2017 (this version, v2)]
- ICCV 2017

---

## Abstract
style transfer 단점 : slow iterative optimization process, fixed set of styles and cannot adapt to arbitrary new styles.
논문 제안 : we present a simple yet effective approach that for the first time enables arbitrary style transfer in real-time. 
특징 : aligns the mean and variance of the content features with those of the style features.
장점 : achieves speed comparable to the fastest existing approach, without the restriction to a pre-defined set of styles. flexible user controls (자신이 원하는 임의의 스타일 이미지로부터 스타일 정보를 가져올 수 있음, 실시간으로 빠르게 스타일 전송을 진행할 수 있음)

## 1. Introduction
neural style transfer 속도를 높이기 위한 노력
- attempted to train feed-forward neural networks that perform stylization with a single forward pass. > 문제점 : each network is restricted to a single style.

Our approach
-  transfer arbitrary new styles in real-time
- combining the flexibility of the optimization based framework
- the speed similar to the fastest feed-forward approaches
- inspired by the instance normalization (IN) layer,
- we introduce a simple extension to IN, namely adaptive instance normalization (AdaIN)
- Given a content input and a style input, AdaIN simply adjusts the mean and variance of the content input to match those of the style input.
- we find AdaIN effectively combines the content of the former and the style latter by transferring feature statistics.
- A decoder network is then learned to generate the final stylized image by inverting the AdaIN output back to the image space
- 장점 : magnitude faster without sacrificing the flexibility of transferring inputs to arbitrary new styles. & our approach provides abundant user controls at runtime, without any modification to the training process.

## 2. Related Work
### Style transfer.
기존 Style transfer.의 문제점 
- These methods typically rely on low-level statistics and often fail to capture semantic structures.
- framework of Gatys : based on a slow optimization process that iteratively updates the image to minimize a content loss and a style loss computed by a loss network.
- feed-forward style transfer : limited in the sense that each network is tied to a fixed style.
- transfer arbitrary styles: their style swap layer creates a new computational bottleneck
- style loss function :  aim to match some feature statistics between the style image and the synthesized image.

### Deep generative image modeling.
GANs have also been applied to style transfer and cross-domain image generation

## 3. Background
### 3.1. Batch Normalization
- batch normalization (BN) layer that significantly ease the training of feed-forward networks by normalizing feature statistics.
- to accelerate training of discriminative networks but have also been found effective in generative image modeling
- mean and standard deviation, computed across batch size and spatial dimensions independently for each feature channel
- BN uses mini-batch statistics during training and replace them with popular statistics during inference

### 3.2. Instance Normalization
- ean and standard deviation, computed across spatial dimensions independently for each channel and *each sample*
- applied at test time unchanged, whereas BN layers usually replace minibatch statistics with population statistics.

### 3.3. Conditional Instance Normalization
- conditional instance normalization (CIN) layer that learns a different set of parameters γs and βs for each style s:
- the network can generate images in completely different styles by using the same convolutional parameters but different affine parameters in IN layers.

## 4. Interpreting Instance Normalization
- IN takes place in the feature space 
- the affine parameters in IN can completely change the style of the output image
- instance normalization performs a form of style normalization by normalizing feature statistics, namely the mean and variance
- Our results indicate that IN does perform a kind of style normalization.
- IN can normalize the style of each individual sample to the target style.
- The reason behind the success of CIN also becomes clear: different affine parameters can normalize the feature statistics to different values, thereby normalizing the output image to different styles.

## 5. Adaptive Instance Normalization (AdaIN)
- it adaptively computes the affine parameters from the style input
- AdaIN performs style transfer in the feature space by transferring feature statistics, specifically the channel-wise mean and variance.
- adding almost no computational cost.

## 6. Experimental Setup
### 6.1. Architecture
Our style transfer network T takes a content image c and
an arbitrary style image s as inputs, and synthesizes an output
image that recombines the content of the former and the
style latter.

- encoder f : fixed to the first few layers (up to relu4 1) of a pre-trained VGG-19
- After encoding the content and style images in feature space, we feed both feature maps to an AdaIN layer that aligns the mean and variance of the content feature maps to those of the style feature maps,
- decoder g : trained to map t back to the image space, generating the stylized image T(c, s)
- use reflection padding in both f and g to avoid border artifacts
- we do not use normalization layers in the decoder.

### 6.2. Training
- We use the adam optimizer and a batch size of 8 content-style image pairs
- image : 512 -> 256 × 256
- use the pre-trained VGG-19 to compute the loss function to train the decoder
- content loss is the Euclidean distance between the target features and the features of the output image.
- style loss : our AdaIN layer only transfers the mean and standard deviation of the style features, our style loss only matches these statistics

## 7. Results
### 7.1. Comparison with other methods
compare our approach with three types of style transfer methods
1) the flexible but slow optimization-based method
2) the fast feed-forward method restricted to a single style
3) the flexible patch-based method of medium speed

**Qualitative Examples**   
all the test style images are never observed during the training of our model, while the results of are obtained by fitting one network to each test style.

**Quantitative evaluations**  
we compare our approach with the optimization-based method and the fast single-style transfer method in terms of the content and style loss
note that our style loss is much smaller than that of the original content image.

**Speed analysis**   
- our method is nearly 3 orders of magnitude faster
- achieves comparable speed to feed-forward methods limited to a few styles

### 7.2. Additional experiments.
proposed : Enc-AdaIN-Dec
실험 : Enc-Concat-Dec / Enc-AdaIN-BNDec / Enc-AdaIN-INDec

- Enc-Concat-Dec : fails to disentangle the style information from the content of the style image, fail to decrease the content loss
- BN/IN layers also obtain qualitatively worse results and consistently higher losses

### 7.3. Runtime controls
**Content-style trade-off**    
our method allows content-style trade-off at test time by interpolating between feature maps that are fed to the decoder.

**Style interpolation**    
we similarly interpolate between feature maps

**Spatial and color control**    
controls over color information and spatial locations of style transfer, which can be easily incorporated into our framework.
our method can transfer different regions of the content image to different styles.

## 8. Discussion and Conclusion

---
---
---
---
# Arbitrary Style Transfer in Real-time with Adaptive Instance Normalization
- https://arxiv.org/abs/1703.06868
- code : https://github.com/xunhuang1995/AdaIN-style
- [Submitted on 20 Mar 2017 (v1), last revised 30 Jul 2017 (this version, v2)]
- ICCV 2017

---

## Summary
기존  style transfer 들은 속도가 느리거나 / 한 가지 스타일로만 변환할 수 있다는 단점이 있다. 이를 극복하기 위해서 해당 논문에서는 Adaptive Instance Normalization를 사용해 한 번 훈련시키면 임의의 스타일로 변환할 수 있는 style transfer 모델을 제안했다.

## Normalization
1. Batch Normalization
![image](https://user-images.githubusercontent.com/70581043/128135897-54c25154-8dde-4d99-9d4e-c814371195a4.png)    
네트워크를 빠르게 훈련시킬 수 있다는 장점이 있다.  each feature channel 에서의 mean 값과 standard deviation을 계산한다.

2. Instance Normalization
![image](https://user-images.githubusercontent.com/70581043/128136030-65c7877d-71c8-405e-9bf4-92852f2520f2.png)    
Batch Normalization와 유사함, Instance Normalization은 each feature channel 뿐만 아니라 each sample에서의 mean 값과 standard deviation을 계산한다.

3. Adaptive Instance Normalization
![image](https://user-images.githubusercontent.com/70581043/128136185-2f007687-c251-4e50-86b6-57400d91cd77.png)    
각각의 스타일 s 마다 다른 감마, 베타 값을 다르게 적용시킬 수 있다. 즉, 하나의 같은 네트워크에서 완전히 다른 스타일의 이미지를 만들어낼 수 있다. *(논문에서 참고한 방식)*

4. Adaptive Instance Normalization (AdaIN)
![image](https://user-images.githubusercontent.com/70581043/128136593-a8f77fbf-dec4-4011-b1c1-5c219208084b.png)    
content 를 전달할 x 이미지를 넣었을 때, y의 style 로 바꿔주는 역할을 한다. *(논문에서 제안한 방식)*

## Architecture
![image](https://user-images.githubusercontent.com/70581043/128136897-39cf9fe2-b792-438f-a158-37a83885272b.png)

- encoder f :  pre-trained VGG-19 , content image와 style image에서의 feature를 추출한다.
- AdaIN layer : content feature map에서 style feature map으로 변환해준다.
- decoder g : 스타일이 적용된 이미지를 generate 한다.
- pre-trained VGG-19 : content loss 와 style loss 계산

> - content loss
![image](https://user-images.githubusercontent.com/70581043/128137936-7e7e2e66-fa14-439d-b3bb-76101aaa4447.png)    
아웃풋 이미지의 features와 타겟 features의 거리 차이를 구한다.

> - style loss
![image](https://user-images.githubusercontent.com/70581043/128137966-28950b12-7838-4fd0-86db-eac463014027.png)    
IN statistics 를 사용하여 결과를 계산한다. 각각의 VGG19 레이어에서의 style loss를 구한다.

## Result
![image](https://user-images.githubusercontent.com/70581043/128137473-5d875c16-3e85-4a3e-80de-43e01308901e.png)    
 - content loss 와 style loss 가 어느 정도 좋은 결과를 보임    
![image](https://user-images.githubusercontent.com/70581043/128137558-2ea36b7c-34d1-4100-8508-624560883dc2.png)    
- 기존 모델에 비해 속도가 빠른 편이며, 다양한 스타일로 변환할 수 있다.    
![image](https://user-images.githubusercontent.com/70581043/128137621-f1e43e63-fcd5-4243-8f5e-1a7771e7f973.png)    
- 눈으로 봤을 때도 스타일이 잘 적용된 것을 볼 수 있다.