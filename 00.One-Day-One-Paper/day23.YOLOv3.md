# YOLOv3: An Incremental Improvement
- https://arxiv.org/abs/1804.02767
- [Submitted on 8 Apr 2018]

---

### Bounding Box Prediction
![image](https://user-images.githubusercontent.com/70581043/131056680-e31809be-b1f2-4b3e-8238-d610042cda70.png)
- 이미지 가장 위 + 왼쪽 x값, y 값 : t<sub>x</sub>, t<sub>y</sub>
- bounding box의 폭, 높이 :  t<sub>w</sub>, t<sub>h</sub>
- 예측하는 값 : 
![image](https://user-images.githubusercontent.com/70581043/131057007-9f193e57-06dc-472b-ae03-3c072d83f173.png)
- objectness score : logistic regression을 사용함, 완벽히 똑같으면 1, 특정 threshold를 넘지 못하면 예측하지 않음

### Class Prediction
- multilabel classification 사용함
- 같은 이미지에 여러 개의 label을 붙일 수 있기 때문에 사용함 (eg. 여성 & 사람)

### Predictions Across Scales
- YOLOv3 predicts boxes at 3 different scales : bounding box, objectness, and class predictions.

### Feature Extractor
![image](https://user-images.githubusercontent.com/70581043/131057920-ed0e5aab-edbe-4c57-996f-0103b51b1442.png)
- Darknet-53을 제안함
- 다른 백본과 유사한(혹은 향상된) 성능을 보이면서 속도가 더 빠르다.
- This means the network structure better utilizes the GPU

### Result
![image](https://user-images.githubusercontent.com/70581043/131058132-c8d155c3-e675-429c-9f2d-d2696b49b443.png)
- AP (threshold 값에 따른 구분) 이 커지면 커질 수록 성능이 확 떨어진다.
- AP<sub>S</sub> 에서의 성능이 가장 좋다.
![image](https://user-images.githubusercontent.com/70581043/131058052-28e29f31-70a5-4bb1-af15-9450c22f6806.png)
- 해당 논문에서 제안한 YOLO3은 다른 모델에 비해 속도고 빠르면서 좋은 성능을 보여주고 있다.