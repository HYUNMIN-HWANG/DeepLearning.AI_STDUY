# Analyzing and Improving the Image Quality of StyleGAN
- https://arxiv.org/abs/1912.04958
- Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2020.
---
StyleGAN의 문제점을 개선한 StyleGAN2

## Removing normalization artifacts
![image](https://user-images.githubusercontent.com/70581043/143873308-0457f594-a054-4a52-b02b-2d481c629b23.png)     
StyleGAN결과 중 blob-shape artifacts이 생겨난다. 특히, higher resolution으로 갈 수록 더 강해지는 특징을 볼 수 있다. 저자는 이 이유를 AdaIN 때문이라고 제안함, AdaIN이 destroying any information 하기 때문 -> AdaIN을 제거했더니 droplet artifacts가 사라졌다.

### Revised architecture
![image](https://user-images.githubusercontent.com/70581043/143874370-119a256c-f747-4d5c-bf8e-15cf7cd9125e.png)
- original StyleGAN에서는 bias와 weight를 style block 안에 적용시킴
- revised architecture : bias와 weight를 style block 밖에 적용시킴

### Instance normalization
![image](https://user-images.githubusercontent.com/70581043/143875510-0032097d-6f25-4840-bae0-d8837c237276.png)      
- sacrifice scale-specific controls->remove the normalization &retraining full controllability -> removing the artifacts, improving FID slightly
- effect of a modulation :  modulation 다음에 conv가 오는데, modulation은 입력 스타일에 근거한 conv의 각 피쳐 맵을 scaling 해준다. (conv weights를 scaling하는 대신에)     
- After modulation and Conv, std는 아래와 같다. 
![image](https://user-images.githubusercontent.com/70581043/143876009-99a4aab2-f116-4e04-be41-259f2a92e059.png)       
- **("demodulate")**
![image](https://user-images.githubusercontent.com/70581043/143877289-f00a030b-59d1-4923-aa0e-17c8b105bcf7.png)
- instance normalization 보다는 약하다, 실제 feature maps를 사용하는 게  아니라, signal에 대한 통계학적인 추정을 기반으로 하기 때문에

## Image quality and generator smoothness
- PPL(perceptual path length) : latent space에서 동요, 섭동(perturbations)과  생성 이미지 사이의 평균 LIPIS 거리를 측정함으로써, latent space로부터 생성된 이미지로 맵핑되는 과정이 얼마나 부드럽게 이루어졌는지 정량적으로 측정하기 위해 도입된 metric
- 낮을수록 이미지 품질이 높다
- 다른 regularization을 제안함
### 1 ) Lazy regularization
- regularization과 loss를 동시에 계산하는 것이 아니라
- regularization을 loss 보다 덜 자주 계산한다. -> 16 minibatch 동안 딱 한 번 계산함

### 2 ) Path length regularization
![image](https://user-images.githubusercontent.com/70581043/143878778-5a8c7d50-5db2-4507-b4a2-9133bec7d3c5.png)
- W에서의 고정된 크기의 움직임
- 이미지에 있어서 0이 아닌 고정된 크기의 변화를 유발

## Progressive growing
![image](https://user-images.githubusercontent.com/70581043/143879546-c167ed29-2ba5-4bdc-975c-1403cbcc626b.png)
- strong location preference for details (teeth나 eyes가 자연스럽게 연결되엇 변화해야 하는데 get stuck)

### Alternative network architectures
### Resolution usage
- generator가 초기에 저해상도 피쳐들에 집중하다가 서서히 미세한 세부사항들에 관심을 기울이게 하는 것
- 512 대신 1024 에서 더 sharp한 이미지 결과가 나왔다.

## Projection of images to latent space
- 최적화 과정에서 latent code에 ramped-down noise를 더함 (더 복잡한 latent space를 탐색 가능)
- generator에 입력되는 stochastic noise 값도 정규화(regularize)
- 신호 간의 간섭을 막도록, 최적화
- LPIPS 거리  : 거리가 멀수록 투영이 잘 된 것
 

---
- https://study-grow.tistory.com/entry/Deep-learning-%EB%85%BC%EB%AC%B8-%EC%9D%BD%EA%B8%B0-StyleGAN2