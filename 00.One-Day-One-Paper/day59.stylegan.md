# A Style-Based Generator Architecture for Generative Adversarial Networks
- https://arxiv.org/abs/1812.04948
- CVPR 2019
---
## StyleGAN
- **style transfer** 에 기반한 새로운 generator 구조를 제안함
- 이미지의 style을 조절할 수 있다.
- discriminator 그리고 loss function은 수정하지 않았다.


## Style-based generator
![image](https://user-images.githubusercontent.com/70581043/143861330-50b48ea4-c2c6-4647-878e-97aadaa00d30.png)      
기존 generator의 구조는 input latent vector (z)가 직접 Conv, upsampling을 거쳐야 한다.        
- 한계 : 고정된 input distribution (Gaussian) 에 학습 이미지의 distribution을 맞춰야 한다.
- non-linear 하게 맞춰짐, 조절하기 어렵다.


style-based generator는 z가 8층의 FC를 거쳐 **intermediate latent vector W로 변환을 먼저함** (non linear mapping) -> w는 AdaIN normalization을 사용하여 styles를 특정화한다. (x_i는 각각 normalized 됨, style y에 맞는 scalar를 사용하여 scaled 와 biased 한다.
- w가 고정되어 있지 않다.
- w를 이용하여 visual attribute 조절하기 용이해짐 **disentanglement**
    - perceptual path length : 두 vector를 interpolation할 때 얼마나 급격하게 이미지 특징이 바뀌는지에 대한 지표             
             - ![image](https://user-images.githubusercontent.com/70581043/143865339-d9df3c8d-8b25-4cca-8328-10d8fac742d0.png)      
             - 구면을 따라 중간 위치에 잡을 수 있도록 하는 방법        
             - ![image](https://user-images.githubusercontent.com/70581043/143865460-34f7202b-d96a-41d6-bf31-61301a83fa91.png)      
             - w vector끼리의 interpolation에 대해서 진행할 때는 단순하게 linear 방법으로 수행       

    - linear separability : latent space에서 attribute가 얼마나 선형적으로 분류될 수 있는지를 판단하는 것
             - classification을 만들어서 latent vector가  얼마나 linear한  subspace에 있는지를 확인한다.
             - ex) SVM, conditional entropy 값
 

## StyleGAN 특징
![image](https://user-images.githubusercontent.com/70581043/143864282-7132af79-3633-46d8-b139-e9557bc9e58e.png)        
- each style controls only one convolution
- each layer 다음에 AdaIN을 적용한다. -> 특정 layer의 style에만 영향을 끼친다.
    - AdaIN : x에 대한 평균값을 빼고, 표준편차로 나눔 (정규화) -> s(scaling) & b(bias)를 적용함 -> feature space에서의 statistic을 변경할 수 있다., y에 의해서 style이 변경된다.
- 이미지의 전체적인 이미지를 조정하는 것

## Stochastic Variation
- 사람에게 있어서 stochastic : haris, stubble, freckles, skin pores...
- 각 layer 마다 random noise를 추가함 
- noise는 오로지 stochastic 한 측면에만 영향을 준다. 

## Style Mixing
- 인접한 layer간의 style 상관관계를 줄여가는 것
- 2개의 latent vector가 있을 때 서로 섞어서 이미지를 만들 수 있도록 하는 것
- layer 개수마다 보여지는 결과 특징이 달라진다.
    - 윗부분 (Coarse style) : 이미지의 큼직한 변화가 생김
    - 중간 부분(Middle style)
    - 아랫부분(Fine) : 가장 미세하게 변화가 생긴다. / patch 크기가 작아졌기 때문에 가능해진 것

---
참고자료
- https://blog.lunit.io/2019/02/25/a-style-based-generator-architecture-for-generative-adversarial-networks/
- https://velog.io/@ghgh5317/A-Style-Based-Generator-Architecture-for-Generative-Adversarial-Networks-review