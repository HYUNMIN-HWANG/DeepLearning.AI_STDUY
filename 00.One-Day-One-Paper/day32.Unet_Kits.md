# An attempt at beating the 3D U-Net
- https://arxiv.org/abs/1908.02182
- [Submitted on 6 Aug 2019 (v1), last revised 4 Oct 2019 (this version, v2)]
- 2019 Kidney and Kidney Tumor Segmentation Challenge
---
KiTS Data로 kidney segmentation을 하는 중 data preprocessing  관련 참고하고자 함

## Summary
U-Net을 사용해서 kidney CT image를 semantic-segmentation했고, KiTS challenge 에서 1등한  paper

### Data
- 210 high quality annotated CT scans for training
- 90  for testing
- Preprocessing
> - 모든 이미지를 128 X 248 X 248 voxels 로 resample 시킴
> - 각각의 이미지를 [-79, 304]로 추출한 뒤, 101을 빼고, 76.9로 나눈다. (CNN에 더 잘 처리하기 위해서라고 함)

### Model
![image](https://user-images.githubusercontent.com/70581043/133264289-6d24ddab-6c4c-42bc-bf60-4eb845f48cac.png)

1. Plain 3D U-Net
- For both the encoder and decoder we use two conv-instnorm-ReLU blocks between poolings/upsamplings.
2. Residual 3D U-Net
- uses residual blocks in the encoder
- conv-instnorm-ReLU-conv-instnorm-ReLU
- The decoder uses only one conv-instnorm-ReLU per resolution
3. Pre-activation residual 3D U-Net
- uses pre-activation residual blocks:
- instnorm-ReLU-conv-instnorm-ReLU-conv

### Training
- stochastic gradient descent
- batch size of 2
- 250 batches and train for a total of 1000 epochs.
- The sum of cross-entropy and dice loss is used as training objective
- augmentation : batchgenerators framework (scaling, rotations, brightness, contrast, gamma and Gaussian noise augmentations.)

## Results
![image](https://user-images.githubusercontent.com/70581043/133263795-4f1bb283-173e-4694-b244-90997b68b380.png)
- 기존의 U-Net에서 변경을 시도했지만 그다지 좋은 성능을 보이지는 않았음
- ensemble을 했지만 그다지 좋지 않았음
- 기본적인 Residual 3D UNet을 사용한 게 대체로 좋음

![image](https://user-images.githubusercontent.com/70581043/133264123-8b1e4278-c946-4482-b1e6-33754d490f17.png)
- KiTS challenge 에서 다른 팀들보다 dice score 가 높게 나왔다.
