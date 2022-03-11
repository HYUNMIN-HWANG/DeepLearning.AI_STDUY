# CrossViT: Cross-Attention Multi-Scale Vision Transformer for Image Classification


![image](https://user-images.githubusercontent.com/70581043/156353260-2924ab91-ec9f-4859-9456-4122fe9700e8.png)

**Summary**
- how to learn multi-scale feature representations in transformer models for image classification
- a dual-branch transformer ( token 사이즈에 따라 S와 L 두 개로 구성됨)
- these tokens are then fused purely by attention multiple times to complement each other
- cross attention 을 사용해서 fusion ->  exchange information with other branches.
- 장점 : linear time for both computational and memory complexity


**Multi-Scale Vision Transformer**
- dual-branch ViT where each branch operates at a different scale (or patch size in the patch embedding)
- K multiscale transformer encoders : L-Branch & S-Branch
- Both branches are fused together L times and the CLS tokens of the two branches at the end are used for prediction
![image](https://user-images.githubusercontent.com/70581043/156355323-7287eb2a-d915-41b8-b67b-cd09f2208a9a.png)
- fusion 방식 :  위 4가지 방식을 실험해봤는데 결과적으로 (d) Cross attention  성능이 가장 좋았음. 
    -  fusion involves the CLS token of one branch and patch tokens of the other branch.
    - utilize the CLS token at each branch as an agent to exchange information among the patch tokens from the other branch and then back project it to its own branch.
    - linear 하게 cost 발생한다.

**Results**
![image](https://user-images.githubusercontent.com/70581043/156360067-c8f4e7c6-9350-4f8f-98b6-e0094846e01d.png)
- Comparisons with DeiT : our proposed cross-attention is effective in learning multi-scale transformer features for image recognition.

![image](https://user-images.githubusercontent.com/70581043/156360270-bc25228f-85e6-4b18-8dee-f121d75bebd5.png)
- Comparisons with SOTA Transformers :  outperforms the small models of all the other approaches with comparable FLOPs and parameters
- Our approach is consistently better than T2T-ViT and PVT in terms of accuracy and FLOPs

![image](https://user-images.githubusercontent.com/70581043/156360484-c051f9b7-d4a8-4286-be19-f5320f6feba2.png)
- Comparisons with CNN-based Models : best models are CrossViT-15† and CrossViT-18†
