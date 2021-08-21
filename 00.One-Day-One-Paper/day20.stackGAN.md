# StackGAN: Text to Photo-realistic Image Synthesis with Stacked Generative Adversarial Networks
- https://arxiv.org/abs/1612.03242
- [Submitted on 10 Dec 2016 (v1), last revised 5 Aug 2017 (this version, v2)]
- Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI); Machine Learning (stat.ML)

---

![image](https://user-images.githubusercontent.com/70581043/130321847-c12b0ad2-704d-4df7-9613-4b708bf5639f.png)
- Conditioning Augmentation
> we randomly sample the latent variables ^c from an independent Gaussian distribution ![image](https://user-images.githubusercontent.com/70581043/130322213-d059718c-deef-4616-b4cb-16150ad1fe9b.png)      
> more training pairs given a small number of image text pairs      
> encourages robustness to small perturbations along the conditioning manifold.      
> 장점 : 같은 text 로 부터 다양한 poses 와 appearances 이미지를 생성할 수 있다.

- Stage 1 
> 텍스트로부터 원시적인 shape와 기본적인 color를 스케치하여 백그라운드 레이아웃을 그려준다. (low resolution image)    
> ![image](https://user-images.githubusercontent.com/70581043/130322260-34590985-627f-4a79-bf49-7e4813cfe08a.png)

- Stage 2 
> stage1 에서 만들었던 이미지의 결함들을 고치고, 텍스트를 다시 읽은 후 디테일한 부분을 완성한다. (high resolution image)    
>  ![image](https://user-images.githubusercontent.com/70581043/130322267-8d1ade2b-69b4-42e8-8bae-79bd0b766878.png)
> 다른 GAN 모델과 다르게 the random noise z 가 사용되지 않았다.

## Result
- 평가지표 : Inception Score, human evaluation
![image](https://user-images.githubusercontent.com/70581043/130322380-63e95ce3-7e63-48d8-9133-996e692c015b.png)
> StackGAN에서 inception score와 human evaluation 점수가 가장 높게 나왔다.

![image](https://user-images.githubusercontent.com/70581043/130322404-e25f4c2c-c39b-459e-a056-f2c275b35380.png)
> CUB 데이터셋으로 test 해본 결과, StackGAN에서 디테일하고 고화질의 사진을 생성할 수 있었다.

![image](https://user-images.githubusercontent.com/70581043/130322427-582f3930-0fa5-4034-a034-4fe74e3ee1b9.png)
> Stage1에서는 모양, 색깔 정도 간략하게 생성됨, Stage2에서는 Stage1에 비해 더 디테일한 그림을 생성함