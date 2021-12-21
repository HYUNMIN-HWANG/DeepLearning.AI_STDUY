# Least Squares Generative Adversarial Networks
- https://arxiv.org/abs/1611.04076
---
## LSGAN
- Regular GAN 의 discriminator에 sigmoid cross entropy loss function이 아니라 least squares loss function을 사용함.      
1. sigmoid cross entropy loss function의 단점 : vanishing problems during the learning process
     - sigmoid 특징 상 양쪽 끝으로 갈 수록 flat 하게 수렴하기 때문에 saturate 한다는 특징이 있다.        
![image](https://user-images.githubusercontent.com/70581043/146881827-6a5e1687-f881-47a1-81d3-87594b68b0ee.png)
(b) 그래프를 보면 fake이미지가 경계선에서 한참 떨어져 있음에도 불구하고 decision boundary는 아무 문제없다고 판단을 한다.       
따라서 GAN이 realistic tasks를 하는데 한계가 있는 것      
LSGAN은 이를 해결하기 위해서  fake이미지를 최대한  decision boundary 쪽으로 끌어당겨 real data처럼 보이게 하고자 하는 motivation에서 등장했다. 이를 위해 least squares loss function을 사용함,       
least squares loss function는 거리가 멀수록 penalty를 주는 방식    
2. LSGAN이 훨씬 더 stability한 learning process를 보여준다.

## LSGAN loss function
 기존 GAN 모형은 아래와 같음       
![image](https://user-images.githubusercontent.com/70581043/146882504-da056efe-813e-4458-aabd-76ae5f0fd518.png)

LSGAN은 이 수식 대신에 아래 수식을 사용함          
![image](https://user-images.githubusercontent.com/70581043/146882523-c901a62f-c0b5-4343-bced-61810c6f7de2.png)

## Results
![image](https://user-images.githubusercontent.com/70581043/146882689-31e079c8-e8e0-4406-8134-ba032ad6fb9e.png)      
DCGAN 생성 이미지보다 LSGAN 생성 이미지가 훨씬 realistic 하고 선명하다.         
