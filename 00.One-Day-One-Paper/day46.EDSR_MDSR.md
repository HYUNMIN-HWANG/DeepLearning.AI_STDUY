# Enhanced Deep Residual Networks for Single Image Super-Resolution
- https://arxiv.org/abs/1707.02921
- [Submitted on 10 Jul 2017]
- To appear in CVPR 2017 workshop. Best paper award of the NTIRE2017 workshop, and the winners of the NTIRE2017 Challenge on Single Image Super-Resolution
---
## Summary
- 저화질 사진을 고화질 사진으로 바꾸는 super resolution model인 EDSR과 MDSR을 제안했다.
- 기존 super resolution 기법들
  > - Single image super-resolution (SISR) : High resolution(HR) image를 bidubic, 블러처리, 노이즈 추가 등으로  downsample 시켜 low resolution(LR)이미지를 만든다. LR로 HG을 재구성하는 모델을 만든다.
  > - peak signal-tonoise ratio (PSNR) : (단점) sensitive to minor architectural changes, 각기 다른 scale factir들을 독립적으로 생각한다. 
  > - VDSR : can handle super-resolution of several scales jointly in the single network 스케일이 다른 것들도 SR할 수 있다. 하지만, bicubic을 사용할 때 큰 자원이 필요하다.
  > - SRResNEt : ResNet을 사용해서 super resolution을 수행함, 하지만 ResNet이 이미지 분류나 감지에 적합한 모델이기 때문에 잘 맞지는 않았다.
- 기존 loss funxtion
  > - MSE
  > - L2 loss
  > - PSNR (performance measure)

- Our model
  > - SSResNet 구조를 사용하지만, 불필요한 부분들을 제거했다.
  > - 다른 scales들끼리 파라미터를 공유하는 새로운 multi-scale architecture을 제안함

## Proposed Methods
### EDSR
![image](https://user-images.githubusercontent.com/70581043/136951018-a91bd5bc-aa89-4ad4-9984-0d2ef49f9bb8.png)
- residual network를 사용. 단, Batch Normalization을 제거함,       
- residual block 다음에 ReLU층 제거함     
![image](https://user-images.githubusercontent.com/70581043/136950846-f153c20e-80a3-4061-8895-20ad442be03e.png)
- residual scaling 0.1
- depth 32, width 256
- upsampling factor : X2, X3, X4

### MDSR
![image](https://user-images.githubusercontent.com/70581043/136950873-7f51116d-adb7-45dc-a3a3-9b2da3a2afd7.png)
- depth 80, width 64
- 네트워크 초반에 Resblock (5x5 kernels) 으로 pre-processing

### Training
- L1 loss 사용
- Geometric self-ensemble : test할 때, 인풋 이미지를 augment한 걸 SR으로 만들고, SR한 이미지에 inverse tranform을 적용시켜 평균을 구한다. (모델 이름 뒤에 '+'를 추가함)

## Results
![image](https://user-images.githubusercontent.com/70581043/136952164-9ad9cb76-01ec-4e76-b4c9-ca1e2a49154f.png)
![image](https://user-images.githubusercontent.com/70581043/136952218-162abeba-1b8d-4e44-8921-789f8415a46a.png)
- EDSR, MDSR일 때 성능이 가장 좋게 나왔다.
