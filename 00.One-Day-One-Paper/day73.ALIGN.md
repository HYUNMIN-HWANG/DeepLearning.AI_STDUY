# Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

## ALIGN (A Large-scale ImaGe and Noisy-text embedding. Image and text encoders are learned)
요약 : 기존 Vision-Language 훈련과 달리, 데이터 전처리를 간소화시켜 대용량의 데이터 (one-billion image-text pair)를 사용해서 모델을 훈련시켰다.


### 기존 visual and vision-language representation learning 특징
- studied separately with different training data sources
- requires heavy work on data gathering, sampling, and human annotation, and hence is difficult to scale
- require even heavier work on human annotation, semantic parsing, cleaning and balancing.
- 즉, 전처리에 많은 cost 가 필요했다.

### 제안 : ALIGN 
![image](https://user-images.githubusercontent.com/70581043/155691700-4bc16429-f3ae-4eba-8f15-aa272570c781.png)
- leverage a dataset of over one billion noisy image alt-text pairs to scale visual and vision-language representation learning.
- large noisy dataset
- aligns the visual and language representations in a shared latent embedding space using a simple dual-encoder architecture.
- Image and text encoders are learned via a contrastive loss

## Pre-training and Task Transfer
- pre-train ALIGN using a dual-encoder architecture
- image encoder : EfficientNet with global pooling
- text encoder : BERT with [CLS] token embedding
- optimized via normalized softmax loss
- treat matched image-text pairs as positive and all other random image-text pairs that can be formed in a training batch as negative
![image](https://user-images.githubusercontent.com/70581043/155692738-7ede3ff3-adf9-42bb-af71-2d1b66c5417e.png)
- evaluate ALIGN models on image-to-text and text-to-image retrieval tasks, with and without finetuning.

## Results
- Image-text retrieval results
![image](https://user-images.githubusercontent.com/70581043/155692928-49cc7fa9-c119-4bbe-beb4-e7b505eb0d50.png)
ALIGN achieves SOTA results in all metrics of Flickr30K and MSCOCO benchmarks.

- ImageNet classification results
![image](https://user-images.githubusercontent.com/70581043/155693421-8fc65525-94bc-4e34-8d87-1d939d98f754.png)
ALIGN slightly outperforms CLIP and achieves SOTA result of 85.5% top-1 accuracy.