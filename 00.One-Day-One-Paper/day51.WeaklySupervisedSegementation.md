# Simple Does It: Weakly Supervised Instance and Semantic Segmentation
- https://arxiv.org/abs/1603.07485
- CVPR 2017
- 리뷰 참고자료 : https://wsshin.tistory.com/8
---
일반적으로 segmentation을 할 때, 사람이 직접 segmentation을 한 ground truth 이미지가 필요함. 하지만 이는 엄청난 cost를 발생시키기 때문에 좋은 훈련 방법이 아니다. 그래서 해당 논문에서 ground truth 없이 segmentation할 수 있는 방법을 제안함

- Contributions 
   - recursive training (이전의 segmentation 결과물을 다음 훈련할 때 인풋 값으로 넣는다.)
   - Grab-Cut과 같은 알고리즘을 사용해서 주어진 bounding box로 훈련 라벨 값을 생성함
   - bounding box만을 사용해도 기존의 fully supervised 훈련을 했을 때와 유사한 성능을 보임

## From boxes to semantic labels
### Box baselines
![image](https://user-images.githubusercontent.com/70581043/140755958-5a8bd603-c0db-4231-bfef-d6926fa52569.png)
Naive : annotated bounding box와 그에 해당하는 라벨 값이 주어진다. → Recursive training : 훈련 데이터 셋을 모델에 넣은 결과물을 그 다음 훈련할 때 ground truth 값으로 넣는다.  → box 가 점점 정교해진다. 
### Box-driven segments
GrabCut : bounding box로부터 object segment를 추정 → segmentation mask에서 pixel의 70% 를 차지하면 전면, class라고 정한다. 20% 아래면 배경, mark는 무시한다. 

## Semantic labelling results
weakly supervised instance segmentation as well as for semantic labelling.
![image](https://user-images.githubusercontent.com/70581043/140757388-4dd29943-482d-41f0-868f-747079945799.png)
Naive 모델이 가장 안 좋은 결과를 보임      
Box baseline은 거의 가장 좋은 결과물을 보임
