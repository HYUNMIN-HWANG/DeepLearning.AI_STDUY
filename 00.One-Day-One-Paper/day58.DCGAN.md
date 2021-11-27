# Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks
- https://arxiv.org/abs/1511.06434
- ICLR 2016
---
##  Deep Convolutional Generative Adversarial Networks (DCGAN)
### DCGAN의 가장 큰 특징 4가지
1. Convolutional을 사용한 GANs
2. 훈련시킨 discriminators 사용하여, unsupervised algorithms 성능을 비교
3. visualize the filters by GANs
4. vector arithmetic properties


### Architecture의 특징
![image](https://user-images.githubusercontent.com/70581043/143674386-f35d74c5-27f0-4730-89b4-685a8248ac82.png)
1. 모든 Convolutional net에 있는 pooling layer들을 strided convolution으로 대체한다.
2. 모든 fully-connected layer를 제거함
3. batch normalization을 사용함 ; 모든 layer마다 사용하지는 않았고, generator의 output layer와 discriminator의 input layer에서는 사용하지 않았다.
4. ReLU activation : generator의 마지막 층을 제외하고 ReLU가 사용됨
5. Leaky ReLU activation : discriminator에 사용됨, 특히 higher resolution modeling일 때 잘 작동한다.



### Results
#### 1. NOT MIMICKING TRAIN DATA 
- using LSUN dataset
이건 1epoch일 떄의 결과,       
생성된 이미지들이 그다지 좋은 결과를 보이지 못함, 이는 해당 모델이 training data를 momorize해서 학습시키는 게 아니라는 것임    
![image](https://user-images.githubusercontent.com/70581043/143675122-4560967a-6f53-440a-a0b2-71d38b860430.png)

이건 5 epochs일 때의 결과,       
해당 모델이 단순히 train data를 overfitting/memrizing해서 고화질의 이미지를 생성하는 것은 아니라는 걸 증명함    
![image](https://user-images.githubusercontent.com/70581043/143675127-1ec2a2fe-2c80-4665-b250-30d758c372b8.png)

#### 2. WALKING IN THE LATENT SPACE
![image](https://user-images.githubusercontent.com/70581043/143675217-d5794e58-4613-4618-9b9a-242f6c1b9c65.png)
- z 벡터에 따라 서서히 바뀐다.

#### 3. VISUALIZING THE DISCRIMINATOR FEATURES
![image](https://user-images.githubusercontent.com/70581043/143675315-76a2c8fe-5577-4b4c-806d-8c2ed7b38d3b.png)
- using guided backpropagation > discriminator가 학습한 내용이 뭔지 볼 수 있다.


#### 4. VECTOR ARITHMETIC ON FACE SAMPLES
![image](https://user-images.githubusercontent.com/70581043/143675436-a9ddbd75-dbdc-4d1d-854d-e09a711b4dc8.png)
- vector들을 간단하게 계산할 수 있다.
- conditional generative models : 특정한 scale, rotation, position을 학습한다는 걸 이용
- 하나하나의 샘플로 실험하면 unstable함, 대신 3개의 샘플들을 평균한 z 벡터는 안정적인 generation결과를 보인다.
