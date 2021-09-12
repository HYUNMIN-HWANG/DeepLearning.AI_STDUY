# Adam: A Method for Stochastic Optimization
- https://arxiv.org/abs/1412.6980
- [Submitted on 22 Dec 2014 (v1), last revised 30 Jan 2017 (this version, v9)]
- Published as a conference paper at the 3rd International Conference for Learning Representations, San Diego, 2015
- 참고 : https://ropiens.tistory.com/90

---
딥러닝 훈련할 때 많이 사용하던 optimizer 인 Adam에 대해서 알아보고자 논문을 읽기 시작!했는데 수식에 아찔했네요.... ㅠㅠ

## Summary
Adam이란?
- first-order gradients (일차 미분한 weight를 반영)
- AdaGrad와 RMSProp을 합침
- 장점1 : magnitudes of parameter updates are invariant to rescaling of the gradient
- 장점2 : its stepsizes are approximately bounded by the stepsize hyperparameter
- 장점3 : it does not require a stationary objective
- 장점4 : it works with sparse gradients
- 장점5 : it naturally performs a form of step size annealing

## Adam Algorithm
![image](https://user-images.githubusercontent.com/70581043/132985256-1da1f7f7-a741-474a-a41d-71630ba8706e.png)
1. first & second momentum, time step 초기화
2. time step을 하나씩 증가하면서 반복문 → t-1 일 때의 gradient 계산 → biased first & second moment 값 계산 → bias-correction 적용 → 최종 파라미터 가중치 업데이트

## Update Rule
- stepsizes를 잘 선택해야 한다.
![image](https://user-images.githubusercontent.com/70581043/132985399-96ed88d8-b57c-4797-9c5c-6a3e0078bb9f.png)

- a form of automatic annealing : ![image](https://user-images.githubusercontent.com/70581043/132985526-6dfd7fa1-70c7-4296-8caa-0879dfdf4023.png)를 signal-to-noise ratio(SNR)이라고 부른다. 해당 값이 작으면 stepsize는 zero에 가까워진다. 



두 가지 Upper bounds가 있다.
1) ![image](https://user-images.githubusercontent.com/70581043/132985406-3f73e8e2-d905-489e-8417-4e33e699d91b.png) 일 때, ![image](https://user-images.githubusercontent.com/70581043/132985411-fc35854a-58d3-40c9-8cb0-9316ed635690.png)
- most severe case of sparsity
- 현재 timestep을 제외하고 모두 zero
- stepsize가 크다.
 
2) 그 외 범위에서, ![image](https://user-images.githubusercontent.com/70581043/132985428-b65463c7-758f-448e-88e0-43c0f1ef0cad.png)
- less sparse cases
- stepsize가 작다


