# Unsupervised Monocular Depth Estimation with Left-Right Consistency
- CVPR, 2017

Ground truth depth map 없이 Mono depth estimation 할 수 있는 모델을 제시했다.       
목표 : Left image 만 인풋으로 넣고, right image를 생성해서 3d shape을 학습하는 것     

### Left-Right Consistency
![image](https://user-images.githubusercontent.com/70581043/150300450-9f1da625-f365-459d-96cb-432ae13ae8d6.png)
- consistency between the disparities produced relative to both the left and right images
- Naive한 방법 : left 이미지와 right 이미지 사이의 격차가 생성된다.
- No LR : left 이미지로 right 이미지를 생성하고, 이 이미지와 left 이미지 간의 격차를 계산한다.
- Ours : left 이미지로 right 이미지 간의 disparity map을 생성 (오른쪽도 마찬가지) 두 disparity map 간의 consistency를 이용해서 더 정확한 결과를 도출해낼 수 있다.

### Training Loss
![image](https://user-images.githubusercontent.com/70581043/150327753-6bbd4db8-1667-4228-94c4-3055ec656a46.png)
- C_ap : encourages the reconstructed image to appear similar to the corresponding training input
- C_ds : enforces smooth disparities
- C_lr : prefers the predicted left and right disparities to be consistent.

#### Appearance Matching Loss
![image](https://user-images.githubusercontent.com/70581043/150328502-3ee1861a-0b65-4552-8f84-d78fa743013c.png)
compares the input image and its reconstruction images

#### Disparity Smoothness Loss
![image](https://user-images.githubusercontent.com/70581043/150328550-4a62675e-0431-490f-bca4-322433f6b493.png)
locally smooth with an L1 penalty on the disparity gradients

#### Left-Right Disparity Consistency Loss
![image](https://user-images.githubusercontent.com/70581043/150328818-ba7ee165-ea7e-4a62-8265-4f07be503d3e.png)
train our network to predict both the left and right image disparities,

### Results
![image](https://user-images.githubusercontent.com/70581043/150329210-14891352-a9fa-44da-bd6f-5ebf05f271cc.png)
Ground Truth data로 훈련시킨 결과와 크게 다르지 않은 결과가 나왔다.