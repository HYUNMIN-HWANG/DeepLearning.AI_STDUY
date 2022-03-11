# A Simple Framework for Contrastive Learning of Visual Representations

## SimCLR
![image](https://user-images.githubusercontent.com/70581043/157814812-682a8bcc-47ca-46ff-b2a7-f49e0484264a.png)

- contrastive selfsupervised learning algorithms 
   - stochastic data augmentation : 주어진 data를 각각 x_i, x_j로 augmentation시킴, 이 둘은 각각 x에 대해서 positive pair를 이룬다. 
   - neural network base encoder (f) : 여기서는 RseNet을 사용하여 extract representation vector했다.
   - projection head (g) : ReLU 사용
   -  contrastive loss function : contrastive prediction task를 수행함, x_i, x_j positive pair 로 훈련시켰다면, x_i가 주어졌을 때 이에 대응되는 x_j를 찾는 task를 시행한다. / NT-Xent loss 사용
   - loss function : ![image](https://user-images.githubusercontent.com/70581043/157815640-fc78c226-72b2-4dc5-bae8-deb012aa7968.png)

- Contributions 3가지
    1. Composition of data augmentation
       - spatial/geometric transformation :  cropping, resizing, cutout 
       - appearance transformation : color distortion, Gaussian blur, Sobel filtering
       - augmentation을 하나만 하는 것보다 두 개 같이 사용하는 것이 더 성능이 좋다. 특히, random cropping & random color distortion 함께 사용했을 때 가능 좋았음
![image](https://user-images.githubusercontent.com/70581043/157816130-d9d96d9f-5dc2-4666-80db-d5d498dbfbb2.png)

    2. leanable nonlinear transformation
        - nonlinear projection is better than a linear projection (+3%), and much better than no projection (>10%). 
![image](https://user-images.githubusercontent.com/70581043/157816289-193e1931-8d14-4115-bd8c-32dd5b8ea89f.png)

    3. contrastive learning benefits from larger batch size and more training steps 
       - the number of training epochs is small (e.g. 100 epochs), larger batch sizes have a significant advantage over the smaller ones.
       - larger batch sizes provide more negative examples, facilitating convergence
![image](https://user-images.githubusercontent.com/70581043/157816569-773cee1f-eee6-4f0f-90b6-ff2e7f69b901.png)
