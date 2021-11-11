# Image-to-Image Translation with Conditional Adversarial Networks
- https://arxiv.org/abs/1611.07004
- Proceedings of the IEEE conference on computer vision and pattern recognition. 2017.
---
## Pix2Pix
image-to-image translation 문제에 관한 모델이다. 기존  image-to-image translation을 하는 CNN모델에서는 단순히 예측한 값과 GT 값 간의 Euclidean 거리를 감소시키는 방향으로 학습되었다. 하지만 이 방법을 사용했을 때 이미지가 blurring된다는 문제가 발생했다. 해당 논문에서는 conditioned GAN을 제안하며 blur되는 것을 방지했다.

### conditioned GANs
![image](https://user-images.githubusercontent.com/70581043/141312501-31181731-6c00-4d63-8c77-c6ab72817c58.png)
- 위 이미지, edge to phto를 예시로 설명
- 기존 G는 noise vector z만 넣었었는데, cGAN에서는 z 뿐만 아니라 원본 x도 같이 넣는다.
- D는 G로 생성한 이미지 G(x)와 원본 x를 묶어서 fake로 예측 & GT이미지인 y와 원본 x를 묶어서 real로 판별해야 한다.
- _both the generator and discriminator observe the input edge map_

### Loss
![image](https://user-images.githubusercontent.com/70581043/141313192-bc986a0f-6545-45d1-b4d5-ba4504d4f9fd.png)
(1) conditional GAN loss : G와 D 모두 원본 x가 들어가 있음, minimize G, maximize D하는 것이 목표
![image](https://user-images.githubusercontent.com/70581043/141313412-92e59ba0-a6e5-4c42-84fe-2ec0da886918.png)
(2) unconditional variant GAN loss : D에 원본 x 안 들어가 있음
![image](https://user-images.githubusercontent.com/70581043/141313577-5b5f2426-3a0a-4c48-aea0-0581d6d49ed0.png)
(3) L2 distance가 아닌 L1 distance를 사용함
![image](https://user-images.githubusercontent.com/70581043/141313678-3c41b3f4-cf16-44b6-a916-ee08bead9ae2.png)
최종 objectrive

### Architecture
- Generator : U-NET 구조 사용, encoder-decoder 사용하는 것 대신 U-NET 사용해서 bottleneck 문제를 해결
- Discriminator : patchGAN 사용, blurry 한 결과가 나오는 것을 해결, only penalizes structure at the scale of patches, N x N 개의 patch 이미지들을 real인지 fake인지 판별한다. 

## Results
![image](https://user-images.githubusercontent.com/70581043/141314157-261f0a57-c4b1-4e46-bb60-8a2cabfc4ac7.png)
다양한 loss값을 사용해서 결과를 비교 : L1만 사용하면 blurry, cGAN만 사용하면 훨씬 더 sharper 한 결과가 나옴, L1과 cGAN 같이 사용할 때 좋은 결과가 나온다.
![image](https://user-images.githubusercontent.com/70581043/141314487-3cd9e540-ec59-4f41-a092-c8bd01c0fd7b.png)
Patch 사이즈에 따른 결과 비교 : 16x16 사이즈일 때 충분히 좋은 결과가 나왔다. patch 사이즈를 70x70으로 키우면 약간 더 선명해진다. 286x286 크기는 그다지 성능이 좋아지지 않았다. 