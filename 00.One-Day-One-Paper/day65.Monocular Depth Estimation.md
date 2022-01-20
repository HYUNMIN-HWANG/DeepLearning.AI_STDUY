# High Quality Monocular Depth Estimation via Transfer Learning

하나의 RGB 사진을 인풋으로 넣고 high-resolution depth map을 추출한다.       

### Contributions : 
1. simple transfer learning-based network architecture
![image](https://user-images.githubusercontent.com/70581043/150280517-ee91b90f-892b-4bbf-bcd8-24596dda3aab.png)        
- Encoder : DenseNet-169, pretrained ImageNet, 더 복잡하게 만들어보았지만 복잡하다고 성능이 항상 좋은 것은 아니었음
- Decoder : up-sampling, skip-connection form decoder, BN 없음

2. loss function
![image](https://user-images.githubusercontent.com/70581043/150280735-922b76b5-cf38-4bea-a76b-1e78844ef560.png)
    - L_depth : point-wise L1 loss defined on the depth values
      ![image](https://user-images.githubusercontent.com/70581043/150280768-6db8b7e6-24b0-4a38-a8c1-d690b5713428.png)    
    - L_grad : L1 loss defined over the image gradient g of the depth image
      ![image](https://user-images.githubusercontent.com/70581043/150280872-37c6bcfe-dbd9-4afb-a199-aed56aa194d2.png)       
    - L_SSIM : Structural Similarity (SSIM)
      ![image](https://user-images.githubusercontent.com/70581043/150280950-3ea7957e-ba3c-4d3f-bd0e-32a7a3b54439.png)    


근본적인 문제가 있음 >> ground-truth depth values가 크면 loss가 큰 값을 갖게 된다. 이를 해결하기 위해서 ![image](https://user-images.githubusercontent.com/70581043/150281116-ecd89f0e-2c2a-4706-ada7-1dd373e30cc4.png) 식 처럼 depth의 가장 큰값으로 나눈 값을 target depth map으로 설정함


3. simple data augmentation
geometric 의미가 왜곡될 수 있으므로 모든 방면으로 augmentation을 할 수 없다.        
horizontal flipping (probability 0.5) 그리고 color channle augmentation (probability 0.25)만 실행


### Results
![image](https://user-images.githubusercontent.com/70581043/150281406-92dccf83-e7ad-4d0f-a8f6-4a0eae9b7c7b.png)
가장 오른쪽 column에 있는게 Our. GT와 유사한 결과를 보임

![image](https://user-images.githubusercontent.com/70581043/150281637-44277f13-cea4-4b21-b252-d6b5ab5657a3.png)
threshold (1.25 / 1.25^2 / 1.25^3)에 따른 average relative error(rel), root mean squared error(rms), average log10 error(log10) 결과를 보여주고 있다. 2가지를 빼고서는 our model 성능이 좋았다.           
더 적은 파라미터 수와 더 적은 훈련 수, 더 적은 training data 수로 SOTA와 유사한 성능을 보여줌                   
