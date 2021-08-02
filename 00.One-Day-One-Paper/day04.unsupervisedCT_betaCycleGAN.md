# Unsupervised CT Metal Artifact Learning using Attention-guided beta-CycleGAN
- https://arxiv.org/abs/2007.03480
- [Submitted on 7 Jul 2020]
- IEEE Trans. on Medical Imaging

---

## Abstract
- we propose a much simpler and much effective unsupervised MAR method for CT. 
- novel -cycleGAN architecture
- attention mechanism is the key element to effectively remove the metal artifacts. by adding the convolutional block
- attention module (CBAM) layers with a proper disentanglement parameter, experimental results confirm that we can get more improved MAR that preserves the detailed texture of the original image.

## 1. INTRODUCTION
- the more serious problem in dental CT is the typical placements of metallic implants and dental fillings that can cause severe metal artifacts.
- In the imaging of patients with metallic inserts, X-ray photons cannot penetrate the metallic object consistently due to the object’s high attenuation.
- Other reasons such as beam-hardening or poor signal to noise ratio (SNR) can contribute to metal artifacts
- several works using deep learning for MAR have been proposed
> - applied the pix2pix model : prior image by a convolutional neural network (CNN) -> sinogram network and the image network by learning two CNNs (supervised manner)
> - cycle-consistent adversarial network (CycleGAN) :  unsupervised image-to-image translation task, only a single generator is necessary at the inference stage, which makes the algorithm simple.
- they are radiated from a few metalic regions. -> network by focusing only where the artifacts exist and how their patterns appear.
> - attention mechanism in human visual system
> - convolutional block attention module (CBAM)
- we propose an attention-guided unsupervised MAR method using the cycleconsistent adversarial network with CBAM.
- introduction of the parameters to control the level of feature disentanglement. 
- we control the level of the importance in terms of the statistical distances in the original and target domains using a weighting parameter .

## 2. RELATED WORKS
### A. Conventional methods
- classical MAR algorithms
> - the sinogram modification methods reconstruct objects after the corrupted sinogram is removed and interpolated from adjacent data.
> - linear interpolation (LI)
> - Although LI removes most background artifacts, this usually causes new artifacts due to inaccurate values interpolated in the metallic parts in the sinogram

- normalized metal artifact reduction (NMAR)
> - improve image quality
> - limitation for general applications due to the difficulty of optimal parameter selection.

- Maximum-Likelihood for TRansmission (ML-TR), expectation maximization (EM), iterative maximum-likelihood polychromatic algorithm for CT (IMPACT)
> - take sinogram inconsistency into consideration by correctly modeling its physical origin.
> - extremely high computation complexity.


### B. Unsupervised MAR models
- artifact reduction (ADN)
> - disentangles the artifact and content components of an artifact-affected image by encoding them separately into a content space and an artifact space. / highly complicated due to the explicit disentanglement steps.

### C. Attention model
- Many generative adversarial network (GAN)-based on the deep convolutional networks had difficulty in modeling some image classes more than others when training on multi-class datasets
- This is because small receptive field from convolution operator may not be able to represent them
- attention mechanisms have become an integral part of models that must capture global dependencies, since attention is designed to capture global patterns.
- the self attention Generative Adversarial Network (SAGAN)
> - uses self attention in the context of GAN
> - find global and long-range of dependencies within internal representations of images
- we used the CBAM module

### D. beta-VAE for feature space disentanglement
Variational Autoencoder (VAE) : methods of variational Bayesian and graphical model.
- to find the parameter *theta* to maximize the loglikelihood.
- VAE loss is a measure of the distances that equally considers both latent space and the ambient space between real and generated samples.

beta-VAE 
- a controllable parameter beta to impose the relative importance between the two distances:
- latent space is more interpretable and controllable

## 3. Theory
### A. Geometry of CycleGAN
- CycleGAN has shown great performance especially in unsupervised image artifact removal
- optimal transport (OT) provides a rigorous mathematical tool to understand the geometry of unsupervised learning by cycleGAN.
- LS-GAN approach : which is often used in combination of standard cycleGAN, is also closely related to imposing the finite Lipschitz condition.

### B. beta-CycleGAN for metal artifact disentanglement
we assume that Y is the domain for metal-artifact images, whereas X is the artifact-free images.

### C. Geometry of Attention
spatial and channel attentions
- Y = AZT
- T : implemented as a diagonal matrix so that each diagonal element represent the weight for each channel
- A : calculated as a full matrix so that global information of the features are used to compute the attended feature map.

convolutional block attention module (CBAM)
1. Channel attention module 
> - focuses on ‘what’ are important channels given an input image
> - the average pooling for aggregating spatial information
> - the max pooling for gathering another important clue about distinctive object features.
> - multi-layer-perceptron (MLP) : to find each channel weighting parameters.

2. Spatial attention module
> - focuses on ‘where’ is an informative part
> - average pooling and the max pooling for memory efficiency
> - used the 7x7 convolution operator in order to reflect the spatial domain information. (can reflect as wide range of spatial information)

