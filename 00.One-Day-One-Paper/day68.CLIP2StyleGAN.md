# **CLIP2StyleGAN**: Unsupervised Extraction of StyleGAN Edit Directions


## Abstract
- 기존 StyleGAN의 한계점 : 결국 인간이 훈련시킨 데이터에 한정되어 결과물이 나온다. 창의적인 새로운 결과물이라고 보기 힘들다.
-  제안 : StyleGAN + CLIP을 합친 모형
- **CLIP**
     - embedding spaces have been learned for image/text embedding on very large internet-scale data.
     - zero-shot tasks 수행

**제안하는 방법 3가지**
1. how can we identify interesting directions, in a data-driven sense, by analyzing the CLIP image space
    - compute a set of directions in the CLIP latent space that capture statistically significant variations within the dataset.
    - using the pre-trained image encoder with the ViT-B/32 implementation
    - PCA 사용 -> assumes the underlying data comes from an approximately Gaussian distribution.

2. if the above directions are entangled according to textual concepts, then how to disentangle the directions
    - normalization : x = x / ||x||
    - goal of output : a set of words
    - zero-shot classification : the centroid of the normalized values x in the CLIP image space
    - token : 
    ![image](https://user-images.githubusercontent.com/70581043/151326467-8e792caf-ea72-411a-822e-5e09f6a9efa8.png)
         - T_E : Text encoder 
         - e : embedding of a word-token
         - goal : word token e를 찾아서 CLIP space x와 동일한 embedding t를 찾는 것
    - loss function : 
    ![image](https://user-images.githubusercontent.com/70581043/151326963-e21ff6b3-6350-4740-b085-e14eb64e34c0.png)
        - L : minimize the cosine distance between t and x while keeping the entropy of z low
![image](https://user-images.githubusercontent.com/70581043/151327593-98e6413e-7989-4f57-a029-05bd388f42f4.png)
 

3. how to transfer the disentangled directions, along with their concept labels, to the StyleGAN space
    - CLIP direction : represent multiple attribute changes
    - disentangle 해야함 > represent that direction as the sum of two or more atomic directions.

![image](https://user-images.githubusercontent.com/70581043/151327752-e3c7b732-352e-47ec-a616-5093946d996c.png)
