# InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets
- https://arxiv.org/abs/1606.03657
- [Submitted on 12 Jun 2016]
---
## Summary
**InfoGAN**(information-theoretic extension to the Generative Adversarial Network :  
- able to learn _disentangled representations_ in a completely _unsupervised manner_.
- maximizes the _mutual information_ between a small subset of the latent variables and the observation.

## InfoGAN
- 기존 GAN 모델에서는 simple factored continuous input noise vector z 를 사용해서 새로운 이미지를 생성했다. → 문제점 : highly entangled way, not correspond to semantic features of the data
- 제안 : 이미지의 카테고리를 표현하는 discrete random variable 와 함께 이미지의 semantic feature 특징을 담는 additional continuous variables 을 추가한다.
- 오로지 unsupervised learning으로만 훈련
- information-theoretic regularization : there should be high mutual information between latent codes c and generator distribution G(z, c). →  I(c;G(z, c)) should be high
> - I(X;Y) : measures the “amount of information” Y를 관찰했을 때 X의 불확실성이 감소하는 정도
> - X와 Y가 독립이라면 I(X;Y)=0
- information-regularized minimax game 
![image](https://user-images.githubusercontent.com/70581043/134790623-5f21274f-ea91-4b77-a8fc-f3be9a59b67a.png)
- 목표는 위 mutual Information을 극대화하는 것
- variational lower bound, LI (G,Q) 정의함
![image](https://user-images.githubusercontent.com/70581043/134790661-bb14d07d-b3c8-4f71-8edd-d9a29cf84823.png)
- 최종 InfoGAN : minimax game with a variational regularization of mutual information and a hyperparameter lambda:
- ![image](https://user-images.githubusercontent.com/70581043/134790681-c6fd01a3-8233-4dea-adf5-535fd19e05ff.png)

## Result
- MNIST
![image](https://user-images.githubusercontent.com/70581043/134790703-4f72a26d-f139-4604-b7f8-eb79e164ea9b.png)
> discrete code c1 : cpatures drastic change in shape (0~9 숫자를 구분)
> continuous code c2, c3 : rotation of digit and controls the width → 단순히 늘리는 것이 아니라 자연스럽게 보이도록 조정되어있다. 
- 3D face dataset
![image](https://user-images.githubusercontent.com/70581043/134790774-6d1b25e0-61b2-4962-99d8-a2e72547d6f6.png)
>  continuous latent vector : azimuth (pose), elevation, and lighting , 기존 다른 GAN 모델과 다르게 unlabeled data만으로도 자연스럽게 face width를 바꿀 수 있었다.