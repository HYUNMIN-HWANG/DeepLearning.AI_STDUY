# Generative Adversarial Networks
- https://arxiv.org/abs/1406.2661
- NIPS 2014
---
GAN의 시초가 되는 페이퍼를 읽어보았습니다. 증명 위주로 설명이 되어 있다보니 생각보다 쉽지 않았네요...

---
적대적인 과정을 통해 생성 모델을 추정하는 프레임워크를 제안했다.  두 가지 모델이 필요함, 두 모델 간의 minmax게임을 하는 것 같음
- G (generative model) : captures data distribution
- D (discriminator model) : 샘플이 G가 아닌 training data에서 온 것인지 확률을 추정

G가 training data distribution을 갖고, D가 1/2 확률을 갖고 있을 때 unique solution 이 존재한다고 할 수 있다.      
적대적 생성망은 multi-layer perceptrons로  정의하고, backpropagation으로 훈련된다. 그 외 Markov chian이나 unrolled approximate inference는 필요하지 않다. 

---
![image](https://user-images.githubusercontent.com/70581043/140609138-922ff5ae-6335-4ced-bf20-f260945bfbe5.png)
D 는 training samples와 generative samples에 맞는 할당을 잘 할 수 있도록 '최대화'시키도록 훈련시키고, G 는  log(1-D(G(z)))를 '최소화' 시키도록 훈련시킨다.

![image](https://user-images.githubusercontent.com/70581043/140609242-1a22bb07-b365-4582-bcc9-d8c796e399ff.png)
K 번 discriminator를 업데이트 시킨 후, 1번 generator를 업데이트 시킨다.

### Global Optimality of p_g = p_data
G가 고정되었을 때, 최적의 판별자 D는 다음과 같다.
![image](https://user-images.githubusercontent.com/70581043/140609963-bdcff1e6-87ed-4c76-825b-abfd836c3417.png)
어떤 생성자 G가 주어졌을 때, 판별자 D 학습은 V(G,D)를 최대화시키는 것이다.
![image](https://user-images.githubusercontent.com/70581043/140610013-58b33b28-1e3f-4617-886a-4f9fdcba6199.png)
y → a log(y) + b log(1-y)는 0과 1사이에서 a / a+b일 때 최대값을 갖는다. D는 조건부확률 P(Y=y|x)를 추정하는 log-likelihood를 최대화하는 것. train data에서 온 x는 y=1, G에서 온 x는 y=0이라고 표현한다.
![image](https://user-images.githubusercontent.com/70581043/140610170-4ffa52a8-d678-4d8d-a9c9-cfc287e38860.png)

### global minimum C(G)는 p_g = p_data일 때 달성된다. 이때, C(g)의 값은 -log4이다.
 p_g = p_data 이라면, D(x) = 1/2가 된다.  따라서 아래 식을 충족시킴
![image](https://user-images.githubusercontent.com/70581043/140610245-88778338-6a89-4560-9df2-2dbab6b91bae.png)

### Convergence
판별자는 주어진 G에 대해서 최적점에 도달 -> p_g도 향상된 기준으로 업데이트 될 수 있다. -> 즉, p_g는 p_data로 수렴
![image](https://user-images.githubusercontent.com/70581043/140610369-0c110a38-57d8-480c-96f7-cf407bae8dec.png)
이는, 최적의 D와 이에 상응하는 G가 있을 때 p_g에 대한 gradient descent updata 계산하는 것과 같음. p_g에 대한 작은 업데이트를 하면, p_g는 p_x에 수렴

---
### Experiment
- Generative model : ReLU, sigmoid activation
- Discriminator model : maxout, (학습할 때 dropout 적용)
- 생성자 모델의 가장 마지막 레이어에만 노이즈를 사용함


### Advantages, Disadvantages
- Disadvantages
   - P_g(x)에 대한 명시적 표현이 없다.
   - D는 G가 훈련하는 동안 synchronized 되어야 한다. (D 업데이터 없이, G를 너무 많이 학습시키면 안됨, G가 collapse된다.)
- Advantages
   - Markov chain이 필요없다. 오로지 backprop만 사용해서 gradient를 얻는다.
   - 학습하는 동안 inference가 필요없다. 
   - 다양한 함수에 통합될 수 있다.
   - data examples 자체를 업데이트 시키는 것이 아니라 discriminator를 통해서 나온 gradient로 업데이터 시킨다.
   - 다른 생성모델과는 다르게, 되게 sharp한 결과가 나온다.