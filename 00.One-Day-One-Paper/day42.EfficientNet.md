# EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks
- https://arxiv.org/abs/1905.11946
- [Submitted on 28 May 2019 (v1), last revised 11 Sep 2020 (this version, v5)]
- International Conference on Machine Learning, 2019
---
![image](https://user-images.githubusercontent.com/70581043/136128402-8bcdbf44-a15a-48da-8faf-f8be90672173.png)
모델의 성능을 높이기 위해서 그동안 width, depth, resolution을 따로 바꿔가면서 성능을 비교했다.  EfficientNet에서는 이 세 가지를 동시에 scaling하는 compound scaling method를 제안했다.
- width : 주로 작은 사이즈 모델에서 scale한다. 너무 wide 하면 high level features들을 잡을 수가 없다.
- depth : 주로 깊은 모델이 좋은 성능을 보이기는 하지만, vanishing gradient problem이 있음, 이를 해결하기 위해 skip connection, batch normalization 기술을 넣었지만 그래도 very deep 모델에서는 성능이 안 좋아진다.
- resolution : input image를 고화질 사진을 넣으면 주로 성능이 좋게 나온다. 하지만 very high resolution이면 acc가 떨어지기도 함

### Compound Scaling
- need to coordinate and balance different scaling dimensions 서로 다른scale들을 조합하고 균형을 잡으면서 모델을 만들어 나가야 한다.
- **compound scaling method**
![image](https://user-images.githubusercontent.com/70581043/136129098-d72aebcc-93a8-41f3-a56f-5c90cf04df89.png)
- compound coefficient Φ :  to uniformly scales network width, depth, and resolution in a principled way, controls how many more resources are available
for model scaling,
- ![image](https://user-images.githubusercontent.com/70581043/136129260-f56865c4-a614-4625-b283-12a5181bf522.png)
 :constants that can be determined by a small grid search.
- 해당 논문에서는 ![image](https://user-images.githubusercontent.com/70581043/136129422-4a2250f8-44bc-4d8d-8f71-6b76f17aa9a4.png) 으로 맞췄다.

## Results
![image](https://user-images.githubusercontent.com/70581043/136129500-45751611-e0a8-4b33-94cd-2b942ddf62f5.png)
- 기존의 MobileNet과 ResNet을 compound scale했을 때 성능이 더 좋아졌다.
![image](https://user-images.githubusercontent.com/70581043/136129623-ee76ba3d-aa39-4536-9ef3-52255995810a.png)
- ImageNet 데이터 셋으로 훈련했을 때의 결과, 다른 모델들의 비해 acc도 높지만 FLOP 또한 적었다.
![image](https://user-images.githubusercontent.com/70581043/136129703-08552999-e28b-461a-ba13-c54b1107dbe9.png)
- 여러 데이터 셋으로 transger learning 한 모델들과 비교했을 때도 EfficientNet에서 성능이 더 좋게 나왔다.

