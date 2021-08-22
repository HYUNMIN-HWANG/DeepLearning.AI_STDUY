# Explainable Artificial Intelligence: Understanding, Visualizing and Interpreting Deep Learning Models
- https://arxiv.org/abs/1708.08296
- [Submitted on 28 Aug 2017]
---

**Black box mode**l : 구체적으로 어떤 input feature가 해당 모델의 결과에 어떤 영향을 끼쳤는지 모른다.     



설명 가능한 AI 모델을 만드는 것이 중요하다. 왜?
- Verification of the system: Black box 시스템은 신뢰성이 없다.
- Improvement of the system: AI 시스템을 향상시키기 위해서는 약점이 무엇인지 알아야 한다. 설명 가능성이 있을 때 다른 모델과의 차이점을 알 수 있고 모델에 필요한 것이 무엇인지 알 수 있다.
- Learning from the system: AI 시스템으로부터 새로운 통찰력을 얻을 수 있다. 
- Compliance to legislation: “right to explanation” 왜 그런 결정을 내렸는지 설명할 수 있어야 한다.

## Methods
### 1. Sensitivity Analysis (SA)
![image](https://user-images.githubusercontent.com/70581043/130353432-82ace53f-fae2-482c-810d-138a79406f36.png)
- explains a prediction based on the model’s locally evaluated gradient (partial derivative).
- the most relevant input features are those to which the output is most sensitive
- does not explain the function value f(x) itself, but rather a _variation_ of it
- heatmap : which pixels need to changed to make the image look (from the AI system’s perspective) more / less like the predicted class. → Note that such heatmap would not indicate which pixels are actually pivot for the prediction “rooster”.

### 2. Layer-Wise Relevance Propagation (LRP)
![image](https://user-images.githubusercontent.com/70581043/130353539-39315d80-b743-4307-9561-b7f7f38a7910.png)
![image](https://user-images.githubusercontent.com/70581043/130353570-a2e6db69-59f2-4405-a9b5-e811fb219afb.png)
- explains predictions relative to the state of maximum uncertainty
- pixels which are pivotal for the prediction “rooster”.
- redistributes the prediction f(x) backwards using local redistribution rules until it assigns a relevance score R<sub>i</sub> to each input variable (e.g., image pixel). →  R<sub>i</sub> = how much this variable has contributed to the prediction.
- this rule redistributes relevance proportionally from layer _l + 1_ to each neuron in layer _l_ based on two criteria,
> (1) the neuron activation x<sub>j</sub> : more activated neurons receive a larger share of relevance
> (2) the strength of the connection w<sub>jk</sub> : more relevance flows through more prominent connections

## Results
### 1. Image Classification
![image](https://user-images.githubusercontent.com/70581043/130353783-5600187c-d03f-468e-8b86-e7613af1f06b.png)
- GoogleNet model ( “volcano” and “coffee cup” 분류하기 )
- SA : noise가 많다. 배경그림에 large values R<sub>i</sub>, 각 pixel이 예측 결과에 어느정도 영향을 미치는지 설명 못함, 
- LRP : SA보다 예측 결과를 더 잘 설명함, perturbation analysis 그래프에서 더 빨리 감소하는 경향을 보임 

### 2. Text Document Classification
![image](https://user-images.githubusercontent.com/70581043/130353906-13ffae1c-a474-4011-8165-9d29626e0c3f.png)
- a word-embedding based convolutional neural network (“sci.med” 주제와 관련된 것과 관련 없는 것 분류하기)
- SA : does not distinguish between positive and negative evidence
- LRP : distinguishes between positive (red) and negative (blue) words, provides more informative heatmaps

### 3. Human Action Recognition in Videos
![image](https://user-images.githubusercontent.com/70581043/130354001-60b27661-45ca-4ba2-a9a5-70c080b55a9c.png)
- Fisher Vector / SVM classifier (앉아있는 모습을 인식하는지)
- LRP : correctly classified as showing the action “sit-up”, visualizes the relevant _locations_ of the action, identifies the most relevant _time points_