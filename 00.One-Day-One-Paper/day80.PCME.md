# PCME

- Cross-modal retrieval methods 중 하나로, image와 caption 두 가지 modality를 잘 representation할 수 있는 ebmedding space 모델을 제안했다.
- contributions :
   1. joint embedding space for cross modal retrieval을 사용하여 one-to-many realtionships를 표현함
   2. 기존 cross-modal retrieval 의 단점을 극복
   3. joint embedding space를 분석
---
![image](https://user-images.githubusercontent.com/70581043/162155221-1029873e-1ada-4a42-949e-0ca8e7924bd9.png)
- visual encoder : ResNet image encoder를 사용함, 
![image](https://user-images.githubusercontent.com/70581043/162155420-f67759d8-c2f0-44a5-9ca5-924d89fe5586.png) -> ![image](https://user-images.githubusercontent.com/70581043/162155468-34daff39-8411-402e-8f2c-ca8c2b56bff0.png) -> GAP -> linear layer
- textual encoder : GloVe,
![image](https://user-images.githubusercontent.com/70581043/162155730-43e50483-9837-447b-88db-7cc1352228a3.png) -> ![image](https://user-images.githubusercontent.com/70581043/162155792-1cef88c8-6a7c-4e48-9ed1-bc93c89f9ede.png) 
- loss : contrastive or triplet loss
- Probabilistic embeddings for a single modality : Hedged Instance Embeddings (HIB) 기반 
    - Soft contrastive loss :  ![image](https://user-images.githubusercontent.com/70581043/162156082-3a75e464-d730-421a-9951-cc2506ee18e8.png) -> Factorizing match probability : ![image](https://user-images.githubusercontent.com/70581043/162156129-bfb991f9-7a1e-42f2-a5e8-7c4226ff1cb4.png) -> Match probability from Euclidean distances : ![image](https://user-images.githubusercontent.com/70581043/162156182-649ee14a-2c24-4907-a35d-e48af81cb50a.png)

---
![image](https://user-images.githubusercontent.com/70581043/162156420-738e289a-aa32-4d14-9e82-e6d8213b0e1d.png)

- vision part에서만  sigmoid, LN, L2 사용함
- caption part에서는 사용하지 않음