## 4. Method
### A. DataSet
1) Real Metal Artifact Data
- 1,200 training slices : 800 slices were with metal artifacts and the remaining 400 slices were without metal artifacts
2) Synthetic Metal Artifact Data
- For quantitative evaluation of the algorithms, we added synthesized metal artifact to clean data.
- Convolutional neural network based metal artifact reduction (CNNMAR) to synthesize metal artifacts 
- For network training, we used 5,860 images to make synthetic metal artifact data, 4,115 images as clean data
- input image is 256x256

### B. Proposed Network Architecture
- green : 3x3 convolutions followed by a rectified linear unit (ReLU) and batch normalization.
- purple : 2x2 average pooling operator
- blue : 3x3 deconvolution
- red : simple 1x1 convolution operator
- black : skip and concatenation operator adding CBAM

- The discriminators D' and D  are constructed based on the structure of PatchGAN

### C. Training Details
1) Real Metal Artifact Data:
2) Synthetic Metal Artifact Data:

## 5. EXPERIMENTAL RESULTS
### A. Real Experiments
- the proposed method outperform the others.
- successfully removed the metal artifacts with little loss of dental information
- without metal artifacts. -> shall be no difference between input and output.
- images without metal artifacts are successfully recovered by our method.
- improved the quality of images removing beam-hardening artifacts

### B. Synthetic Metal Artifact Experiments
- our method outperform the others in terms of PSNR and SSIM for all images
    > 최대 신호 대 잡음비(Peak Signal-to-noise ratio, PSNR)는 신호가 가질 수 있는 최대 전력에 대한 잡음의 전력을 나타낸 것이다. 주로 영상 또는 동영상 손실 압축에서 화질 손실 정보를 평가할때 사용된다.
    > SSIM : 압축 및 변환에 의해 발생하는 왜곡에 대하여 원본 영상에 대한 유사도를 측정하는 방법
 - no metal artifact : it can be confirmed that there is little difference between output and input when we use the proposed method

### C. Ablation Study
1) Result of CycleGAN without CBAM : After the training without CBAM, we found that the artifacts in the background had become fainter compared to those of the input. we found that CBAM is an essential part of our MAR.
2) Dependency on the disentanglement parameter beta : By increasing beta to focus more on the artifact-free images

## 6. CONCLUSION 
we proposed a novel beta-cycleGAN with an attention module for the metal artifact removal in CT data.
we used CBAM to focus on important features in both spatial and channel domain.
we introduced a disentanglement parameter beta

---
---
---
# Unsupervised CT Metal Artifact Learning using Attention-guided beta-CycleGAN
- https://arxiv.org/abs/2007.03480
- [Submitted on 7 Jul 2020]
- IEEE Trans. on Medical Imaging

---
## Summary
- we propose an attention-guided unsupervised MAR method using the cycleconsistent adversarial network with CBAM.
- CT 촬영 이미지에 있는 metal artifact를 없애기 위한 모델을 만들었다. (beta-CycleGAN)
- cycle-consistent adversarial network (CycleGAN) 사용 : unsupervised image-to-image translation task

- convolutional block attention module (CBAM) 사용
- ![image](https://user-images.githubusercontent.com/70581043/127814122-95aa798d-6043-4cdd-9ebf-c86cf4bafb97.png)
> 1.  Channel attention module
> -  focuses on ‘what’ are important channels given an input image
> 2. Spatial attention module
> - focuses on ‘where’ is an informative part

- beta-Variational Autoencoder (VAE) 사용 :  parameter beta를 조절하면서 실제 이미지와 합성된 이미지 사이의 거리를 구함


---

## Model
![image](https://user-images.githubusercontent.com/70581043/127813630-36a0787b-2a46-48c3-b4c3-49632c4ccc64.png)

Synthetic Metal Artifact Data
- green : 3x3 convolutions followed by a rectified linear unit (ReLU) and batch normalization.
- purple : 2x2 average pooling operator
- blue : 3x3 deconvolution
- red : simple 1x1 convolution operator
- black : skip and concatenation operator adding CBAM

## Result
![image](https://user-images.githubusercontent.com/70581043/127813749-d49b49bd-1dab-486f-9f7a-768912e1fde6.png)
- (a) input  (b) proposed model (c) ~ (f) 다른 모델
- (c) ~ (f) 보다 (b)일 때 metal artifacts가 확실하게 없어졌다.
- 만약 metal artifacts 이 없는 이미지를 인풋한다면, 없애야 할 부분이 없기 때문에 인풋 이미지와 차이가 없어야 한다. > proposed model 의 결과 : metal artifacts이 없는 이미지를 인풋했을 때 아웃풋과 큰 차이가 없었음 & 화질 개선됨

---
## etc
![image](https://user-images.githubusercontent.com/70581043/127814156-8204d086-50e1-4a89-8e58-85b8bf12e899.png)
- CycleGAN 작동 원리를 사람 내부에 있는 optimal transport (OT) 의 작동 원리에 비유한 것이 흥미로웠다. (위 이미지)

- beta-CycleGAN 이 상용화 된다면 흉부 x ray 찍을 때 속옷 안 벗고 찍을 수 있는 건가 !!