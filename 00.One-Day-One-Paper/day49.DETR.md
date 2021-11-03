# End-to-End Object Detection with Transformers
- https://arxiv.org/abs/2005.12872
- ECCV 2020
---
**DETR(DEtection TRansformer)** : Transformer를 사용해서 object detection을 수행하는 모델을 제안했다. 기존 object detection model들 보다 훨씬 간단한 구조를 가지고 있다.

## DERT architecture
![image](https://user-images.githubusercontent.com/70581043/140083115-6a68ef74-b324-4657-a2c9-675d2efb1c61.png)
크게 3가지 구조로 되어 있음 
1. CNN backbone : 특성 추출, 일반적인 CNN 구조들을 사용할 수 있다.
2. encoder-=decoder transformer 
   - encoder : 1x1 Conv layer를 사용해서 dimension을 줄인다.  인코더에 sequence input이 들어가기를 원하기 때문에 spatial dimensions of z0을 one dimension으로 줄임 , 각각의 encoder layer는 self-attention module와 FNN으로 구성되어 있다.
   - decoder : 일반적인 transformer 구조를 사용함, 각각의 decoder layer들이 parallel 함, box와 class로 디코딩되어 N개를 예측함 
3. simple feed forward network (FFN) 
   - 3 layer perceptron with ReLU activation function
   - predicted the class label using a softmax function

## Loss
![image](https://user-images.githubusercontent.com/70581043/140084228-a8042139-e5ca-4dfb-bb68-7450982a529d.png)
* Pair wise matching cost - predicted objects와 ground truth 간의 score 차이를 계산 
![image](https://user-images.githubusercontent.com/70581043/140084965-313dfab4-375c-41f8-82d2-54862531bde5.png)
* class 에 대한 예측값과 predicted box에 대한 예측값으로 이뤄짐
![image](https://user-images.githubusercontent.com/70581043/140085246-0f0abe0a-a4bd-4b7a-b1bb-0f303efb73cc.png)
* Hungarian loss를 이용해서 loss를 구한다.
![image](https://user-images.githubusercontent.com/70581043/140085400-98712ffa-0b95-4542-a149-e5375ddfe758.png)
* bounding box loss 는 generalized IoU loss를 이용해서 구한다.