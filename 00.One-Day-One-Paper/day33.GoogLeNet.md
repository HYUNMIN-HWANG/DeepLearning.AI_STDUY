# Going deeper with convolutions
- https://arxiv.org/abs/1409.4842
- [Submitted on 17 Sep 2014]
---
## Summary
2014년 ILSVRC14 에서 우승한 모델인 GoogLeNet 에 대한 논문이다. 해당 모델에서는 연산량을 줄이면서 이미지 정보를 잘 추출할 수 있는 **Inception** 모듈을 제안했다.

- Motivation : 그동안 딥러닝 네트워크의 성능을 높이기 위해서는 depth를 늘리고, width를 늘렸다. 하지만 ① 네트워크 사이즈가 커질 수록 parameter 수가 늘어나고, 늘어난 네트워크는 overfitting될 가능성이 높다. 또한 ② 네트워크 사이즈가 커지면 어마어마하게 computational resources가 필요하다. 거의 제곱 배로 늘어난다.
- 이를 해결하기 위해서 Fully connected 대신  sparse connected 사용함 : 근데 sparse connected 자료구조는 computing 계산을 할 때 비효율적
- 이런 문제들을 커버할 수 있는 Inception Module 제안함 : sparse와 dense 를 모두 사용한 아키텍처
- 1 X 1 convolution layer 의 특징
> -  dimension reduction modules to remove computational bottleneck
> - not just increasing the depth, but also the width of our networks without significant performance penalty

## Inception Module
![image](https://user-images.githubusercontent.com/70581043/133710294-c50cc26e-bd8b-4e65-b921-54d5df115b76.png)
- finding out how an **optimal local sparse structure** in a convolutional vision network can be approximated and covered by readily **available dense components**.
- the optimal local construction and to repeat it spatially.
- 1X1 convolutions are used to compute reductions before the expensive 3X3 and 5X5 convolutions
- it allows for increasing the number of units at each stage significantly without an uncontrolled blow-up in computational complexity.
- increasing both the width of each stage as well as the number of stages without getting into computational difficulties

## GoogLeNet
![image](https://user-images.githubusercontent.com/70581043/133710997-c6aa76a7-eb6c-455b-af19-fa7eefc318b9.png)
- 22 layers
- 9 inception
- auxiliary classifier : average pooling -> FC -> dropout -> softmax loss 