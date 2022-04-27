# MobileViT: Light-weight, General-purpose, and Mobile-friendly Vision Transformer

vision transpose는 CNN에 견줄만한 성능을 보이지만 그에 비해 학습량, 시간이 오래 거린다는 단점이 있다. 이에 해당 논문에서는 ViT를 좀 더 가볍게 사용할 수 있는 모델을 제안했다.


### standard ViT model
![image](https://user-images.githubusercontent.com/70581043/165506301-bfae5713-50a3-4e24-8ace-f3acc875389f.png)

- input → flattened patches → projects it into a fixed d-dimensional space → learn inter-patch representations using a stack of L transformer blocks 

### MobileViT
![image](https://user-images.githubusercontent.com/70581043/165506362-c45ce713-48ef-4e97-ab63-f95743ec851d.png)
- MobileViT : light-weight and general-purpose vision transformer for mobile devices. 
    - implicitly incorporate convolution like properties (e.g., spatial bias) in the network
    - learn representations with simple training recipes (e.g., basic augmentation)
    - easily integrate MobileViT with downstream architectures (e.g.,DeepLabv3 for segmentation)
- input → standard convolutional layer → point-wise (or 1x1) convolutional layer → nxn convolutional layer encodes → UNFOLD → Transformer → FOLD → point-wise convolution → nxn convolution layer 
- local information : nxn convolutional layer encodes
- global information : Transformer
![image](https://user-images.githubusercontent.com/70581043/165508599-c365a84a-1ef7-4e3b-8f06-17b7919ec859.png)
- multi scale sampler : 고정된 batch사이즈를 사용하는 것이 아니라 resolution에 따라 다른 batch size를 지정한다.
   - spatial resolution이 (H_n, W_n) 인 경우, t-th iteration에 해당하는 batch size는 ![image](https://user-images.githubusercontent.com/70581043/165508562-9f2e0c39-90c6-4bdf-9cc0-0ecfaafe9209.png)
