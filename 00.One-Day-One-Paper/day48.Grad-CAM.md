# Grad-CAM: Visual Explanations from Deep Networks via Gradient-based Localization
- https://arxiv.org/abs/1610.02391
- ICCV 2017
---
**Gradient-weighted Class Activation Mapping (Grad-CAM) :** CNN모델을 기반으로 visual explanations 할 수 있는 기술을 제안했다. 마지막 convolution layer에서 나온 gradient를 사용해서 이미지의 concept을 예측할 때 중요한 부위를 하이라이팅하는 localization map을 제공한다.

## Key contributions
1. (a) class discriminative (i.e. localize the category in the image) and (b) high-resolution (i.e. capture fine-grained detail). : 이미지 카테고리를 구분할 수 있을 뿐만 아니라 어디가 중요한 부위인지 표시할 수 있다.
2. any CNN-based network without requiring architectural changes or re-training. 다른 CNN 모델에 어떠한 변형없이 그대로 적용시킬 수 있다.
3. classification, captioning , and VQA  models. 다양한 task에 적용할 수 있다. 

## Grad-CAM Architecture
![이미지 2](https://user-images.githubusercontent.com/70581043/140064120-982277ce-7705-4c76-9022-7b2a70b313ef.png)

1) 빨간색 박스 - CNN 모델을 통과시켜 catgory별 스코어를 얻는다.
2) 초록색 박스 - Rectified Conv Feature Maps에서 backpropagation한 시그널으로 Grad-CAM을 만든다.
3) 주황색 박스 - Guided Backprop과 Grad-CAM을 poitwise 방식으로 합친다.

## Grad-CAM 특징
- last Convolution layer에 가장 공간에 대한 의미가 많이 담겨있다.
- 따라서 last Convolution layer에서 나온 gradient information을 사용함
- gradient의 backpropagation 값을 GAP한 결과 -> α : obtained the neuron importance weights 
![image](https://user-images.githubusercontent.com/70581043/140065331-983d1fa8-607a-40da-a4e6-17362a6bb38b.png)
- α와 feature map간의 linear combination을 해준 후, ReLU를 취한다. (ReLU를 하는 이유는 negative값은 필요없고, positive 값만 사용할 것이기 때문에)
![image](https://user-images.githubusercontent.com/70581043/140065644-b7fc41f4-9a55-4208-a254-43220017dfb7.png)

## Resluts
![image](https://user-images.githubusercontent.com/70581043/140065816-a69f454b-9c5d-48c2-a567-3f71802df70a.png)
- (a) (g) : original image
- (b) (h) : Guided BackProp - 단점, class를 구분하지 못한다.
- (c) (i) : Grad-CAM - category 구분 가능, 중요한 부분을 표시해준다.
- (d) (j) : 두번째 컬럼에 있는 것과 세번째 컬럼을 합친 겨로가
- (e) (k) : blue 색이 class의 결정적인 증거임
- (f) (l) : ResNet을 사용해서 나온 결과물


