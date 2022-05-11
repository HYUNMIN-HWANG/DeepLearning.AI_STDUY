# Contrastive Learning of Medical Visual Representations from Paired Images and Text (ConVIRT)

- image와 text pair를 contrastive learning을 사용해서 훈련시킨다.
- improves visual representations by maximizing the agreement between true image-text pairs versus random pairs via a bidirectional contrastive objective between the image and text modalities.

![image](https://user-images.githubusercontent.com/70581043/167840970-7be9ac36-246a-42c5-9e13-b62f35d218f2.png)
- input : X_v (represents of images), X_u (represents of text)
- transformation : t_v (cropping, horizontal flipping, affine transformation, color jittering and Gaussian blur), t_u (randomly sampled sentence)
- encoder : f_v (ResNet50) , f_u(BERT)
![image](https://user-images.githubusercontent.com/70581043/167841698-efd41f46-a0f0-46cd-bc2d-e6e40e689238.png) , ![image](https://user-images.githubusercontent.com/70581043/167841715-267b84af-7feb-4ecf-9077-b6aecbceb4c0.png)
- loss : 
    - an image-to-text contrastive loss for the i-th pair: ![image](https://user-images.githubusercontent.com/70581043/167841805-64bac2c2-0a31-4d9f-87e2-3c501f039555.png)
    - similar text-to-image contrastive loss : ![image](https://user-images.githubusercontent.com/70581043/167841863-fd5a4187-4773-4af1-881d-fcaef111eed8.png)
    - computed as a weighted combination of the two losses averaged over all positive image-text pairs in each minibatch: ![image](https://user-images.githubusercontent.com/70581043/167841936-d2c12fb7-03b9-4e8c-9b51-6a4915a2a52d.png)


#### TASKS & RESULTS
- Image Classification
![image](https://user-images.githubusercontent.com/70581043/167842350-c944308b-3040-4b19-a87e-98d0ee872f71.png)
- Zero-shot Image-image Retrieval
- Zero-shot Text-image Retrieval
![image](https://user-images.githubusercontent.com/70581043/167842383-1ba22395-f008-4339-b82a-299da9654b00.png)
