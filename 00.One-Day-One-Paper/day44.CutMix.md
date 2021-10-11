# CutMix: Regularization Strategy to Train Strong Classifiers with Localizable Features
- https://arxiv.org/abs/1905.04899
- [Submitted on 13 May 2019 (v1), last revised 7 Aug 2019 (this version, v2)]
- Accepted at ICCV 2019 (oral talk). 14 pages, 5 figures

---
## Summary
data agumenation 방법으로 CutMix를 제안했다.        
![image](https://user-images.githubusercontent.com/70581043/136727020-caee9777-51c5-4373-b86c-d1b6fc8288f1.png)

기존 data augmentaion으로 제안했던 방법 중
- Mixup : 서로 다른 두 클래스를 겹친다. 
- Cutout : 이미지 특정 부분을 zero값으로 채운다.
- 제안한 CutMix : 이미지 특정 부분을 zero값으로 채우는 것이 아닌 다른 training iamge로 대체한다. (Instead of simply removing pixels, we replace the removed regions with a patch from another image)

## Algorithms
![image](https://user-images.githubusercontent.com/70581043/136727375-f6b052c2-14c0-46ec-b5c9-b4d7c563ada0.png)
- (x_a, y_a) + (x_b, y_b) => 새로운 합성 이미지 x~, y~을 만들어낸다.
- M : binary mask indicating where to drop out and fill in from two images, 1 is a binary mask filled with ones
- lamda : the combination ratio between two data points

![image](https://user-images.githubusercontent.com/70581043/136727615-b5ebb05b-5ddf-420f-a30b-1457ce58bec2.png)
- bounding box B = (rx, ry, rw, rh) -> 자르는 영역을 지정
- cropped area ratio ![image](https://user-images.githubusercontent.com/70581043/136727707-61be8e7d-33c3-40a2-ade3-c399e4af9804.png)

## Results
![image](https://user-images.githubusercontent.com/70581043/136727820-fba482b0-89cc-46a8-8d3b-12bccca3721c.png)
- Cutout : 버나드는 잘 인식하지만 푸들 사진은 잘 인식 못함
- Mixup : 버나드, 푸들을 각각 인식 못하고 전체 이미지로 인식함
- CutMix : 버나드와 푸들 각각을 인식한다.

### ImageNet Classification
![image](https://user-images.githubusercontent.com/70581043/136728028-ea5114df-c328-43dd-ad92-899b7ff43919.png)
ResNet50 모델에 CutMix를 사용했을 때 error가 가장 작다.              

그 외, CIFAT Classification, Weakly Supervised Object Localization, Transfer Learning 과제에서도 CutMix를 사용했을 때 좋은 성능을 보였다.
