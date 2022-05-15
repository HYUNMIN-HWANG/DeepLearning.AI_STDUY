# Unsupervised Prompt Learning for Vision-Language Models

기존 Vision-Language Model 은 supervised learning이었기 때문에 image와 text 가 pair되어 있어야 했다. 하지만 pair시키는 데 많은 cost가 들기 때문에 해당 논문에서는 unpaired한 vision-language model을 제안하고자 한다.    
propose an **unsupervised prompt learning (UPL) framework**, which does not require any annotations of the target dataset, to improve the zeroshot transfer of CLIP-like vision-language models. UPL has no dependency on labeled images of the target dataset.

![image](https://user-images.githubusercontent.com/70581043/168454940-398e329f-8aee-4ed5-84b8-5ba99126ba4b.png)
**1. Pseudo Label Generation**
- zero-shot inference of CLIP : 
    - CLIP 모델을 사용해서 large-scale imagetext pairs가 잘 된 모델을 만든다.
    - The prediction probability of class c :  ![image](https://user-images.githubusercontent.com/70581043/168455067-9664ddff-f621-4bf8-872e-7466d70e9d67.png)
    - identify the prediction ![image](https://user-images.githubusercontent.com/70581043/168455075-697e2cf6-5cef-4172-b85d-aa75d91347c9.png)
- Pseudo Label Generation
    - 1) CLIP 결과가 biased preferences 한 결과를 보임 2) confidence와 accuracy가 유사한 결과를 보이지 않음
    - 따라서 advocate to select top-K confident samples per class 방법을 선택함
- Pseudo Label Ensemble
    - 여러 CLIP 모델을 사용하여 ensemble 시킴  

**2. Prompt Representation Optimization**
- Learnable Prompt Representation
    - define the learnable prompt representation V -> define the continuous prompt V_c : ![image](https://user-images.githubusercontent.com/70581043/168455129-454fc711-7720-489b-b185-06129f1f1a4a.png)
    - probability of c-th class : ![image](https://user-images.githubusercontent.com/70581043/168455136-041651f8-3658-4319-94ff-24790f5eac46.png)
- Inference.
- Prompt Representation Ensemble.
    - to learn multi prompt representations with different initializations. 

#### Result
![image](https://user-images.githubusercontent.com/70581043/168455226-78acd104-38de-4bdf-b07c-f554e5610c94.png)
- UPL not only avoids such prompt engineering, but also outperforms CLIP by +4.2 point in terms of the averaged accuracy
- UPL*(leverage additional CLIP models with various vision architectures including) which involves different CLIP models for pseudo-labeling while using the single CLIP with ResNet-50 for training and zero-shot inference, further boosts the averaged accuracy to 68.37.
