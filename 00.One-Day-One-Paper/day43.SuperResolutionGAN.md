# Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network
- https://arxiv.org/abs/1609.04802
- [Submitted on 15 Sep 2016 (v1), last revised 25 May 2017 (this version, v5)]
-  accepted for oral presentation at CVPR, main paper + some supplementary material
---
- Super resolution 네트워크인 **SRGAN**을 제안함
![image](https://user-images.githubusercontent.com/70581043/136587937-75740055-1b04-4c4e-95a5-bb53f2602e36.png)
- 기존 Super resolution 모델들은 
> - texture detail들을 살리지 못했다.
> - MSE을 최소화시키는 걸 목표로 훈련을 시켰기 때문에 perceptual하게 좋은 결과를 보이지는 못했다.
> - Figure 3 : MSE는 pixel-wise 평균화를 시켰기 때문에 smooth하게 보인다는 특징
> - 반면, GAN은 실제 이미지와 같은 방향으로 새로운 이미지를 만들어낼 수 있다.

## Method
- Architecture
![image](https://user-images.githubusercontent.com/70581043/136588488-03141e87-4fc2-4460-a476-8c2900b7001c.png)

- Adversarial network architecture
![image](https://user-images.githubusercontent.com/70581043/136588516-1d90d0a6-cd1c-4d4d-a8fc-bdbcf44439c2.png)
generator는 최대한 실제 이미지와 유사한 이미지를 만들어, discriminator가 실제 이미지와 G가 만든 이미지를 잘 구분하지 못하도록 훈련

- Perceptual loss function
두 가지 loss로 구성되어 있음
![image](https://user-images.githubusercontent.com/70581043/136588838-98d61cdb-7e69-40cb-8184-a7e597b6785f.png)
1. Content loss
![image](https://user-images.githubusercontent.com/70581043/136589149-01f083a3-4262-4a31-8d4c-e9bda9968836.png)
pixel-wise MSE loss로 계산을 많이 하지만, perceptually 에서는 좋지 않은 결과가 나왔다. MSE 대신, VGG loss를 사용함 VGG loss는 G가 생성한 이미지와 HR이미지 간의 유클리드 거리를 의미한다.

2. Adversarial loss
![image](https://user-images.githubusercontent.com/70581043/136589220-a93adca6-3980-4522-91cf-0842af890d7e.png)

 ## Results
![image](https://user-images.githubusercontent.com/70581043/136589333-03f7fe06-e505-443b-a7a1-f699553c43e6.png)
- MSE가 PSNR에서 성능이 좋게 나오기는 했지만 perceptual을 보여주는 MOS에서는 낮은 점수를 보였다.
- SRGAN-VGG54가 가장 깊은 모델임, MOS에서 가장 좋은 성능을 보여줌
![image](https://user-images.githubusercontent.com/70581043/136589533-3e6901f4-f87e-4cfd-a943-8dc3e958e55e.png)
- SRGAN-VGG54 가 봤을 때 가장 자연스럽게 고화질로 사진이 바뀌었다.