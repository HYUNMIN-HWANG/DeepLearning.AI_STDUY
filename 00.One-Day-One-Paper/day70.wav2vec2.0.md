# wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations

wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned.

![image](https://user-images.githubusercontent.com/70581043/154834428-8aa76910-a039-4e49-a754-58c5ef681aa4.png)
1.  encodes speech audio via a multi-layer convolutional neural network : 
input raw audio X and outputs latent speech representations z1, . . . , zT for T time-steps.
2. masks spans of the resulting latent speech representations 
3. fed to a Transformer network to build contextualized representations ; capturing information from the entire sequence & quantization
4. the model is trained via a contrastive task where the true latent is to be distinguished from distractors

- training ; ( pre-training on unlabeled speech) learn discrete speech units to represent the latent representations in the contrastive task
- fine-tuning ;  fine-tuned on labeled data with a Connectionist Temporal Classification (CTC) loss
- objective ; ![image](https://user-images.githubusercontent.com/70581043/154834662-13d59c97-ffe7-4bd4-92f3-b666ea792d59.png)
    - Contrastive Loss : 
![image](https://user-images.githubusercontent.com/70581043/154834676-a4e52c88-4f42-4823-982e-be965ae244f6.png)
requires to identify the true quantized latent speech representation for a masked time step within a set of distractors. 

    - Diversity Loss : 
![image](https://user-images.githubusercontent.com/70581043/154834679-934f0b43-b4ef-46a5-87ac-0a641314e39c.png)
encourage the model to use the codebook entries equally often.

