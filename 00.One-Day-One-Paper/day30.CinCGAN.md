# Unsupervised Image Super-Resolution Using Cycle-in-Cycle Generative Adversarial Networks
- https://openaccess.thecvf.com/content_cvpr_2018_workshops/w13/html/Yuan_Unsupervised_Image_Super-Resolution_CVPR_2018_paper.html
- IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, 2018, pp. 701-710
---
## Summary
CycleGAN 두 개를 사용해서 저화질의 이미지를 고화질로 바꾸는 CinCGAN을 제안했다.

- Architecture
![image](https://user-images.githubusercontent.com/70581043/132944242-c8104bd6-8dad-45eb-ad42-c3e725f9f320.png)
크게 3가지 과정으로 구분되어 있다.           



**1. LR Image Restoration**
- Low Resolution(LR) 과 clean LR 을 매핑
- 인풋 이미지 x를 G1 에 넣어 y~ 생성 -> D1으로 실제 clean 이미지와 판별
- least square loss 사용함 
![image](https://user-images.githubusercontent.com/70581043/132944335-e714152c-f774-40da-9012-218984163e70.png)
- cycleGAN으로  x와 y를 한 번 더 확인하기 위해 G2 추가 : 
![image](https://user-images.githubusercontent.com/70581043/132944361-08386c18-b907-4250-a0ae-4d55d8853fc4.png)
- color감을 유지하기 위해서 identity loss를 추가함 : 
![image](https://user-images.githubusercontent.com/70581043/132944392-187c764e-b1a4-4a5f-8cdd-fc61e65cc304.png)
- total variation loss 추가 : 
![image](https://user-images.githubusercontent.com/70581043/132944412-d406a921-1069-4e86-aa4c-5a302d0eedb5.png)
- 최종 loss : 
![image](https://user-images.githubusercontent.com/70581043/132944440-ca4b5dc7-a5c2-4d4d-87b7-7edcc41378f2.png)



**2. Jointly Restoration and Super Resolution**
- LR -> HR network
- SR을 함으로써 우리가 원하는 이미지 크기만큼 키워야 한다.
- G1을 거친 다음 바로 SR 네트워크에 인풋
![image](https://user-images.githubusercontent.com/70581043/132944531-63d4e272-2417-4550-bb0e-aec1801ca9bb.png)
- D2가 G1과 SR 네트워크를 훈련시킨다.
- G3를 추가함으로써 CycleGAN 기능을 수행함 
![image](https://user-images.githubusercontent.com/70581043/132944534-8271fbac-792f-4af6-87f0-aea9d5b22a3c.png)
- total variation loss 추가 : 
![image](https://user-images.githubusercontent.com/70581043/132944542-6b7109fc-5bf4-4ec9-93c1-1cfd385dbeeb.png)
- identity loss : SR 이미지를 잘 생성할 수 있도록
![image](https://user-images.githubusercontent.com/70581043/132944566-5fed3afe-ba2d-4eb4-a91b-13f098f8cad6.png)
- 최종 loss : 
![image](https://user-images.githubusercontent.com/70581043/132944583-c7d17939-074e-4515-bdc8-e5f297c8abfa.png)

**3. Network Architecture**
![image](https://user-images.githubusercontent.com/70581043/132944591-9dbf7dbd-8029-4ede-bb7e-f542c1949601.png)
- 1과 2 모델을 연결
---
## Results
- 다른 모델들과 비교했을 때 가장 clean한 결과가 나왔다.
![image](https://user-images.githubusercontent.com/70581043/132944630-5c4a22b5-c891-4894-bada-c0c91a94110b.png)
- proposed model 에서 하나 두개씩 빼보면서 성능을 비교했고 CinCGAN 모델일 때 가장 좋은 결과가 나왔다. (Structure1이랑 3이 더 잘 나온 것 같은데,,,,)
![image](https://user-images.githubusercontent.com/70581043/132944647-2eeef744-7221-41a6-90aa-3dbfd9a25d72.png)
![image](https://user-images.githubusercontent.com/70581043/132944663-69984c9f-3dd2-4e67-b130-b33c6d686ec7.png)
