# Squeeze-and-Excitation Networks
- https://arxiv.org/abs/1709.01507
- [Submitted on 5 Sep 2017 (v1), last revised 16 May 2019 (this version, v4)]
- journal version of the CVPR 2018 paper, accepted by TPAMI
---
## Summary
기존 모델들 : **features**들 간의 spatial correlation을 통합함으로써 훈련시킨다.
“Squeeze-and-Excitation” (SE) block : channel-wise feature responses by explicitly modelling interdependencies between _**channels**_. (channel-wise relationship)


![image](https://user-images.githubusercontent.com/70581043/135836519-75562521-028f-4210-8288-3bd078e82c1e.png)
- ![image](https://user-images.githubusercontent.com/70581043/135836561-11f7b6cb-f304-4556-bf8c-27047868491f.png) : X (input)을 U(feature map)으로 매핑시켜준다.
- SE Block에는 2 가지 처리 과정이 있음
1. **squeeze operation** : squeeze global spatial information into a channel descriptor, using global average pooling
![image](https://user-images.githubusercontent.com/70581043/135837317-2026cec4-f2ef-4210-bb61-c28d0a3d296c.png)

2. **excitation operation** : U에서 나온 feature map에 Weight를 곱한다.
![image](https://user-images.githubusercontent.com/70581043/135837593-f91618c1-8886-402d-8250-84bc9b8d4041.png)
마지막 아웃풋은 s와 U를 곱해서 rescale 한 결과를 출력한다.
![image](https://user-images.githubusercontent.com/70581043/135838179-40624420-228f-4353-a2a4-1c13470a45bb.png)

## Results
![image](https://user-images.githubusercontent.com/70581043/135838297-a4f4c3ba-e736-490f-ac6c-d3d16d38eed9.png)
cifar10 과 cifar100 데이터 셋을 적용했을 때, 가존 모델들보다 에러가 더 적게 나온 결과를 보임


