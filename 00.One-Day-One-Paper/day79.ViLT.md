vision과 text 데이터를 동일한 transformer로 처리할 수 있는 모델을 제안한다.
![image](https://user-images.githubusercontent.com/70581043/161429284-196e6c21-0154-4192-8c36-d707d74acd6f.png)

기존의 Vision-and-Language Pre-training(VLP) 모델들보다 훨씬 light하고 fast 한 모델을 제안했다. 
- CNN을 사용하지 않고 linear로만 feature extractor역할을 수행한다.
- embedding layer를 deep하지 않게 설계한다.
- Patch projection : RCNN에서 사용하는 region feature혹은 CNN을 사용하는 Grid feature와는 다른 path projection을 사용했다. 즉 lienar projection 방법으로  visual embedding 방법을 고안함
![image](https://user-images.githubusercontent.com/70581043/161429459-fa268bd7-348c-4477-a09d-75cbf60db21b.png)
- model : deviate from the literature that we initialize the interaction transformer weights from pre-trained ViT, use weights from ViT-B/32 pretrained on ImageNet
- Pre-training Objectives : Image Text Matching. Masked Language Modeling
- Whole word masking : 일부 단어만 mask하지 않고 전체 단어를 mask한다. -> 장점 : make full use of information from the other modality
- Image Augmentation : Image Augmentation의 효과가 VPN에서는 그다지 크지 않다. Rand augment 적용함/