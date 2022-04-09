# Perceiver: General Perception with Iterative Attention

### Perceiver
image, point clouds, audio, video, video+audio 서로 다른 modalities들을 동일한 architecture로 처리할 수 있는 transformer 구조를 제안했다.

![image](https://user-images.githubusercontent.com/70581043/160243668-6b89b5a7-6577-47ed-ac98-a1c99d40ecea.png)

- a cross-attention module that maps a **byte array** (e.g. an pixel array) and a latent array to a **latent array**
- Transformer tower that maps a latent array to a latent array.
    - Transformer를 훨씬 더 deep하게 디자인 함.
    - latent transformer는 GPT2  구조를 따름
    - decoder는 original transformer 구조를 따름
- cross-attention module
   - 기존 Query-Key-Value (QKV) 와 다른 점 : K와 V는 byte array, Q는 latent array에 projection시키면 계산 복잡도가 훨씬 줄어든다.
   -  allow the latent array to iteratively extract information from the input image as it is needed
   - more cross-attends leads to better performance (but increases the computational requirements of the model because it increases the number of layers with linear dependence on the input size)
- positional encodings
    - Fourier feature position encodings
    - directly represent the position structure of the input data 
    - control the number of frequency bands in our position encoding independently of the cutoff frequency,
    - uniformly sample all frequencies up to a target resolution.
    - ![image](https://user-images.githubusercontent.com/70581043/160244227-0d1e2f81-b464-4efd-b782-00102ac2d8ef.png)
