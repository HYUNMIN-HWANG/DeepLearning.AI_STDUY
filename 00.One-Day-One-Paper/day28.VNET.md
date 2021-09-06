# V-Net: Fully Convolutional Neural Networks for Volumetric Medical Image Segmentation

- https://arxiv.org/abs/1606.04797
- [Submitted on 15 Jun 2016]
---

## Summary
- 3D image segmentation based on a volumetric, fully convolutional, neural network
- Dice coeffcient
- augment the data applying random non-linear transformations and histogram matching

## Model
![image](https://user-images.githubusercontent.com/70581043/132231641-1fd4cd13-26af-45d4-b982-1cb5b0db89e9.png)
### Left
- extract features from the data
- compression path
- Each stage comprises one to three convolutional layers
> - (a) used in the convolutional layers and processed through the non-linearities
> - (b) added to the output of the last convolutional layer of that stage in order to enable learning a residual function
- 5 x 5 x 5 Voxel -> stride 2 -> resolution is reduced
- horizontal connections : left part -> right part
### Right
- decompresses the signal until its original size is reached
- expand the spatial support of the lower resolution feature maps in order to gather and assemble the necessary information to output a two channel volumetric segmentation.

### Last Output
- 1 x 1 x 1 kernel size
- output same size as the input volumes
- soft-max

## Dice loss

- 기존 방법의 한계점 : 배경에 비해 segmentation 해야 하는 부분이 굉장히 작았기 때문에 data bias 문제가 있었다. 이를 해결하기 위해서 foreground에 더 많은 가중치를 부여하는 방식을 사용했었다.
- Dice coefficient : 
![image](https://user-images.githubusercontent.com/70581043/132232978-adae0741-7928-4809-9f4d-7e9f2ce1a852.png)
- 0과 1사이 값 (1일수록 좋은 성능)
- P : predictied binary segmentation volume, G : Ground Truth binary volume
![image](https://user-images.githubusercontent.com/70581043/132233384-198351b7-13fb-4c76-b22e-0fff6be5b756.png)
- 미분가능함
- j 번째 voxel 예측하는 걸 계산할 수 있다.
- foreground 와 background의 가중치간의 balance를 유지하기 위해서 가중치를 재조정할 필요가 없다.

## Results
- Dice score 잘 나옴
![image](https://user-images.githubusercontent.com/70581043/132233824-61ad75fb-8a84-41cc-9964-8d0c0380e717.png)
- Qualitative result
![image](https://user-images.githubusercontent.com/70581043/132233663-8a03b5fd-a275-4bbe-b9d8-0194fc8ed4a9.png)
