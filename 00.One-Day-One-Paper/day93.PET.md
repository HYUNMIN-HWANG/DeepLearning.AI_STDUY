# Exploiting Cloze Questions for Few Shot Text Classification and Natural Language Inference

그동안 NLP 훈련 : text와 관련된 hint를 제공해서 zero-shot learning을 하도록 하거나, cloze-style phrase를 사용해서 pretraining동안에 사전지식을 학습할 수 있도록 했다. 하지만 PET에서는 어떠한 추가적인 label data나 특정 사전지식 없이 NLP를 학습하고자 한다.              

### PET (Pattern-Exploiting Training)
- semi-supervised training procedure와 reformulates input examples as cloze-style phrases 합쳤다.                

#### 큰 틀
![image](https://user-images.githubusercontent.com/70581043/168757865-28916c5b-446a-4141-ba1f-471b675ca11f.png)              
RoBERTa large 모델을 사용했다.
#### PVP Training and Inference
pattern P(x)가 v(l) label을 갖게 될 모델 M의 확률             
![image](https://user-images.githubusercontent.com/70581043/168758102-227c4c52-ca29-4b31-8aae-5abaa81aa3bd.png)
이를 softmax에 통과시킨다           
![image](https://user-images.githubusercontent.com/70581043/168758461-23d51f59-4e08-4e20-b958-7728263a7b9e.png)
그 후, q_p와 true distribution 사이에 cross-entropy를 구한다.
 
#### Combining PVPs
![image](https://user-images.githubusercontent.com/70581043/168758750-4a5a38b8-dfa1-4720-9609-6b100e38957d.png)           
데이터 D로부터 annotation된 data를 사용한 M 모델들을 앙상블

---
참고 : http://dsba.korea.ac.kr/seminar/?mod=document&uid=1829