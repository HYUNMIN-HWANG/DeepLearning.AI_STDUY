# An Image is Worth 16X16 Words: Transformers for Image Recognition at Scale
- https://arxiv.org/abs/2010.11929
- ICLR 2021
---
## ViT (Vision Transformer)
그동안 NLP 분야에서 많이 사용되었던 Transformer를 Computer Vision 영역에 적용했다. 해당 논문에서는 최대한 기존의 standard Transformer를 그대로 이미지에 적용하려는 시도를 했다. image를 patch단위로 자르고, 이를  Transformer에 patch를 선형으로 제공했다. 
![image](https://user-images.githubusercontent.com/70581043/142411182-de7991ce-6d2b-401e-bbfb-c76128a64ec5.png)
- 2D 이미지를 임베딩해야하기 때문에 : reshape the image  ![image](https://user-images.githubusercontent.com/70581043/142411329-d6292835-3822-475a-b464-046e28358828.png) → ![image](https://user-images.githubusercontent.com/70581043/142411377-e60e67fe-db88-4f78-a5ed-e6b981605d42.png)
- H, W : 이미지 차원
- (P, P) : 이미지 패치의 차원
- N = HW/P<sup>2</sup>
- D : constant latent vector size
- 패치들을 flattne시킨 후, D 차원에 맞게 매칭해준다.
- class token과 유사한 역할 : learnable embedding to the sequence of embedded patches (z<sup>0</sup><sub>0</sub>) = x<sub>class</sub>
- position embedding : patch embedding에 positional information을 추가한다.
- Transformer encoder : multi-headed self attention, MLP blocks, LAyernorm

### Experimetns
- ResNet, ViT, hybrid 모델을 비교
- pre-train on datasets한 결과와도 비교

![image](https://user-images.githubusercontent.com/70581043/142412895-a2fa6188-eaa2-4a90-bdfd-5307ac21593b.png)
- classification model을 비교했을 때 : ViT-L/16 model pre-trained on the public ImageNet-21K dataset performs well on most datasets too
