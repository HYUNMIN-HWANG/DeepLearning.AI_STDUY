# Learning Transferable Visual Models From Natural Language Supervision
[Reference]
- https://openai.com/blog/clip/
- https://github.com/OpenAI/CLIP
- https://inforience.net/2021/02/09/clip_visual-model_pre_training/
- https://daeun-computer-uneasy.tistory.com/38
---
## CLIP (Contrastive Language-Image Pre-training)
이미지와 그와 관련된 text를 pair 시키고, 이를 zero-shot learning 으로 훈련시켜 이미지와 관련된 text를 예측하도록 한다.
![image](https://user-images.githubusercontent.com/70581043/151118592-bc22eb3b-9373-4761-92dd-c5241d1dbcaa.png)

1. Contrastive pre-training
- 2개의 인코더 : text-encoder, image-encoder 
    - image-encoder : ResNet / Vision Transforemer
    - text-encoder : Transformer 
- 각 인코더를 통과시킨 벡터들 간의 관계를 학습시킨다.
- zero-shot learning : 
     - 한 번도 본적이 없는 object를 classification 할 수 있다. 
     - 인터넷에 있는 이미지-텍스트 연결된 데이터들을 갖고 훈련시킴, 데이터가 매우 다양하고 방대함(400 million) > zero-shot과 유사한 환경
     

2. Create dataset classifier from label text
- 이미지를 학습된 image-encoder를 통과시켜 이미지 특징을 추출
- class label 중에서 가장 관계가 높은 text를 선택한다.
- 유사한 관계는 cosine similarity로 계산한다.
- prmt template : "A phto of a {label}" 이런식으로 이미지에 대한 promt를 제시하면 이미지에 대한 내용을 더 상세히 표현해낼 수 있다.

### Performance
![image](https://user-images.githubusercontent.com/70581043/151119779-6dedb74c-45c0-4729-af63-ad15ffe3ff40.png)
CLIP is 4x to 10x more efficient at zero-shot ImageNet classification

![image](https://user-images.githubusercontent.com/70581043/151119990-6785067f-2781-4989-9c73-d9003cdfd3fa.png)
CLIP models are significantly more flexible and general than existing ImageNet models. 27개 데이터 셋에 대한 성능을 봤을 때 CLIP-ViT가 다른 모델에 비해서 좋은 성능을 보여주고 있다.
