# AttnGAN: Fin![image](https://user-images.githubusercontent.com/70581043/130043243-1d6f5bb7-a216-4864-8f57-166702bc1c42.png)-Grained Text to Image Generation with Attentional Generative Adversarial Networks
- https://arxiv.org/abs/1711.10485
- Computer Vision and Pattern Recognition (cs.CV)
- [Submitted on 28 Nov 2017]

---

## Summary
text to image GAN에서 attention기능을 추가함. 자연어 지문 중에서 관련된 단어에 attention을 함으로써 관련된 sub image를 합성한다.(AttnGAN can synthesize fine-grained details at different subregions of the image by paying attentions to the relevant words in the natural language description.)

- 기존 text to image GAN 에서 문제점
> - encode the whole text description into a global sentence vector → global sentence vector lacks important fine-grained information at the word level, and prevents the generation of high quality images.

- Attentional Generative Adversarial Network (AttnGAN)
![image](https://user-images.githubusercontent.com/70581043/130041430-7894c68d-ee56-4362-bc96-bd39c3d6981c.png)
### 1. The first component is an **attentional generative network** 
![image](https://user-images.githubusercontent.com/70581043/130042869-79388011-fbc6-4cfb-9a48-94fffc4dc5c6.png)
> - draw different sub-regions of the image by focusing on words that are most relevant to the sub-region being drawn
> - m : generator 개수
> - h : hidden states
> - x : 생성된 이미지
> - z is a noise vector / ![image](https://user-images.githubusercontent.com/70581043/130043243-1d6f5bb7-a216-4864-8f57-166702bc1c42.png) is a global sentence vector / e is the matrix of word vectors / ![image](https://user-images.githubusercontent.com/70581043/130043793-0c288149-2d4a-40c0-940f-238703d388b0.png) represents the Conditioning Augmentation / ![image](https://user-images.githubusercontent.com/70581043/130043872-cb3a5018-7158-4012-afb8-f30f85e1726f.png) is the proposed attention model at the ith stage of the AttnGAN 
> - ![image](https://user-images.githubusercontent.com/70581043/130044464-63b76ecb-88a0-408b-a809-5f4f39a24b4a.png) : word features e , image features from the previous hidden layer h
![image](https://user-images.githubusercontent.com/70581043/130045080-a2e78fab-b75a-4e07-8f10-63f6f321902c.png)
> - ![image](https://user-images.githubusercontent.com/70581043/130045137-70ad0f3b-d91e-4ac1-abd4-67d8627e32a0.png) indicates the weight the model attends to the ith word when generating the jth sub-region of the image.
> - image features and the corresponding word-context features are combined to generate images at the next stage. 

- GAN loss
> generator loss :  ![image](https://user-images.githubusercontent.com/70581043/130045921-17cb2d52-4265-4699-a290-5c85500098e1.png) 
> - unconditional loss : whether the image is real or fake
> - conditional loss : the image and the sentence match or not.
> discriminator loss : ![image](https://user-images.githubusercontent.com/70581043/130046143-dfc50863-f946-4cb3-b41c-9958b7a9becd.png)
> - classify the input into the class of real or fake by minimizing the cross-entropy loss

- AttnGAN to automatically select word level condition for generating different sub-regions of the image.

### 2. The other component in the AttnGAN is a **Deep Attentional Multimodal Similarity Model** (DAMSM). 
> DAMSM : 생성된 이미지와 문장 간의 유사도 측정 (to compute a fine-grained loss for image generation)

- The text encoder
> - bi-directional Long Short-Term Memory (LSTM)
> - represent the semantic meaning of a word.
> - last hidden states of the bi-directional LSTM are concatenated to be the global sentence vector

- The image encoder
> - Convolutional Neural Network (CNN) that maps images to semantic vectors (inception-v3 model pretrained on ImageNet)
> - CNN learn local features of different sub-regions of the image
> - the later layers learn global features of the image.

- The DAMSM loss : the only supervision is the matching between entire images and whole sentences (a sequence of words).
- the DAMSM is able to compute the fine-grained text-image matching loss LDAMSM.

## Result
- evaluation : inception score(quantitative evaluation measure), R-precision(complementary evaluation
metric for the text-to-image synthesis task),
- a larger lamda leads to a significantly higher R-precision rate on both CUB and COCO datasets.
- not only generates images of a higher resolution (from 128x128 to 256x256 resolution), but also yields higher inception scores on both CUB and COCO datasets.
![image](https://user-images.githubusercontent.com/70581043/130068759-425adfed-f838-457c-88a7-a2f75fc77878.png)
- fig 5 : 문장 단어를 조금씩 변경했더니 그림도 변경됨
- fig 6 :  현실에 존재하지 않은 문장에 대해서도 이미지를 생성함
- fig 7 : 동화 속에 나올 법한 새 이미지를 생성함
![image](https://user-images.githubusercontent.com/70581043/130069029-64549859-2093-4951-883d-2805c85a378b.png)
- AttnGAN일 때 inception score가 가장 높다.
