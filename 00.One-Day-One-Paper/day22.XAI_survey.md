# A Survey on Explainable Artificial Intelligence (XAI): towards Medical XAI
- https://arxiv.org/abs/1907.07374
- [Submitted on 17 Jul 2019 (v1), last revised 11 Aug 2020 (this version, v5)]
---
(총 22 페이지라서 이틀 동안 나눠 읽겠습니다.)

## TYPES OF INTERPRETABILITY
### A. Perceptive Interpretability
인간이 인지한 것을 기반으로 해석 가능하다.
![image](https://user-images.githubusercontent.com/70581043/130380362-a66e4406-88f8-46b6-a821-1b6158446386.png)
**A.1) Saliency**
- input 요소 중에서 결정을 내리는데 큰 기여를 한 것이 무엇인지 설명
- v(x<sub>i</sub>) ← the component x<sub>i</sub> is a significant reason for the output y
- 1) Class Activation Map (CAM) : M<sub>c</sub>(x,y) = ![image](https://user-images.githubusercontent.com/70581043/130389943-ed659631-bfa2-4682-a2ed-c501098dfd16.png), generate heat/saliency/relevance map
- 2) Layer-wise Relevance Propagation(LRP) : ![image](https://user-images.githubusercontent.com/70581043/130390205-f0126584-0dd8-4681-816d-10084eadf07a.png), decomposition method
- 1)과 2) 공통점 : certain ways of interaction between weights and the strength of activation of some units within the models
- 앞으로 방향 : 시각적인 검증을 넘어선 증거를 시스템적으로 검증하는 시도가 필요하다.

**A.2) Signal Method**
- Methods of interpretability that observe the stimulation of neurons or a collection of neurons
- 1) Feature maps and Inversions for Input Reconstructions 
> - feature map은 인간이 지각할 수 있는 특징을 제외하고 대부분 흐릿한 이미지로 보인다.
> - inverse convolution map : ![image](https://user-images.githubusercontent.com/70581043/130391530-c67b8445-bad1-4f7f-a35d-5b9c47444154.png), x~ does appear like slightly blurred version of the original image

- 2) Activation Optimization
> - activation maximization : finding input images that optimize the activation of a neuron or a collection of neurons.
> - x<sub>0</sub> = ![image](https://user-images.githubusercontent.com/70581043/130392608-636dfc4e-b575-4c4f-ba66-7ea53240fa8b.png)
> - the optimized input that maximizes the activation of the neuron(s) 
> - visualization of activations within a higher-level organization and semantically more meaningful arrangements.

**A.3) Verbal Interpretability** 
- the form of verbal chunks that human can grasp naturally.
- a cognitive chunk is defined as a clause of inputs in DNF and the number of (repeated) cognitive chunks in a rule set is varied.

### B. Interpretability via Mathematical Structure
![image](https://user-images.githubusercontent.com/70581043/130396413-85e39d7b-4ce6-4a3b-9ffc-018ee0e40f11.png)

**B.1) Pre-defined Model**
- 시스템을 더 잘 이해할 수 있다면, 더 복잡한 구성 요소를 포함하여 공식을 더 향상시킬 수 있다. 
- Linearity : 모델이 linear 하다면 설명 가능성이 높다. 하지만 linear 하지 않은 모델들이 많다. f(h<sub>k</sub>) = softmax(Wh<sub>k</sub> +b) 사용, 얼마나 아웃풋을 잘 예측하는지 알 수 있음
- General Additive Models(GAM) : ![image](https://user-images.githubusercontent.com/70581043/130397593-1b0f181d-f0ab-4409-9f63-7a3bc53bd523.png)
- Content-subject-specific model : Some algorithms are considered obviously interpretable within its field.

**B.2) Feature Extraction**
- 가장 중요한 예측 변수로부터 더 많은 정보를 얻을 수 있다.
- Correlation : covariance matrix and correlation coefficients after transformation by kernel functions, Principal Component Analysis(PCA), Canonical Correlation Analysis (CCA), SVCCA
- Clustering : cluster input images based on their activation of neurons in a network, distance between objects being considered.

**B.3) Sensitivity**
- group together methods that rely on localization, gradients and perturbations under the category of sensitivity
- Sensitivity to input noises or neighborhood of data points : rely on the locality of some input x
- Sensitivity to dataset : to understand the effect of removing x<sub>i</sub> for some i and shows the consequent possibility of adversarial attack

**B.4) Optimization**
- Quantitatively maximizing interpretability (LIME, MUSE)
- Activation Optimization : The interpretability relies on direct observation of the neuron-activation-optimized images.

---

### C. Other Perspectives to Interpretability
각기 다른 task 마다 필요한 interpretability 방법이 다르다. 어떻게 고를 것인가?

**C.1) Data-driven Interpretability**
- Data in catalogue. : 카테고리 별로 정렬한다. 어떻게 많은 카테고리들을 큰 하나의 행렬로 모을 것인가? → crowd-sourcing, pick latent dimensions (common criteria)
- Incompleteness : 하나의 의견으로 모여지지 않을 때가 있다. 장점은 서로 다른 지지에 대한 강력한 근거가 있다는 것, 단점은 해석 가능성 기준에 미치지 못한다.

**C.2) Invariances**
- Implementation invariance : functionally equivalent functions, 속성을 사용하지 않고도 진술을 확장할 수 있다.
- Input invariance : translating an image을 하면 super-pixels 경계도 translate 한다.

**C.3) Interpretabilities by Utilities**
- Application-based : 이미 설명하능한 모델을 기반으로 같은 작업을 수행한다.
- Human-based : 사람이 평가한 것과, 컴퓨터가 평가한 것을 비교한다.
- Functions-based : use metrics

## XAI IN MEDICAL FIELD
의학분야에서는 다른 분야와 다르게 risk and responsibilities를 고려해야 한다.
