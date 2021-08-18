# Improved Techniques for Training GANs
- https://arxiv.org/abs/1606.03498
- [Submitted on 10 Jun 2016]
- Machine Learning (cs.LG); Computer Vision and Pattern Recognition (cs.CV); Neural and Evolutionary Computing (cs.NE)

---

초창기 GAN, 모델 평가 방법에 대해서 제시했다.

## 1. Introduction
준지도 학습과 샘플생성 성능을 향상시켜 , GAN 모델이 더 잘 수렴할 수 있는 기술을 제안한다. 

## 2. GAN Training
GAN을 훈련시키는 것은 두 player 간(생성자, 판별자)의 비협조적(적대적) 게임으로 Nash equilibrium을 찾는 것으로 이루어져있다.
- **Nash equilibrium** : 전통적인 gradient-based minimization 기술을 사용하여 각각의 모델에 최소 비용을 사용하는 아이디어에서 모티브되었다. 생성자와 판별자 모델이 최소 cost를 갖을 때 발생, // 하지만 생성자 cost를 줄이면 판별자 cost는 늘어나는 등 잘 수렴이 안 되었음

### 2-1) Feature matching
판별자의 overfitting을 방지하기 위해 생성자에 새로운 목표를 지정하는 불안정한 GAN을 제안한다. 불안정한 GAN일 때 더 효과적인 결과가 나온다. 생성자는 실제 데이터 통계적으로 가까워진다. 판별자는 생성자가 생성한 이미지가 통계적으로 의미가 있는지 판별한다.

### 2-2) Minibatch discrimination
GAN 모델 중, 항상 같은 포인트로 파라미터가 세팅이 되는 경우 생성자가 붕괴되면서 GAN 훈련이 실패된다. 이때 판별자는 실제 데이터와 유사하다고 판별한다. 이를 해결하기 위해서 minibatch discrimination 를 해야 함 → 판별자 모델에 batch normalization을 적용함 → 생성자와 훈련데이터로부터 minibatch 끼리 계산한 후 → 판별자에서 각각의 예시들이 얼마나 훈련 데이터에 가까운지 하나의 값으로 아웃풋을 내야 한다.

### 2-3) Historical averaging
파라미터의 Historical averaging은  온라인 방식으로 업데이터를 할 수 있기 때문에 긴 시계열 데이터에 잘 업데이트 된다.

### 2-4) One-sided label smoothing
![image](https://user-images.githubusercontent.com/70581043/129902471-b3754c5f-9f39-4873-a447-f2e6e476377c.png)

Label smoothing은 0과 1로 타겟을 구분했던 것을 0.9와 0.1 값으로 대체하는 것이다. positive labels일 때는 판별자가 alpha 값에 가까워지고, negative label일 때는 0에 가까워진다.

### 2-5) Virtual batch normalization
- Batch normalization의 단점 : 같은 minibatch에 있는 다른 인풋들로부터 의존적인 아웃풋이 나온다.
- virtual batch normalization (VBN) : reference batch(한 번만 선택회고 훈련시작할 때 고정된다. x 그 자체임)로 샘플 x들을 정규화한다. generator 네트워크에서만 사용한다.

## 3. Assessment of image quality
> human annotators : 사람이 생성된 데이터와 실제 데이터를 구분하는 지표
> 사람이 직접 하는 것 말고 자동으로 계산해주는 지표를 제안한다.
![image](https://user-images.githubusercontent.com/70581043/129911979-f2768cce-f731-483f-be52-31b7268e7b93.png)

- Inception model : 모든 생성된 이미지가 갖는 conditional label distribution p(y|x) → 낮은 entropy가 오면 의미 있는 object인 것 >> measure the “objectness” of a generated image.

## 4. Semi-supervised learning
- softmax를 적용해서 확률을 구한 다음, cross-entropy가 최소값이 되도록 훈련시킨다.
- semi-supervised learning
> - 생성자에서 만든 샘플을 원래의 데이터 셋에 추가한다. (y = K + 1,라고 라벨링)
> - ![image](https://user-images.githubusercontent.com/70581043/129904845-e66357b7-884d-4dae-8afd-24c7c395aa60.png) x가 가짜일 확률 = 1 - D(x)
> - 훈련데이터 중 절반은 실제 데이터고 절반은 생성자에서 만든 이미지를 임시로 넣는다.

## Result
- MINIST
![image](https://user-images.githubusercontent.com/70581043/129909424-19f7e410-79f6-4e4a-8f65-b5f1f8d914b7.png)

> - 20, 50, 100 및 200개의 레이블이 지정된 예제 → 이들 중 무작위로 선택한 부분으로 semi-supervised
> - 레이블이 지정된 10개의 무작위 하위집단으로 평균을 냄 (각각의 클래스마다 동일한 수의 데이터로 구성됨)
> - 나머지 이미지들은 레이블 없이 제공됨
> - 결과 : minibatch discrimination을 했을 때 성능이 좋았다.

## Conclusion
기존 GAN은 모델을 평가할만한 적절한 metric이 없었다. 해당 논문에서는 GAN 훈련을 안정화할 수 있는 몇 가지 기술들을 제안했다. Inception 점수는 모델의 품질을 비교하기 위한 기초를 제공한다.