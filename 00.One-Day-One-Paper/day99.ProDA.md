# Prompt Distribution Learning (ProDA)

- prompt를 활용한 vision-language model에서 다양한 prompt를 사용하여 data의 distribution을 더 잘 측정할 수 있다.
- automatically learning diverse prompts from data, which can effectively adapt the pre-trained VLM to downstream recognition tasks
- soft prompt(=continuous prompts) : our ProDA estimates a distribution over diverse and informative prompts to capture the variance of visual representations

## Prompt 기본
- “a photo of a {class}.”
- C 개의 categorical class가 있음 그걸 아래와 같은 probability로 class 값을 예측한다.
![image](https://user-images.githubusercontent.com/70581043/174931902-0cd8a314-e796-474f-abbd-5299eea69942.png)
- generate the weight w1:C of the target classifier : prompt tuning : a few training sample를 사용해서 아래의 objective를 최소화시킨다.
- t_c(P) : random하게 initialize한 learnable continuous prompt P를 각각의 class name가 합친 것 -> 이거를 text encoder에 넣는다. 
![image](https://user-images.githubusercontent.com/70581043/174932050-668997cc-a16a-4f6c-82f8-e98006f0631b.png)

## Learning the Prompt Distribution
- our approach ProDA aims to learn the distribution of various prompts.
- learn an optimal prompt distribution p(P), which minimizes the empirical classification loss. -> intractable 함
- 대신에, learn the prompt distribution by learning the distribution of the classifier weights 을 구한다.
- **Optimization** : minimizing the empirical classification loss
![image](https://user-images.githubusercontent.com/70581043/174933722-894befc5-2715-4640-8f58-d99046edc8f8.png)
-> intractable
- 대신 upper bound of the loss 를 구한다. minimizing L_upper를 구한다.
![image](https://user-images.githubusercontent.com/70581043/174934076-3a65a671-4594-478b-80ef-835d3d6fa5e7.png)

## Improving Prompt Diversity
- diverse classifiers are able to enhance generalization
- Position Diversity : insert the category name in the front, middle, and end positions of different prompts.
- Semantic Orthogonality. : We feed the prompts {Pk}Kk=1 without incorporating the category name into the pre-trained text encoder to obtain their semantic embeddings {g(Pk)}Kk=1.
- semantic orthogonality loss : 
![image](https://user-images.githubusercontent.com/70581043/174934316-d19cffbe-b7b0-4464-a417-d2e3f1cbc357.png)

#### pseudo-code of the training procedure
![image](https://user-images.githubusercontent.com/70581043/174934430-91e722a5-e76a-4f6d-b3f7-a4aa6edd4110.png)
