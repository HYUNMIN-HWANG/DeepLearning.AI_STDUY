# Rethinking Atrous Convolution for Semantic Image Segmentation
- https://arxiv.org/abs/1706.05587
- 참고 자료 : http://www.navisphere.net/7660/rethinking-atrous-convolution-for-semantic-image-segmentation/
---
## DeepLab v3

기존 sementic segmentation의 두 가지 문제점
1. reduced feature resolution 
       - pooling이나 convolution striding으로 feature resolution의 저하 문제, 정보 손실 문제
       - 논문 제안 : **atrous convolution** 사용
2. objects at multiple scales
![image](https://user-images.githubusercontent.com/70581043/141099698-7c8e96ee-cf66-4450-8ab1-3a97d9d64a58.png)
       (a)  Image Pyramid : shared weights / 문제는 does not scale well for larger/deeper DCNNs
       (b)  Encoder-Decoder : 인코더에서 feature map이 점점 줄어들면서 긴 길이의 정보들의 특징을 잡을 수 있음, 디코더에서 spatial dimension을 회복해나감
       (c)  Deeper w. Atrous Convolution (Context module) : incorporate DenseCRF to DCNNs / or jointly train both the CRF and DCNN components / or combine Gaussian Conditional Random Fields and DCNNs
       (d)  Spatial Pyramid Pooling : atrous spatial pyramid pooling (ASPP),
     
## atrous convolution 이란?
![image](https://user-images.githubusercontent.com/70581043/141099270-a5b0ab2c-c195-4e3b-8f20-d75bb5474f2d.png)
- effectively enlarge the field of view of filters to incorporate multi-scale context
- laying out the modules in cascade or in parallel (Atrous Spatial Pyramid Pooling)
- adopts hybrid atrous rates within the last two blocks of ResNet
- 기존 convolution filter의 weight들 사이에 0을 넣어 크기를 늘린 것이다. 여기서 rate은 얼마나 많은 0을 넣는지를 의미한다.
### Atrous Convolution for Dense Feature Extraction
- for the task of semantic segmentation.
- atrous rate r : stride with which we sample the input signal (upsampling 어느 정도 할 것인지)
- r = 1 : Standard convolution
- Atrous Convolution : explicitly control how densely to compute feature responses in fully convolutional networks.
### Going Deeper with Atrous Convolution
![image](https://user-images.githubusercontent.com/70581043/141102801-07c1a85e-8b43-4bb0-82d4-e5c0e27e16a5.png)
- duplicate several copies of the last ResNet block, 특히 cascaded ResNet blocks up to block7 (Atrous Convolution 적용 안하면 output stride 256, 적용하면 16)

### Multi-grid Method
block4에서 block7의 내에 있는 3개의 convolution layer에 대한 rate를 Multi Grid = (r1; r2; r3)로 지정

### Atrous Spatial Pyramid Pooling
- Atrous Spatial Pyramid Pooling(ASPP) : four parallel atrous convolutions with different atrous rates are applied on top of the feature map.
- ASPP 안에 batch normalization을 추가시킴
- ASPP with different atrous rates effectively captures multi-scale information
- 하지만, sampling rate이 커지면 valid filter weight는 작아진다.
- 해결책 : apply global average pooling on the last feature map of the model : 1x1 convlolution with 256 and BN, 그리고 bilinear interpolation을 통해 upsampling한다.
![image](https://user-images.githubusercontent.com/70581043/141104460-560270ba-fb50-45f0-a25c-f87e8c39b729.png)
