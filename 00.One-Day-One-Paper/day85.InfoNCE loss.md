# Representation Learning with Contrastive Predictive Coding

**Proposed :**
   1. compress high-dimensional data into a much more compact latent embedding space
   2. use powerful autoregressive models in this latent space to make predictions many steps in the future
   3. Noise-Contrastive Estimation for the loss function

**Contrastive Predicting Coding :**
- motivation : to learn the representations that encode the underlying shared information between different parts of the (high-dimensional) signal. 
- modeling p(x|c) 를 바로 예측하는 것이 아니라, density 비율을 모델링함으로써 mutual information을 최대화시킨다.
![image](https://user-images.githubusercontent.com/70581043/164389472-b36e1bee-89b5-48c8-ac13-90182f9b1951.png)

![image](https://user-images.githubusercontent.com/70581043/164388905-22f0c3f1-2400-4f2c-89c0-4d594644f82f.png)
1. non-linear encoder g_enc : CNN, ResNet v2, 1D-convolution + ReLU + mean-pooling
2. autoregressive model g_ar : GRU, RNN, GRU PixelRNN


do not predict future observations x_t+k directly with a generative model p_k(x_t+k|c_t). Instead we model a density ratio which preserves the mutual information between x_t+k and c_t
![image](https://user-images.githubusercontent.com/70581043/164389840-be51f828-3354-46c8-bd72-710f68a05b11.png)
그리고 normalization하기 위해서 log-bilinear model을 사용함
![image](https://user-images.githubusercontent.com/70581043/164389869-a04dba11-9c4d-4044-9eb3-0561dc175a3b.png)


**InfoNCE Loss :**
 ![image](https://user-images.githubusercontent.com/70581043/164406901-18c621c3-2735-43d4-8e16-e020058674af.png)
- Equation 4 is the categorical cross-entropy of classifying the positive sample correctly,
