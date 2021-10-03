# StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation
- https://arxiv.org/abs/1711.09020
- [Submitted on 24 Nov 2017 (v1), last revised 21 Sep 2018 (this version, v3)]
- IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 8789-8797
---
## Summary
**StarGAN** : image-to-image translations for multiple domains using only a single model. 하나의 모델로 여러 스타일의 이미지로 변환하는 모델을 제안한다.
![image](https://user-images.githubusercontent.com/70581043/135754341-089c8936-869a-4bca-9182-47b7309a26b1.png)
- 기존 Style transfer GAN의 특징들
> Figure2 (a)
>  K domain의 스타일로 사진을 바꿀려면 K(K-1) 개의 generator가 필요함
> 한 모델에 하나의 스타일만 학습할 수 있다.

- StarGAN
> Figure(b)
> 훈련할 때 multiple domain을 학습한다. 
> 하나의 generator로 여러 domain에 매핑할 수 있다.

## Star Generative Adversarial Networks
1) Multi Domain Image to Image Translation
![image](https://user-images.githubusercontent.com/70581043/135754546-4cb2a130-2a48-4a96-8379-69b814c9a96e.png)

> - input : image (x) & domain label (c) 두 개를 인풋으로 넣는다.
> - output : image (y)

 
![image](https://user-images.githubusercontent.com/70581043/135754558-80c1bc57-b873-4978-9858-f882cc2f3369.png)

> - a domain classification loss of real images used to optimize D
> - real image와 실제 domain label 값을 페어시킴

![image](https://user-images.githubusercontent.com/70581043/135754611-4166f01a-8fd2-44ee-be60-b07a84567aab.png)

> - a domain classification loss of fake images used to optimize G.
> - fake image와 target domian label  값을 페어시킴


![image](https://user-images.githubusercontent.com/70581043/135754652-db54e18b-7a63-43f0-b743-4e0d582188fb.png)

> - Reconstruction Loss (cycle consistency loss)


2) Training with Multiple Datasets
- 하나의 데이터 셋이 아닌 두 개의 데이터 셋을 같이 훈련시키기 위한 장치.
- mask vector m : allows StarGAN to ignore unspecified labels and focus on the explicitly known label provided by a particular dataset.

## Results
1) CelebA datastet
![image](https://user-images.githubusercontent.com/70581043/135754794-1383d4d0-5164-4e4d-93d8-c721dee217b1.png)
- 다른 모델들은 원하지 않는 도메인이 바뀌거나 부자연스러운 결과를 보인 반면 StarGAN은 꽤 좋은 결과를 보임
- 이유 : 다른 모델들은 fixed translatrion이다 보니 overfitting되는 경우들이 많다.  StarGAN은 유연하게 다른 라벨 값으로 변환할 수 있다보니 좋은 결과를 보임

2) ReFD dataset
![image](https://user-images.githubusercontent.com/70581043/135754870-df2afc15-a9a8-4b32-b48c-907868dd9f07.png)
- StarGAN에서 좋은 결과를 보인다.
- 이유 : 데이터셋 자체가 워낙 작은 이미지들이라서 train 된 이미지가 적다. 하지만 starGAN에서는 멀티 태스크를 수행하면서 데이터를 augmentation 했기 때문에 데이터 수가 적은 문제를 극복할 수 있었다.

3) CelebA datastet +  ReFD dataset
![image](https://user-images.githubusercontent.com/70581043/135754926-703f01f8-fc78-4544-b343-05b6e724b32d.png)
- first row가 논문에서 제안한 모델
- 한 번에 두 가지 dataset으로 훈련을 시켰음
- starGAN properly learned the intended role of a mask vector in image-to-image translations when involving all the labels from multiple datasets altogether.
