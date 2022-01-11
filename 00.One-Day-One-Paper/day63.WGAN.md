# Wasserstein GAN (WGAN)

## Earth-Mover (EM) distance/ Wasserstein Metric
![image](https://user-images.githubusercontent.com/70581043/148930114-baa3adfe-56c2-4715-ad02-dd8de9c7fa5a.png)     
![image](https://user-images.githubusercontent.com/70581043/148927735-3d6df4d5-013d-42cd-99cb-b6d036edc0e1.png)    
real data distribution (p) 와 generated model distribution (q) 사이의 거리를 좁히기 위한 "Wassertein distance" 거리를 제안함     
(Transportation plan ; p에 있는 모래성을 q로 어떻게 하면 저렴한 가격으로 옮길 수 있을까)

기존의 GAN 모델이 gradient를 계산할 때는  gradient vanishing problem이 있었다.(KL divergence의 한계)    
![image](https://user-images.githubusercontent.com/70581043/148927869-40dc15be-dd04-4443-adcb-83ea611d94f7.png)     

이 문제를 해결하기 위해서 아래와 같은 새로운 gradient를 제안함        
![image](https://user-images.githubusercontent.com/70581043/148927949-65634986-2713-4183-a39c-b67ee5a3f1d5.png)         
제안한 함수를 더 안정화시키기 위해서 noise를 추가함    
![image](https://user-images.githubusercontent.com/70581043/148928089-9008f37c-602d-4154-9331-9f1f94301a48.png)      

기존 GAN 모델은 vanishing gradient 문제를 보였지만, WGAN critic을 사용했을 때는 어디에서나 linear gradient 결과를 보였다.     
![image](https://user-images.githubusercontent.com/70581043/148928127-699bd434-e175-48cc-9518-60f9090cd530.png)

---

## Wasserstein GAN
Wasserstein distance를 더 간단하게 계산하기 위해서 Kantorovich-Rubinstein Duality Theorem를 이용해 아래와 같이 다시 쓸 수 있다.    
![image](https://user-images.githubusercontent.com/70581043/148928336-fe1ac49a-059a-41c6-91fa-eab5c49cba3f.png)     

![image](https://user-images.githubusercontent.com/70581043/148928508-17fdfb6a-0e0d-4158-aa39-92a0add93b1b.png)

기존의 GAN 모델과의 차이는 
- Discriminator라고 안 부르고 Critic이라고 부른다.
- Discriminator 끝에 sigmoid를 안 붙인다.
- 함수 f에 1-Lipschitz function를 사용한다. (함수 f의 maximum weight value를 제한하기 위해서 clip 기법을 사용함)



---
[참고사이트]
- https://jonathan-hui.medium.com/gan-wasserstein-gan-wgan-gp-6a1a2aa1b490
- https://kionkim.github.io/2018/06/01/WGAN_1/
- https://haawron.tistory.com/21