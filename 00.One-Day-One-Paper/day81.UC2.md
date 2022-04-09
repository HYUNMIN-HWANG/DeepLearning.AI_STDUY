# UC2: Universal Cross-lingual Cross-modal Vision-and-Language Pre-training

- the first machine translation-augmented framework for cross-lingual cross-modal representation learning.
![image](https://user-images.githubusercontent.com/70581043/162560470-a3c06962-ab69-43b2-9b42-fec265f92ccf.png)

- 이미지와 영어 텍스트 pair 되어 있는 데이터 셋을 사용 -> augmentaiton : Machine translation을 사용해서 영어를 중국어, 독일어 등으로 번역 -> standard masked languages modeling 방법을 사용하여 모델링 -> Image-text matching training task 진행
- propose two novel pre-training tasks, 
- Masked Region-to-Token Modeling (MRTM) : encourages fine-grained alignment between words and image regions, by sharing
the embedding space of word tokens and region labels 
- Visual Translation Language Modeling (VTLM) : designed to jointly learn cross-lingual cross-modal mapping from parallel textual corpora and paired images. 
- Image Encoder : Faster R-CNN, sequence of image region features & For each region, extract location features via a 7-dimensional vector -> LN -> FC layer -> region feature is then obtained via summing up the projected region feature and location feature
- Cross-lingual Language Encoder : XLM-R, sentence piece model을 사용하여 tokenize an input sentence -> embedding -> final
representation of each token is obtained via summing up its word embedding, segment embedding, and position embedding