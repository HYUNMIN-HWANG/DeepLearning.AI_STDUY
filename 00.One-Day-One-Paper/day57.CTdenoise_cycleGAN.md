# Cycle Consistent Adversarial Denoising Network for Multiphase Coronary CT Angiography
- https://arxiv.org/abs/1806.09748
- journal ; Medical Physics (2018)
---
CycleGAN을 이용해 CT images를 denoise시킴  
- CT denoise는 low-dose CT images와 routine-dose CT images들 간의 pairing이 가능해야 할 수 있었다(supervised learning). 하지만 현실적으로 동일한 사람으로부터 두 가지 CT를 찍기 어렵다.
- unsupervised learning 방법을 제안 : low-dose CT images 와 routine-dose CT images 가 완전하게 pair시키지 않아도 됨



## Framework (CycleGAN)
![image](https://user-images.githubusercontent.com/70581043/142760789-6ac8d1ed-319a-4981-a1b5-c048f087646d.png)        
- (A) low-dose CT domain
- (B) routine-dose CT domain
- generator G<sub>AB</sub> : (A) → (B)
- generator G<sub>BA</sub> : (B) → (A)
- discriminator D<sub>A</sub> : G<sub>BA</sub>(x<sub>B</sub>)와 los-dose CT image x<sub>A</sub> 간의 차이
- discriminator D<sub>B</sub> : G<sub>AB</sub>(x<sub>A</sub>)와 routine-dose CT image x<sub>B</sub> 간의 차이

 
## Loss
![image](https://user-images.githubusercontent.com/70581043/142760904-9acad27e-b2a7-4f6d-a347-79a4f0822c0d.png)         
### 1. Adversarial loss
- 기존 original gan loss를 사용하면 unstable하기 때문에 least squares GAN (LSGAN)을 사용함
- GAN loss는 generator가 denoise images를 점점 더 잘 만들게 해주는 동시에 discriminator의 성능도 높여준다.         
![image](https://user-images.githubusercontent.com/70581043/142761021-625ddfae-627c-4119-838c-03c712485c2a.png)         

### 2. Cyclic loss
![image](https://user-images.githubusercontent.com/70581043/142761134-7596cf5d-168f-4b33-ab89-9118550f8436.png)           
- L1 norm
- To enable one to one correspondence between the noisy and denoised image, the cycle which consists of two generators should be imposed to bring the input xA<sub>A</sub> to the original image.

### 3. Identity loss
![image](https://user-images.githubusercontent.com/70581043/142761181-1cdb7a2b-5cf6-40c3-800b-896708ddd944.png)            
![image](https://user-images.githubusercontent.com/70581043/142761223-a98b50ee-6ca0-4da2-849f-fe13ecaed238.png)        
원래 자신의 도메인과 얼마나 유사한지 나타낸다.


## Network
- two generators : G<sub>AB</sub>, G<sub>BA</sub>
- deiscriminator : D<sub>A</sub>, D<sub>B</sub> PatchGAN을 사용함

## Results
![image](https://user-images.githubusercontent.com/70581043/142761303-7a020277-c3db-4dc1-8849-c9fbfa65886e.png)            
