# Group Normalization
- [Submitted on 22 Mar 2018 (v1), last revised 11 Jun 2018 (this version, v3)]
- https://arxiv.org/abs/1803.08494
- Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
- https://github.com/facebookresearch/Detectron/tree/main/projects/GN
---
## Summary
batch-dimension에 영향을 받는 batch-normalization의 한계를 극복하는 방법으로 제안되었다.
> `batch-norm` : the features by the mean and variance computed within a (mini-)batch. & required for BN to work with a sufficiently large batch size
> 단점 : BN is also batch-dependent, and when the batch size decreases its accuracy still degrades
![image](https://user-images.githubusercontent.com/70581043/134194654-1f4125f2-2779-4b63-a54d-32bf53103cdc.png)
---
![image](https://user-images.githubusercontent.com/70581043/134194335-36c1e8f1-8484-4fec-a239-505715343609.png)
- 그동안 batch-size의 영향을 덜 받기 위해 제안된 것들 (하지만 visual recognition 작업에서 그다지 좋은 성능을 보이지 못했다.)
1. `Layer Normalization`  - operates along the channel dimension 
![image](https://user-images.githubusercontent.com/70581043/134195161-ed4b4325-2634-4c4a-8c46-49b5bac5875d.png)
2. `Instance Normalization` - performs BN-like computation but only for each sample 
![image](https://user-images.githubusercontent.com/70581043/134195183-924d9b61-1241-4882-882b-0e1ed9d9839d.png)
---
### Group Normalization
![image](https://user-images.githubusercontent.com/70581043/134195782-f1d39960-e7ee-4089-befe-be811f52ead3.png)
- G : number of groups
- indexes i and k are in the same group of channels, assuming each group of channels are stored in a sequential order along the C axis.
> G=1이면 Layer Normalization과 동일함
> G=C이면 instance Normalization과 동일함
### Results
- Image Classification in ImageNet
![image](https://user-images.githubusercontent.com/70581043/134196278-f1747d29-b3e1-4dba-a9c7-2edc40f0faa5.png)
train할 때, GN의 error가 가장 적었고  eval할 때는 BN보다 약간 error가 높았다.
- GN는 batch-size 변화에 따른 영향이 적었다.
![image](https://user-images.githubusercontent.com/70581043/134196468-ef420984-1c1c-4c0a-8a01-061206f261f8.png)
batch-size가 변할수록 BN은 변화가 심하다. 하지만 GN은 batch-size에 거의 상관이 없는 dependent
- 그렇다고 Normalization 층을 아예 빼버리면 성능이 확 떨어진다. Normalization하는 건 필요하다.
![image](https://user-images.githubusercontent.com/70581043/134196694-02abc89e-944a-4e47-938b-9f6a7d4efa26.png)


