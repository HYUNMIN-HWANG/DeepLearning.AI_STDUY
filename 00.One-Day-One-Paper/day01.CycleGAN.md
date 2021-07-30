# Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks
- https://arxiv.org/abs/1703.10593
- [Submitted on 30 Mar 2017 (v1), last revised 24 Aug 2020 (this version, v7)]
- ICCV 2017 paper

---

## Abstract

기존 image-to-image의 한계 : paired training data will not be available.
해당 논문의 제안 : image-to-image in the absence of paired examples.
결과 : style transfer, object transfiguration, season transfer,photo enhancement

## 1. Introduction

논문 핵심 : capturing special characteristics of one image collection and figuring out how these characteristics could be translated into the other image collection, all in the absence of any paired training examples.

- G : X -> Y
- F : Y -> X

We apply this structural assumption by training both the mapping G and F simultaneously, and adding a 'cycle consistency loss' that encourages
F(G(x)) ~= x and G(F(y)) ~= y.

## 2. Related work
### Generative Adversarial Networks (GANs)
adversarial loss : forces the generated images to be, in principle, indistinguishable from real photos.

### Image-to-Image Translation
“pix2pix” framework : uses a conditional generative adversarial network to learn a mapping from input to output images.

### Unpaired Image-to-Image Translation
the input and output to share specific “content” features even though they may differ in “style“.

### Cycle Consistency
cycle consistency loss , back translation and reconciliation 

### Neural Style Transfer
image-to-image translation, which synthesizes a novel image by combining the content of one image with the style of another image

## 3. Formulation
G : X -> Y
F : Y -> X
discriminators Dy :  distinguish between images {y} and translated images {G(x)}
discriminators Dx :  distinguish between images {x} and translated images {F(y)}

### 3.1. Adversarial Loss
min_G max_DY L_GAN(G;D_Y ;X; Y )
min_F max_DX L_GAN(F;D_X; Y;X)

### 3.2. Cycle Consistency Loss
forward cycle consistency : x -> G(x) -> F(G(x)) ~= x
backward cycle consistency : y -> F(y) -> G(F(y)) ~= y


### 3.3. Full Objective

## 4. Implementation
### Network Architecture

### Training details

## 5. Results
### 5.1. Evaluation
Using the same evaluation datasets and metrics as “pix2pix”

### 5.1.1 Evaluation Metrics
- AMT perceptual studies : to assess the realism of our outputs
- FCN score : how interpretable the generated photos are according to an off-the-shelf semantic segmentation algorithm
- Semantic segmentation metrics : per-pixel accuracy, per-class accuracy, and mean class Intersection-Over-Union

## 6. Limitations and Discussion

---

Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks
- https://arxiv.org/abs/1703.10593
- [Submitted on 30 Mar 2017 (v1), last revised 24 Aug 2020 (this version, v7)]
- ICCV 2017 paper

---

![image](https://user-images.githubusercontent.com/70581043/127602042-0035d69a-bc6e-4e74-bcd0-cabd4319bcd7.png)

### Abstract : 
기존 image-to-image로는 paired training data가 많이 없다는 한계가 있었다. 해당 논문은 이러한 한계를 극복하기 위해서 paired examples가 없어도 이미지 변환을 할 수 있는 모델을 제안한다. 위 그림과 같이 paried data는 같은 그림이지만 스타일만 다른 데이터가 있어야 한다. 하지만 해당 논문에서 하고자 하는 것은 Unpaired 처럼 완전히 다른 대상으로 변환하고자 함.

### 논문 핵심 : 
**capturing special characteristics of one image collection and figuring out how these characteristics could be translated into the other image collection, all in the absence of any paired training examples**

### 모델구조 : 
![image](https://user-images.githubusercontent.com/70581043/127602207-8d7acde1-78da-4058-ae97-f06034be1880.png)
(a)      
![image](https://user-images.githubusercontent.com/70581043/127602405-9e193bbe-e11a-41f8-87d1-5844015cdde8.png)

(b) forward cycle consistency : 인풋 x → 새로운 이미지 생성 → 다시 원래 이미지로 반환 → x와 비슷해야 함      
![image](https://user-images.githubusercontent.com/70581043/127602384-961467a4-800a-4d83-9d1a-df404db1ea49.png)

(c) backward cycle consistency : 인풋 y → 원래의 이미지 반환 → 새로운 이미지 생성 → y와 비슷해야 함       
![image](https://user-images.githubusercontent.com/70581043/127602475-08758695-9d94-43bb-965d-916d08178b22.png)

