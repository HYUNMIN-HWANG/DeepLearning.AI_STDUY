# data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language

NLP, vision, speech를 같은 method를 사용해서 처리할 수 있는 data2vec를 제안했다. (data2vec, a framework for general self-supervised learning that works for images, speech and text where the learning objective is identical in each modality.)         

![image](https://user-images.githubusercontent.com/70581043/154684349-9c4760a1-7eb3-481b-b51e-624b08dbdcd8.png)
[과정]
1. input 데이터를 learning task에서 teacher mode로 설정한다. (Our method uses a teacher network to first compute target representations from an image, a piece of text, or a speech utterance. )
2. input샘플을 encode해서 mask 버전을 만든다. 이를 사용해서 full data representation을 예측하는 student mode를 설정한다. (we mask part of the input and repeat the process with a student network, which then predicts the latent representations of the teacher)
3.  teacher 가중치는 student의 평균의 지수승만큼 감소한다. (The teacher network is identical to the student model but with weights that are slightly out of date.)         

[Method]
- model architecture : Use standard Transformer architecture 
- masking : MASK embedding token and feed the sequence to the Transformer network
- training target : contextualized-representation , encoding the particular time-step but also other information from the sample 
- teacher parameterization : EMA(exponentially moving average) 
- targets : output of the top K blocks of the teacher network for time-steps which are masked in student-mode
- Loss : Smooth L1 loss  ![image](https://user-images.githubusercontent.com/70581043/154685981-74f634ea-47ff-47d9-b620-149a5301515c.png)

[Results]
![image](https://user-images.githubusercontent.com/70581043/154686106-c9d63bc3-7119-4d72-95c4-e13ed72b89a9.png)
- we pretrain data2vec on the images of the ImageNet-1K training set
- data2vec outperforms prior work with ViT-B and ViT-L in the single model setting

![image](https://user-images.githubusercontent.com/70581043/154686248-7eadd694-89a2-4d7b-9c98-3e12315b7e1a.png)
- pre-train data2vec on the 960 hours of speech audio data from Librispeech (LS-960)
- learning discrete units is not required when rich contextualized targets are used
- learning contextualized targets during pre-training improves performance

![image](https://user-images.githubusercontent.com/70581043/154686527-2987a586-4f67-47ab-b7c4-5ff3017e3f68.png)
- data2vec outperforms the RoBERTa baseline
- successful pre-trained NLP model which does not use discrete units as the training target.
- the model predicts a contextualized latent representation emerging from self-attention over the entire unmasked text sequence.
- the set of training targets is not fixed

[의의]
- continuous and contextualized ; 특정한 target으로 고정시키는 것보다 더 풍부한 representation을 만들 수 있다.
- data2vec has no limitation on the number of target units.
- data2vec is the first work that does not rely on pre-defined target units
