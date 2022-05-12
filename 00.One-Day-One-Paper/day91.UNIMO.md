# UNIMO: Towards Unified-Modal Understanding and Generation via Cross-Modal Contrastive Learning

#### UNIMO
single model처럼 text 및 image 각각 처리할 수도 있고, multi-modal 처럼 image와 text를 결합시켜서 처리할 수도 있는 모델을 제안했다.
![image](https://user-images.githubusercontent.com/70581043/168039746-bd78ea21-7cda-4ca8-b14f-e2b9a8be261e.png)
- 기존 CV 혹은 NLP 모델들은 image-text 결합 모델을 처리할 수 없고, image-text 결합 모델은 CV/NLP 성능이 떨어졌는데 이 논문에서는 두 개를 합친 것!    
![image](https://user-images.githubusercontent.com/70581043/168040370-dac46948-61ca-42f9-b31c-3541ed2ccd6f.png)

- input으로 image, text, imate-text pair 3 가지가 들어가고 이들을 동일한 공간에서 처리하기 위해서 **CMCL** (Cross-modal contrastive learning) 을 제안했다.    
    - Joint visual learning on image collections, language learning on text corpus and cross-modal learning on image-text pairs 
    - not only improve the capability of visual and language understanding and generation, 
    - but also enable the textual knowledge and visual knowledge to enhance each other in the unified semantic space.
    - imgae-text pair : positive examples(X+), negative examples (X-)
    - single modal information : text(X^T), image (X^I)
    - ![image](https://user-images.githubusercontent.com/70581043/168040856-22dbb850-b3fc-4f04-9090-bcf15489398e.png)

- 더 다양한 cross-modal information을 만들기 위해서 **text rewriting techniques**를 제안
    - sentence-level, phrase-level and word level 별로 text를 생성함
- Image/Text Retrieval : each image-text pair is further augmented with various related images and texts that retrieved from the single-modal data.
- Visual Learning 
    - the model is trained to reconstruct the masked regions v_m given the remaining regions v_\m: ![image](https://user-images.githubusercontent.com/70581043/168041867-21c62227-f035-4319-b813-3c6b9a6d642f.png)
    - the model is trained to reconstruct the masked regions v_m given the text W and the remaining regions v_\m: ![image](https://user-images.githubusercontent.com/70581043/168041961-6d8be3d8-223f-4ebb-a8a9-708e9f56496a.png)

- Language Learning : Bidirectional prediction. & Seq2Seq generation.
