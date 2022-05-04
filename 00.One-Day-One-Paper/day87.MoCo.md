# Momentum Contrast for Unsupervised Visual Representation Learning

### Momentum Contrast (MoCo) 
contrastive learning 방법 중 하나 : queue형태의 dictionary를 정의하여 많은 negative sample을 저장할 수 있도록 했다. 
![image](https://user-images.githubusercontent.com/70581043/166626566-42cdef9d-c186-4a87-8ade-da93a758417a.png)
- q : query 
- {k_0, k_1, k_3, ,,, } : key
- 현재의 mini-batch에 있는 것을 enqueue하고, 가장 오래된 mini-batch를 dequeue한다.
- momentum update 방식을 사용해서, key가 query 보다 더 천천히 encode시켜 둘의 차이를 줄인다. > consistent를 높일 수 있음

#### Contrastive Learning
InfoNCE 
![image](https://user-images.githubusercontent.com/70581043/166626809-0b4f9ebf-320f-4026-b2f5-2c8642ffd894.png)


#### Momentum Contrast
- 가정 : Our hypothesis is that good features can be learned by a large dictionary that covers a rich set of negative samples
- Queue : The samples in the dictionary are progressively replaced. The current mini-batch is enqueued to the dictionary, and the oldest mini-batch in the queue is removed.
- Momentum update : key parameter가 queue parameter보다 천천히  evolve할 수 있다. momentum이 클 수록 효과가 좋았다.
![image](https://user-images.githubusercontent.com/70581043/166626918-8e054f6f-b9b8-469c-8b35-6792f8c04bff.png)
 
#### pseudo-code of MoCo
![image](https://user-images.githubusercontent.com/70581043/166627028-19386f48-2891-4675-82fe-c59d3a9ef899.png)
- encoder : ResNet + last layer : FC layer
- L2 norm
- augmentation : a randomly resized image, and then undergoes random color jittering, random horizontal flip, and random grayscale conversion, all available in PyTorch’s torchvision package.
- shuffling BN 

### Results
![image](https://user-images.githubusercontent.com/70581043/166627149-790f8cdc-d559-427d-b40c-bb0f220e1b8c.png)
