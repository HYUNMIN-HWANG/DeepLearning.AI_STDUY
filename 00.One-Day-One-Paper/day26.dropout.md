# Dropout: A Simple Way to Prevent Neural Networks from Overfitting
- https://jmlr.org/papers/v15/srivastava14a.html
- Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, Ruslan Salakhutdinov; 15(56):1929−1958, 2014.
---
총 30페이지..ㅎㅎ 오늘은 개념 정리하고, 내일은 결과 부분 읽겠습니다.

## Summary
dropout 기법을 사용함으로써 overfitting을 막을 수 있고, neural network를 다양하게 조합하면서 다양한 architecture를 만들 수 있다.

  ---
![image](https://user-images.githubusercontent.com/70581043/131343895-e1907f94-472f-4c2d-90dc-1f964ea20b2c.png)
(a) drop out을 적용하지 않은 architecture
(b) drop out을 적용한 'thinned net' (train을 할 때마다 dropout할 노드가 랜덤하게 정해진다. 2의 n승 개의 모델 구조를 만들 수 있다. weight를 공유한다.)

---
![image](https://user-images.githubusercontent.com/70581043/131344049-83fa22d7-f05f-423b-b57c-ecbd094e27b6.png)
- train 단계 : train을 할 때마다 dropout할 노드가 랜덤하게 정해진다. 2의 n승 개의 모델 구조를 만들 수 있다. weight를 공유한다.
- test 단계 : approximate averaging method, test 단계에서는 dropout이 없다. train할 때 확률 p를 보유하고 있다면 test 에서는 weight에 p를 곱한다.

---
![image](https://user-images.githubusercontent.com/70581043/131345186-70ecce59-8287-40bb-ba67-fcd26632206e.png)
![image](https://user-images.githubusercontent.com/70581043/131345214-4ad7e1a8-5a6b-447c-a869-05c7cbcca0a4.png) : Bernoulli random variables each of which has probability p of being 1.
![image](https://user-images.githubusercontent.com/70581043/131345368-5aebb960-70f6-4b16-9b25-9d7f12c79798.png) : thinned output, input og the next layer
![image](https://user-images.githubusercontent.com/70581043/131345421-3ac5d94b-2e44-48e1-bbf5-701f91a829ee.png) : inputs into layer l+1
![image](https://user-images.githubusercontent.com/70581043/131345568-0c2048a2-ab39-4a01-9685-4678ba04abae.png) : apply activation function


---

## Results
### MNIST
![image](https://user-images.githubusercontent.com/70581043/131697758-686151d7-a31e-4b43-8a32-6f367d876e2e.png)
- Deep Boltzmann Machines : pretrained dropout nets일 때 가장 error 가 작았다.

### CIFAR10 and CIFAR100
![image](https://user-images.githubusercontent.com/70581043/131698710-26e4f0b5-22f0-461f-a62a-bb89b0a02ad4.png)
- CIFAR10 : FC 다음에 dropout -> 모든 레이어에 dropout -> RELU  대신에 maxout 일 때 성능이 가장 좋았다.
- CIFAR100 : 모든 레이어에 dropout

### IMAGENET
![image](https://user-images.githubusercontent.com/70581043/131699360-c03abd0b-9b56-4c9c-a4dd-0b11ccfc6a69.png)
- 보통 26%의 error rate를 보여주는데, dropout을 적용함으로써 16.4%까지 떨어졌다

> 그 외, Speech Recognition, document classifier 에서도 dropout을 적용했을 때 좋은 성능을 보였다.

## 다른 모델과의 비교
- Bayesian Neural Network와 비교했을 때, dropout을 사용했을 때 더 빠르게 성능을 처리할 수 있었고 regularizing 효과도 볼 수 있었다.
- Standard Regularizers 인 L2 등등과 비교를 했을 때, dropout 또한 regularizer 기능을 수행할 수 있다.

## Dropout의 효과
- detect edges, strokes, spots 할 수 있다.
- 한계점 : activations of the hidden units become sparse.
- train할 때 시간이 오래 걸린다.
