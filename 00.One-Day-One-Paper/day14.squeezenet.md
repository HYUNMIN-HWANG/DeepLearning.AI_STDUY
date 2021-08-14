# SQUEEZENET: ALEXNET-LEVEL ACCURACY WITH 50X FEWER PARAMETERS AND <0.5MB MODEL SIZE
- https://arxiv.org/abs/1602.07360
- [Submitted on 24 Feb 2016 (v1), last revised 4 Nov 2016 (this version, v4)]
- ICLR

---
기존 AlexNet보다 파라미터 수는 0.5MB 적지만 어느정도의 정확도를 보여주는 small CNN 모델인 _SqueezeNet_을 제안했다.

### ARCHITECTURAL DESIGN STRATEGIES
1. 3x3 filter 대신 1x1 filter 사용함 : 1x1이 3x3보다 9배 적은 파라미터 수를 갖고 있다.
2.  input channel 에 3x3 filter를 사용함 : 전체적으로 적은 수의 파라미터를 유지할 수 있음
3. downsample을 늦게 함으로써 large activation maps를 구성함 :  acc를 높일 수 있음

### THE FIRE MODULE
![image](https://user-images.githubusercontent.com/70581043/129431143-d14acdf6-f46f-4e77-ba52-a8a55dd598af.png)
- 1x1 filter로 구성된 _squeeze convolution layer_
- 1x1 filter 4개, 3x3 filter 4개로 구성된 _expand layer_
-  무조건 s1x1 < (e1x1 + e3x3) 

### THE SQUEEZENET ARCHITECTURE
![image](https://user-images.githubusercontent.com/70581043/129431222-1232749f-2a7a-4433-a2b8-290983bcfbd9.png)

### EVALUATION OF SQUEEZENET
![image](https://user-images.githubusercontent.com/70581043/129431596-797bd0e7-2219-4a95-bce6-de5f4a142f3a.png)
- SqueezeNet을 사용했을 때 AlexNet에 비해 모델 사이즈를 50배 줄일 수 있었다. AlexNet의 accuracy에 충분히 충족시킴 , 
- Deep Compression 기법을 적용했을 때 정확도는 일정하게 유지하면서 모델 사이즈가 더 줄어들었다. 

### CNN MICROARCHITECTURE
![image](https://user-images.githubusercontent.com/70581043/129431907-c2b75952-aa41-4091-9a70-2383ce3e8235.png)
- squeeze ratio (SR) : as the ratio between the number of filters in squeeze layers and the number of filters in expand layers. SR을 높일수록 acc가 올라갔다.
- 3x3 filter의 비율을 높일수록 모델 사이즈는 커졌지만, acc는 그다지 오르지 않았다.

### CNN MACROARCHITECTURE
![image](https://user-images.githubusercontent.com/70581043/129432160-c63fe5bf-188f-4ca3-86a7-d0a8fa2068fc.png)
- simple bypass architecture
> - bypass connections around Fire modules
> - can improve the final accuracy and/or ability to train the full model.
> -  complex bypass 보다 성능이 더 좋다.
- complex bypass architecture
> - bypass that includes a 1x1 convolution layer with the number of filters set equal to the number of output channels that are
needed.
> - help to alleviate the representational bottleneck introduced by squeeze layers.