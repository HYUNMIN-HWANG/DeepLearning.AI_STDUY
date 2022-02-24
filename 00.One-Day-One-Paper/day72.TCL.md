# Vision-Language Pre-Training with Triple Contrastive Learning

### TCL (trupiple contrastive learing)
![image](https://user-images.githubusercontent.com/70581043/155492302-5fa13793-377c-465c-8bf0-3c76dbca881b.png)
요약 : vision과 text 데이터를 pair 로 학습시키기 위해서 세 가지 constrastive module을 사용해 훈련시켰다.

- stage 1 :  align cross-modal features by using a contrastive loss to pull the embeddings of matched image-text pairs together while pushing those of non-matched pairs apart
    - aims to maximize the mutual information (MI) between matched image-text pair
- stage 2 : apply a fusion encoder to the aligned image and text representations to learn joint embeddings
    - fusion encoder에 들어가기 전에 alignment module(3 constrastive modal ) 을 거친다. 
- 3 constrastive modal 
    - **CMA ( cross-modal alignment)** - pulls the embeddings of matched image-text pairs together while pushing those of non-matched pairs apart by maximizing global MI between matched image and text, by minimizing InfoNCE loss, 
    - **IMC (intra-modal contrastive)** -  maximizes agreement between differently augmented views of the same data example through maximizing their global MI, guarantee reasonable intramodal representation learning
    - **LMI (local MI maximization)** - encourages high MI between the global representation and every local region of the input, forces the model to also capture fine-grained information and in turn to benefit joint representation learning
- 효과 :  1. learn representations that are semantically meaningful not only for cross-modal image-text pairs but also for intra-modal inputs & 2. capture the structural and localized information by extracting relevant features that are shared across local patches/tokens
- Encoder 
   - vision encoder : ViT-B/16 with 12 layers and 85.8M parameters
   - text encoder & fusion encoder : a 6-layer transformer and are initialized by the first 6 layers and the last 6 layers of BERT-base which contains 123.7M parameters.