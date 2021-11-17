# Super SloMo: High Quality Estimation of Multiple Intermediate Frames for Video Interpolation
- http://jianghz.me/projects/superslomo/
- CVPR 2018
---
generate high-quality slow-motion video from existing video 필요한 것     
- transforming standard video -> higher frame rates
- generate smooth view transitions
- self-supervised learning
- interpret the motion between two input images
- understand occlusions


variable-length multi-frame interpolation method
- interpolate a frame at any arbitrary time step between two frames.
- wrap the input two images to the specific time step -> fuse the two warped images to generate the intermediate image -> modeled in a single end-to-end trainable network

![image](https://user-images.githubusercontent.com/70581043/142138714-eda3100b-97e4-4288-afe6-8710dc6c7bae.png)

### Intermediate Frame Synthesis
- estimate the bi-directional optical flow between the two input images
- 두 이미지 I<sub>0</sub>과 I<sub>1</sub> 사이의 I<sub>t</sub> 이미지를 예측하기 위해서
- not only the motion pattens but also the appearance of the two input images
- F<sub>t→0</sub> : I<sub>t</sub>에서 I<sub>0</sub>   
- F<sub>t→1</sub> :  I<sub>t</sub>에서 I<sub>1</sub>   
![image](https://user-images.githubusercontent.com/70581043/142135337-924b1aa6-e04e-428b-8a59-b8ae30736070.png)

### occulusion problem 
- T=t 타임에 p 픽셀이 있었다면 그 인풋 이미지 중 적어도 하나에서 p 값이 있을 것이다.
- visibility maps : V<sub>t←0</sub>, V<sub>t←1</sub>
- whether the pixel p remains visible when moving from T=0 to T=t
![image](https://user-images.githubusercontent.com/70581043/142136144-b14a79ae-4d38-4747-b764-2a405afb1db0.png)

### Arbitrary-time Flow Interpolation
![image](https://user-images.githubusercontent.com/70581043/142136664-1ceac8ff-eafa-4d9e-9877-38a366c7e7b6.png)
- synthesize the intermediate optical flow F<sub>t→0</sub> and F<sub>t→1</sub> using the optical flow between the two input images F<sub>0→1</sub> and F<sub>1→0</sub>
- orange dot p : T = t인데 이걸 T = 1 쪽으로 합성시키고 싶을 때,
![image](https://user-images.githubusercontent.com/70581043/142136800-bbf8dc27-9cc5-4181-afc7-b67c830c1a22.png)
- bi-directional input optical flow 합성시키고자 할 때는
![image](https://user-images.githubusercontent.com/70581043/142136945-8e841e18-73ee-48de-8781-282be58a2f78.png)
- works well in smooth regions but poorly around motion boundaries

### flow interpolation
- To reduce artifacts around motion boundaries
- input : g(I<sub>0</sub>, F^<sub>t→0</sub>), g(I<sub>1</sub>, F^<sub>t→1</sub>)
- output : refined intermediate optical flow fields F<sub>t→1</sub> and F<sub>t→0</sub>

### visibility maps
- to handle occlusions
![image](https://user-images.githubusercontent.com/70581043/142137620-017b3105-d902-4989-9a32-9743b68417b3.png)
- ![image](https://user-images.githubusercontent.com/70581043/142137749-9b35677d-2511-4985-8bfc-451c86a6d4d7.png) : I<sub>0</sub>의 픽셀 p가 T=t에서는 가려진다는 뜻
- soft visibility maps :  I<sub>0</sub>과 I<sub>1</sub> 모두 픽셀 p가 보일 때 사용한다.

## Network architecture
![image](https://user-images.githubusercontent.com/70581043/142137954-8361b418-0eb9-45e6-913b-4dc40dc83f1f.png)
bi-directional optical flow between the two input images.
     -  input : I<sub>0</sub>과 I<sub>1</sub> -> flow computation CNN -> forward optical flow F<sub>0→1</sub> and backward optical flow F<sub>1→0</sub> between them
     - U-NET architecture
     - large filter 7*7

## Training
Loss : ![image](https://user-images.githubusercontent.com/70581043/142138524-0d2a2010-df48-4c83-a8aa-ac332bb9854a.png)
- Reconstruction loss : ![image](https://user-images.githubusercontent.com/70581043/142138551-248b3d14-d9c3-4739-acd4-8de3e0c7a5fb.png)
- Perceptual loss : ![image](https://user-images.githubusercontent.com/70581043/142138582-3503ab74-ae8c-4aa6-ab76-3d27e2ac8d93.png)
- Warping loss : ![image](https://user-images.githubusercontent.com/70581043/142138611-9b2db694-cdb5-4838-bfd2-51cf9480c20c.png)
- Smoothness loss : ![image](https://user-images.githubusercontent.com/70581043/142138633-620ed1f6-73c1-4258-abb5-59729e036218.png)

