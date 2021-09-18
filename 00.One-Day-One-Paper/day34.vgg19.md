# Very Deep Convolutional Networks for Large-Scale Image Recognition
- https://arxiv.org/abs/1409.1556
- [Submitted on 4 Sep 2014 (v1), last revised 10 Apr 2015 (this version, v6)]
---
과제할 겸 읽어보는 VGGNet paper !

## Summary 
- we evaluated very deep convolutional networks (up to 19 weight layers) for large scale image classification
- depth is beneficial for the classification accuracy
- our models generalise well to a wide range of tasks and datasets
- matching or outperforming more complex recognition pipelines built around less deep image representations

### Architecture
![image](https://user-images.githubusercontent.com/70581043/133879589-a44e5d64-e041-4ecf-927b-c431cd65ec3c.png)

3x3 convolution layer를 깊게 쌓은 네트워크를 발표했다. 
- input 224 x 224 RGB
- convolution layers : 3x3 filters
- 1x1 convolution filters : linear tranformatiom을 하기 위해서 
- stride 1
- padding 1 (3x3 conv layer일 때)
- max-pooling 2x2, with stride 2
- Fully Connected layer (input 4096) -> output 1000 classes
- activation : ReLu
- Local Response Normalization (LRN)
---
## Results
![image](https://user-images.githubusercontent.com/70581043/133879812-e9d1c92c-cc8e-4657-ae9c-17969f162a6c.png)
- A-LRN은 성능이 좋지 않았다. LRN은 그 다음 아키텍쳐에서도 사용안함
- C vs D : 1x1 conv보다 3x3 conv의 성능이 더 좋았다.
> - 3x3 conv를 사용한 이유? 
> 1. incorporate three non-linear rectification layers instead of a single one
> 2. decrease the number of parameters
- 깊이가 깊어질 수록 성능이 더 좋아짐