# Self-Attention Generative Adversarial Networks
- https://arxiv.org/abs/1805.08318
- [Submitted on 21 May 2018 (v1), last revised 14 Jun 2019 (this version, v2)]

---

## Summary

이전 GAN 모델의 단점
- previous models rely heavily on convolution to model the dependencies across different image regions.
- convolution operator has a local receptive field, long range dependencies can only be processed after passing through several convolutional layers.
- small model may not be able to represent long-term dependencies, optimization algorithms may have trouble discovering parameter values
- Increasing the size of the convolution kernels loses the computational and statistical efficiency obtained by using local convolutional structure      


**Self-Attention Generative Adversarial Networks (SAGANs)**
![image](https://user-images.githubusercontent.com/70581043/130214726-fe814675-63af-4517-9339-c94af014d526.png)
- attention mechanism into convolutional GANs.
- helps with modeling long range, multi-level dependencies across image regions.
- 구조
> - f, g 두 feature spaces를 계산한 후, softmax ![image](https://user-images.githubusercontent.com/70581043/130215031-d799ba2c-df0b-4a9c-8a67-cdc6343970c7.png)
> - Beta와 h를 합친 후, 1x1 conv layer를 적용함 ![image](https://user-images.githubusercontent.com/70581043/130215363-811bca02-4996-44e1-bc64-a671589b310b.png)
> - 최종 아웃풋 : 마지막 attention layer를 통과시킨 것과 input을 합친다. ![image](https://user-images.githubusercontent.com/70581043/130215558-bd0527fb-19f1-4769-9b98-79f51c912aa3.png)      

**Techniques to Stabilize the Training of GANs**
1. Spectral normalization
> - discriminator : constrains the Lipschitz constant of the discriminator by restricting the spectral norm of each layer. & does not require extra hyper-parameter tuning & the computational cost is also relatively small
> - generator : can prevent the escalation of parameter magnitudes and avoid unusual gradients.
> - use fewer discriminator updates per generator update, thus significantly reducing the computational cost of training.

2. two timescale update rule (TTUR)
> - advocated using separate learning rates
> - TTUR specifically to compensate for the problem of slow learning in a regularized discriminator, making it possible to use fewer discriminator steps per generator step      

## Result
![image](https://user-images.githubusercontent.com/70581043/130216319-41ff76be-6f1c-43a3-9576-a038f60d36ef.png)
- spectral normalization (SN) , utilizing imbalanced learning rates (TTUR).
- 왼쪽 : baseline, Generator와 discriminator 데이터 1:1 균형있게 훈련시켰지만 결과는 unsable
- 가운데 : SN을  Generator와 discriminator 둘 다 적용, 1:1 균형있게 훈련, 성능이 좋아지긴 했지만 중간에 성능 향상이 떨어짐
- 오른쪽 : TTUR까지 적용, stabilization techniques for GANs’ training.

![image](https://user-images.githubusercontent.com/70581043/130216755-a3a23db5-7d90-415c-b993-099a06c7b32a.png)
- self attention mechanism을 서로 다른 stage에 적용시킴
- middle-to-high level feature maps에 적용시켰을 때 성능이 더 좋다.]
- self-attention block 대신 residual block을 사용했을 때 성능이 더 안 좋아짐

![image](https://user-images.githubusercontent.com/70581043/130217177-079533e6-90a1-472e-b8a9-d9755f68d628.png)
- 다른 GAN 모델과 비교했을 때 SAGAN 성능이 훨씬 더 좋았다.