# Noise2Noise: Learning Image Restoration without Clean Data
- https://arxiv.org/abs/1803.04189
- [Submitted on 12 Mar 2018 (v1), last revised 29 Oct 2018 (this version, v3)]
---
## Summary
**noise2noise** : noise를 제거하는 모델, train data도 noise 이미지이고 target data도 noise 이미지! clean image 없이 노이즈를 제거한다. (In this work, we observe that we can often learn to turn bad images into good images by only looking at bad images)

- 기존의 noise 제거하는 방식 : 노이즈 이미지 x와 clean 이미지 y를 pair해서 훈련시킨다.
![image](https://user-images.githubusercontent.com/70581043/135717275-f72bc83e-1e84-40e6-a40a-47051326e0c8.png)





- 해당 논문에서 제시하는 방식 : 노이즈 이미지 x와 노이즈 이미지 y를 pair 해서 훈련시킨다.
![image](https://user-images.githubusercontent.com/70581043/135717468-d2c2980d-0e56-463c-a5f9-198543c4cae4.png)
- clean 이미지 y는 노이즈 이미지 x에 대한 노이즈 이미지 y가 나오는 조건에서의 평균 값
![image](https://user-images.githubusercontent.com/70581043/135717530-88da21ac-7e95-4412-8bd3-cac988be2013.png)


### Addictive Gaussian Noise
- noise  평균 : zero -> L2 loss를 사용한다.
- RED30이라는 모델 사용 (image restoration tasks 로 많이 사용됨)
- standard deviation이 ![image](https://user-images.githubusercontent.com/70581043/135717704-d014225f-91d2-4848-bd27-500dbe9f244a.png) 되도록 노이즈를 randomize한다.
## 결과
![image](https://user-images.githubusercontent.com/70581043/135717793-b33050fe-6e38-43e0-81b6-1f2d83f84c5c.png)
noisy tareget으로 훈련한 결과, clean target으로 훈련한 것과 큰 차이가 없었다.
![image](https://user-images.githubusercontent.com/70581043/135717989-e77aef26-40b4-4763-b04b-6021c4478c25.png)
noisy image 로 훈련한 결과 PSNR 31.74dB , clear image로 훈련한 결과 PSNR 31.77dB ==> 거의 비슷함