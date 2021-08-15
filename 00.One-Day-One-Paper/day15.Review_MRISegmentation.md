# Deep Learning for Brain MRI Segmentation: State of the Art and Future Directions
- https://link.springer.com/article/10.1007/s10278-017-9983-4
- Published: 02 June 2017
---
## Abstract
뇌 MRI에 대한 딥러닝 기반 segmentation 방식들을 리뷰한 논문

## Background
Magnetic resonance imaging (MRI)
- structural brain analysis
- it provides images with high contrast for soft tissues and high spatial resolution
- Alzheimer’s disease, epilepsy, schizophrenia, multiple sclerosis (MS), cancer, and infectious and degenerative diseases

Quantitative analysis of brain MR images
- 3D and 4D imaging 나오고 있으며 데이터의 크기와 복잡도가 커지고 있다. 이에 따라 큰 데이터 셋에서 필요한 정보만 추출하는 개발 도구가 필요하다.
- segmentation of the brain structures and detection of the abnormalities 은 기계학습에서 아직까지도 풀리지 않은 문제이다. brain의 형태도 다 다르고, 질병에 따라 다르고, 기계 세팅에 따라 다르기 때문에
- 딥러닝 기술을 활용한 MR segmentation에 대해서 리뷰할 예정이다.

## Deep Learning
딥러닝에 대한 기본적인 원리들 설명함

## Review
논문들을 두 가지로 구분함
1. works on normal structures
2. works on brain lesions
각각 세부 항목으로 patch-wise, semantic-wise, or cascaded architectures로도 구분함

## Training, Validation and Evaluation
데이터 셋을 train / validation / test 셋으로 나눈다. 데이터가 적다면 cross validation methods를 사용하기도 한다. training data는 정답지가 있는 supervised learning이기 때문에 이를 손으로 직접 segmentation하는데 많은 노력이 들기도 하다. brain 과 관련된 많은 데이터들이 등장했다.
ex ) Brain Tumor Segmentation (BRATS), Ischemic Stroke Lesion Segmentation (ISLES), Mild Traumatic Brain Injury Outcome Prediction (mTOP), Multiple Sclerosis Segmentation (MSSEG), Neonatal  Brain Segmentation (NeoBrainS12), and MR Brain Image Segmentation (MRBrainS)

## Image Preprocessing
- Registration : 공통된 해부학적 공간, MR 이미지를 표준화된 공간으로 standardizing 한다.
- Skull Stripping : skull 부위를 지운다.
- Bias Field Correction : 이미지 대비 변화를 보정한다.
- Intensity Normalization : 이미지의 intensity를 정규화한다. 0 ~ 4095 사이로
- Noise Reduction : MR 이미지에서 관찰된 noise를 감소시킨다.

## Current CNN Architecture Styles
- Patch-Wise CNN Architecture : N x N patch로 이미지의 특징을 추출한다.
- Semantic-Wise CNN Architecture : 특징을 추출하는 encoder & upsample을 하는 decoder & encoder와 classify 부분을 합친 부분
- Cascaded CNN Architecture : 두 CNN을 합친 모델, 첫 번째 CNN에서 예측을 한 후, 두 번째 CNN에서 이를 더 정교하게 tune한다.

## Segmentation of Normal Brain Structure
- white matter (WM), gray matter (GM), and cerebrospinal fluid (CSF) segmentation (SVM, random forest (RF), FCN, patch-wise CNN approach, multi-scale patch-wise CNN)

## Segmentation of Brain Lesions
![image](https://user-images.githubusercontent.com/70581043/129472768-1c7d9abe-4782-4a53-a068-be8a55ca05da.png)

- brain cancer, MS, and stroke
- Reliable extraction of these biomarkers depends on prior accurate segmentation.
- unsupervised modeling methods 자동으로 새로운 이미지들을 적응시킬 수 있음
- atlas-based methods는 unsupervised와 supervised를 합친 것
- tumor vs. normal brain labels 데이터 불균형 문제를 해결하기 위해서 : 1) 동등한 비율로 훈련을 먼저 시킨 후, 2) 아웃풋 레이어에서만 불균형 데이터로 훈련시킨다.

## Discussion
- medical imaging datasets이 부족하다는 한계를 극복해야 한다. (data augmentation)
- 성능을 높이기 위한 다양한 시도들 (data preprocessing, data postprocessing, network weight initialization,Random weight initialization, dropout, L1/L2 regularization)

