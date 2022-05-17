# Clinical Prompt Learning with Frozen Language Models

### 기존 NLP는?
- large Pre-trained language model (PLMs)를 사용했다.
- 크게 2가지 종류가 있음 1) BERT, 2)GPTs
- PLM 모델을 fine-tuned한 다음에 downstream tasks를 디자인할 수 있다.
- 단점 : PLM으로 학습시키지 않은 text를 넣게 되면 성능이 떨어진다. 만약 non-medical text로 훈련을 시켰다면 medical text에 대한 성능이 별로 좋지 않을 것이다. 이를 해결하기 위해서 specific-task를 잘 수행할 수 있도록 train시키기도 함 하지만 fine-tuning하는 데 많은 cost가 소요되고 generality가 좋지 않다.
- prompt learning을 사용해서 PLMs training objectives와 downstream task의 gap 차이를 줄이고자 한다.
- prompt learning의 장점 : few-shot, low resources settings, relying on frozen PLMs

###  Traditional fine-tuning
![image](https://user-images.githubusercontent.com/70581043/168828832-1df18686-b408-490f-8e9e-52198a2512e1.png)
- input text _x_ → PLM 모델 넣고 → aggregation algorithm을 사용해서 embedding을 singular senetence embedding으로 표현 → classification을 수행할 수 있는 MLP 통과 → softmax → 확률을 구한다.
- softmax : 
![image](https://user-images.githubusercontent.com/70581043/168829283-0289d85f-801a-4666-8156-37f1ccb0d79d.png)

### Prompt Learning
![image](https://user-images.githubusercontent.com/70581043/168829346-ec261eb4-3909-4b77-909b-ff8a781ef31d.png)
- input text _x_ → x' template을 만든다. x'=[original text, promt, MASK] → PLM 모델 통과 → masked token 예측 → Verbalizer로 예측한 vocabulary 를 알맞은 class로 변환 → pass through standard language model
![image](https://user-images.githubusercontent.com/70581043/168829955-044278e0-ca76-4693-80b4-1f9fe2240599.png)
- prompt를 manual하게 짜야 한다는 단점
### soft template and verbalizer in prompt learning
![image](https://user-images.githubusercontent.com/70581043/168829854-2b0f21de-2306-4aad-a31b-9f3bcdb23068.png)
- create trainable or soft prompt components.
- replaces the fixed manual components with trainable embeddings (continuous vectors) of same dimension as the original PLM
- soft template : optimized during traning
- Soft verbalizer : 더이상 mapping할 수 없음. trainable vectors는 sematnic meaning이 없기 때문에, 대신 matrix operator로 기능한다.
![image](https://user-images.githubusercontent.com/70581043/168831147-128fc0c6-4508-48ba-aa4a-310de4d952b9.png)

### 그 외,
- Bio-ClinicalBERT 모델 사용함
- 데이터셋 : MIMIC-III
- tasks : ICD9 50가지 예측하기, ICD9 20가지 분류하기, 사망여부 예측, ICU 머무는 기간 예측
- 결과 : 
    -  prompt learning can match or improve on traditional fine-tuning,

![image](https://user-images.githubusercontent.com/70581043/168831801-da538942-40ac-4fd6-8773-817f46b164ab.png)
