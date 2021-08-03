# Unsupervised Image-to-Image Translation Networks
- https://arxiv.org/abs/1703.00848
- code : https://github.com/mingyuliutw/unit
- [Submitted on 2 Mar 2017 (v1), last revised 23 Jul 2018 (this version, v6)]
- NIPS 2017

---

## Abstract
Unsupervised image-to-image translation aims at learning a joint distribution of images in different domains by using images from the marginal distributions in individual domains.
we make a shared-latent space assumption and propose an unsupervised image-to-image translation framework based on Coupled GANs.

## 1. Introduction
- image-to-image translation : mapping an image in one domain to a corresponding image in another domain
> - supervised setting : paired of corresponding images in different domains are available
> - unsupervised setting : there exist no paired examples showing how an image could be translated to a corresponding image in another domain

- the key challenge is to learn a joint distribution of images in different domains.
> - unsupervised setting : the two sets consist of images from two marginal distributions in two different domains, and the task is to infer the joint distribution using these images.
> - inferring the joint distribution from the marginal distributions is a highly ill-posed problem.

- shared-latent space assumption
> - assumes a pair of corresponding images in different domains can be mapped to a same latent representation in a shared-latent space
> - based on generative adversarial networks (GANs) and variational autoencoders (VAEs).
> - interacts with a weight-sharing constraint, which enforces a shared latent space, to generate corresponding images in two domains, while the variational autoencoders relate translated images with input images in the respective domains.

## 2. Assumptions
shared-latent space assumption
- a shared latent code z
- cycle-consistency

## 3 Framework
- based on variational autoencoders (VAEs) and generative adversarial networks (GANs)
### VAE.
- encoder–generator pair
- VAE1 : X1 domain {E1, G1}
- VAE2 : X2 domain {E2, G2}

### Weight-sharing.
- we share the weights of the last few layers of E1 and E2 that are responsible for extracting high-level representations of the input images in the two domains
- we share the weights of the first few layers of G1 and G2 responsible for decoding high-level representations for reconstructing the input images. 
- The shared-latent space assumption allows us to perform image-to-image translation.
- Once we could ensure that a pair of corresponding images are mapped to a same latent code and a same latent code is decoded to a pair of corresponding images

### GANs.
- G1 can generate two types of images
    1. images from the reconstruction stream ~x1!1 1 = G1(z1  q1(z1jx1))
    2. images from the translation stream ~x2!1 2 = G1(z2  q2(z2jx2)).

### Cycle-consistency (CC).
the cycle-consistency constraint in the proposed framework to further regularize the ill-posed unsupervised image-to-image translation problem.

### Learning.
수식

## 4 Experiments
### Performance Analysis.
- ADAM
- learning rate was set to 0.0001
- momentums were set to 0.5 and 0.999
- encoders consisted of 3 convolutional layers as the front-end
- 4 basic residual blocks as the back-end.
- The generators consisted of 4 basic residual blocks as the front-end
- 3 transposed convolutional layers as the back-end
- LeakyReLU

### Qualitative results.
- street scene image translation tasks including sunny to rainy, day to night, summery to snowy, and vice versa
- we found our method made the cityscape images cartoon like.

### Domain Adaptation.
labeled samples in one domain (source domain) to classify samples in a new domain (target domain) where labeled samples in the new domain are unavailable during training.

## 5 Related Work

## 6 Conclusion and Future Work
limitation
- the translation model is unimodal due to the Gaussian latent space assumption
- training could be unstable due to the saddle point searching problem


---
---
---
# Unsupervised Image-to-Image Translation Networks
- https://arxiv.org/abs/1703.00848
- code : https://github.com/mingyuliutw/unit
- [Submitted on 2 Mar 2017 (v1), last revised 23 Jul 2018 (this version, v6)]
- NIPS 2017

---

## Summary
- image-to-image translation : 한 도메인에 있는 이미지를 다른 도메인에 있는 이미지로 변환한다.  
- unsupervised setting 으로 훈련
- 서로 다른 도메인에 있는 이미지들의 joint distribution을 찾는 것이 문제
- shared-latent space 사용 : based on generative adversarial networks (GANs) and variational autoencoders (VAEs)

## Assumptions
![image](https://user-images.githubusercontent.com/70581043/127984379-b3cd23eb-9b94-4971-ba7d-d40668880c63.png)
- z : shared-latent space
- ![image](https://user-images.githubusercontent.com/70581043/127983762-f64d36ed-ec88-4e7a-bf46-4fe58e213988.png)
- ![image](https://user-images.githubusercontent.com/70581043/127983784-7797a857-b0ce-4cc9-8b54-69b10d919fad.png)
- ![image](https://user-images.githubusercontent.com/70581043/127983876-9c2d7ff6-6183-45c2-b420-1fb142475234.png)
 - F1->2 혹은 F2->1 이 가능하기 위해서는 cycle-consistency가 가능해야 한다.
 - cycle-consistency : ![image](https://user-images.githubusercontent.com/70581043/127984056-3d32f990-5771-4989-b061-654c10714341.png)
 
![image](https://user-images.githubusercontent.com/70581043/127984437-51d94745-ad66-4500-bb6c-a9d65c59214c.png)
- shared intermediate representation  h
- high-level generation function : z -> h
- low-level generation function : h -> x1, x2

## Framwork
![image](https://user-images.githubusercontent.com/70581043/127984858-c341449f-fbac-4644-8999-72cdb9438958.png)
- two domain image encoders E1 and E2, two domain image generators G1 and G2, and two domain adversarial discriminators D1 and D2.
- VAE : X1 도메인에서 input image x1 -> Encoder1 -> latent space Z -> Generator -> reconstructed image x(1->1) (vice versa)
![image](https://user-images.githubusercontent.com/70581043/127985710-76258f85-ffb0-4a64-a014-24d90fece06a.png)
![image](https://user-images.githubusercontent.com/70581043/127985820-5c71f662-dc34-4b80-b957-8bbb00054036.png)
- Weight-sharing. : 
> - E1, E2 마지막 층에 있는 가중치 공유함 >  인풋 이미지의 high-level representations 특징을 추출할 수 있다.
> - G1, G2 처음 층에 있는 가중치를 공유함 > 재생산한 인풋이미지의  high-level representations 특징을 추출할 수 있다. 
> - image translation stream : x1 이미지를 넣어서 x2 이미지로 변환하는 것도 가능함 ![image](https://user-images.githubusercontent.com/70581043/127986644-b40d3323-cc89-497a-bb12-5e4aaedf4660.png)
- GAN : 
> - 1. 같은 이미지를 reconstruction 하는 것  ![image](https://user-images.githubusercontent.com/70581043/127987009-c6751edd-b164-41ed-b285-a22ec57603a0.png)
> - 2. 다른 이미지로 변환하는 것 ![image](https://user-images.githubusercontent.com/70581043/127987040-f7013fa9-1412-4358-b718-ff4118322be9.png)
- 종합 
![image](https://user-images.githubusercontent.com/70581043/127987243-897a8f83-7812-4a20-9157-f1615c4d477f.png)

## Result
![image](https://user-images.githubusercontent.com/70581043/127987469-d9b5c508-741b-4afa-828c-7ffda4145dae.png)
day to night / night to day
- it achieved the best performance of 0.600 average pixel accuracy.
- limitation
> - the translation model is unimodal due to the Gaussian latent space assumption
> - training could be unstable due to the saddle point searching problem