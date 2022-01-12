# Emerging Properties in Self-Supervised Vision Transformers
- 2021
---

## DINO
- the model was able to automatically learn class-specific features leading to accurate unsupervised object segmentation
- A Student ViT learns to predict global features in an image from local patches supervised by the cross entropy loss from a momentum Teacher ViT’s embeddings while doing centering and sharpening to prevent mode collapse
    - collapse 문제 :  입력값과 상관없이 출력값이 하나의 차원이 dominate 하거나, 모든 차원에 대하여 uniform 한 상황을 말함
    - Centering : The teacher’s raw activations have the their exponentially moving average subtracted from them, uniform한 결과를 장려
    - Sharpening : the same as applying a temperature to the softmax to artificially make the distribution more peaked ( exaggerate small differences so that there is one or some high values and some low values. ), 출력값이 uniform 분포가 아닌 sharp한 분포를 갖게 함


### self-distillation
- teacher and student network both having the same architecture, a Vision Transformer(ViT)
- momentum teacher :  it’s weights are an exponentially weighted average of the student’s
-  teacher network를 student network의 이동 평균으로 가중치를 업데이트 


### Data
- Small crops are called Local views :  96x96 image
- large crops are called Global views : 224x224 image
- All crops are passed through the student while only the global views are passed through the teacher
- “local-to-global” :  training the student to interpolate context from a small crop

### Loss
- softmax along with cross entropy loss
- 성능이 좋은 teacher의 output을 student가 흉내내도록 합니다. 둘 사이의 cross entropy를 사용하여 student 모델을 학습 , teacher는 stop gradient를 적용

### Results
- DINO has understood object semantics


---
- https://towardsdatascience.com/dino-emerging-properties-in-self-supervised-vision-transformers-summary-ab91df82cc3c
- https://deep-learning-study.tistory.com/827