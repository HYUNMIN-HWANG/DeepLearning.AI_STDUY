# GENERATIVE ADVERSARIAL NETWORKS FOR IMAGE-TO-IMAGE TRANSLATION ON MULTI-CONTRAST MR IMAGES - A COMPARISON OF CYCLEGAN AND UNIT
- https://arxiv.org/abs/1806.07777
- Github : https://github.com/simontomaskarlsson/GAN-MRI
- [Submitted on 20 Jun 2018]

---

## Abstract
- we evaluate two unsupervised GAN models (CycleGAN and UNIT) for image-to-image translation of T1- and T2-weighted MR images, by comparing generated synthetic MR images to ground truth images.
- We also evaluate two supervised models; a modification of CycleGAN and a pure generator model.
- It is also shown that models producing more visually realistic synthetic images not necessarily have better quantitative error measurements, when compared to ground truth data.

## 1. Introduction
그동안 데이터 증강을 하기 위한 노력
- Data augmentation  : but can only provide limited alternative data.
- GANs : to generate additional realistic training data, to improve classification performance, image-to-image translation, 아직 어떤 GAN 모델이 가장 좋다고는 말할 수 없다.
- 해당 논문에서는 T1, T2 MR images를 기반으로 image-to-image translation 성능을 비교할 것이다.

## 2. Method

### 2.1. GAN model selection and implementation
- CycleGAN and UNIT : work with unpaired training data.
- CycleGAN : CycleGAN_s and CycleGAN
    > - To investigate this, CycleGAN_s was implemented and trained supervised by adding the mean absolute error (MAE) between output and ground truth data.
    > - To investigate how the adversarial and cyclic loss contribute to the model, Generators s was also implemented.

### 2.2. Evaluation
- All the images have been registered to a common template brain, such that they are in the same position and of the same size
- All quantitative results; MAE, mu-tual information (MI), and peak signal to noise ratio (PSNR), are based on the test dataset.
- normalized한 후, division of the standard deviation and subtraction of the mean value 계산함
- To visually evaluate a synthetic image compared to a real image : absolute difference between the images, and dividing it by the real image
- Determining if the synthetic MR images are visually realistic or not was done via a perceptual study by one of the authors (Anders Eklund)

## 3. RESULTS
**Quantitative results**
- The Generators_s model outperforms the other models in all quantitative measurements.
- The performance of Cycle-GAN, CycleGAN s and UNIT is similar.
- the quantitative performance is better for T1 images


**perceptual study**
- more synthetic T1 images are labeled as synthetic compared to T2.
- UNIT shows the best performance for T1 images and CycleGAN shows the best performance for T2 images.
- greater error for the synthetic T2 images compared to the synthetic T1 images.

## 4. DISCUSSION
### 4.1. Quantitative comparison
- During training the Generators s model uses MAE as its only loss function, which creates a model where the goal is to minimize the MAE.
- This indicates that the architecture in the Simple model is not sufficiently complex for the translation.
- CycleGAN s : CycleGAN보다 T2에서의 MAE가 더 좋다.
- Cycle-GAN : T1에서의 MAE가 더 좋다.
-The CycleGAN and UNIT show similar results and it is difficult to argue why one or the other performs slightly better than the other one. 

### 4.2. Qualitative comparison
From the perceptual study > it was shown that the synthetic images have a visually realistic appearance, since synthetic images were classified as real
- T2 images were more difficult to classify than T1 images and the reason for the difference can be that the synthetic T2 images had a more realistic appearance, but also the darker nature of T2 images
- If the aim of the test would instead be to evaluate how similar the synthetic images are to the ground truth, the translated images from CycleGAN s may give better results. (하지만 assessing how realistic an image is, 평가하는 건 어렵다.)
- 하지만 지표를 만들수만 있다면 it does not necessarily generate visually realistic images.

### 4.3. Future work
if the model which creates the most visually realistic images, or the model which performs best in the quantitative evaluations, is the most suitable to use. 


---
---
---

## Summary 
그동안 데이터 증강을 하기 위한 여러 시도들이 있었고, 해당 논문에서는 MR이미지를 기반으로 GAN을 집중적으로 비교, 분석했다.
(we evaluate two unsupervised GAN models (CycleGAN and UNIT) for image-to-image translation of T1- and T2-weighted MR images, by comparing generated synthetic MR images to ground truth images.)

## Method
- CycleGAN_s : CycleGAN에 MAE 지표를 추가하여 모델이 최소 MAE 성과를 보이기 위해 훈련할 수 있도록 했다.
- Generator_s : CycleGAN에서 generator 부분만 사용함 (cyclic loss 없음)
- T1이미지를 input -> T2이미지를 output (vice versa)
- MAE 지표를 비교해 T1-과 T2- 에서 어떤 GAN 모델의 성능이 좋은지 평가한다. (추가로 mu-tual information (MI), and peak signal to noise ratio (PSNR)도 지표로 사용함)
- 그 후, 사람이 직접 보고 무엇이 합성한 사진인 것 같은지 평가하는 방식도 함 (perceptual study)

## Result
![image](https://user-images.githubusercontent.com/70581043/127760103-917c0ccb-791c-4f77-83d4-d7edfca5013a.png)
- Generator_s 성능이 가장 좋다.
- CycleGAN_s가 CycleGAN보다 T2에서의 성능이 더 좋다.
- CycleGAN와 UNIT 성능 유사함

![image](https://user-images.githubusercontent.com/70581043/127760183-fb4f42cc-90d2-45c8-ac3c-ede4fd43dfad.png)
- T2 이미지는 T1 이미지에 비해 사람이 눈으로 분석하기 어렵다. (더 어두움)
- 만약 최소 MAE를 목표로 하는 게 아닌, 사실적인 이미지 만들기가 목표로 잡고 훈련을 시켰다면 결과가 달라질 수 있을 것이라 예상
- 하지만 'assessing how realistic an image is' 지표를 만드는 게 어렵다.

---
+  UNIT 뭔지 조사 ⛳
+  'assessing how realistic an image is' 지표로 만들어진 것이 있는지 조사 ⛳