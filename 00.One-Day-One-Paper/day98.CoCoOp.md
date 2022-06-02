# Conditional Prompt Learning for Vision-Language Models

CoOp에서 제시한 모델이 generality가 부족하다는 문제를 해결하기 위해 CoCoOp 모델을 제안했다.

## CoCoOp (Conditional Context Optimization)
![image](https://user-images.githubusercontent.com/70581043/171558351-4f1f4ab8-d3b4-477d-bcc5-63c31ac2064d.png)
- to make a prompt conditioned on each input instance (image) rather than fixed once learned
- extend CoOp by further learning a lightweight neural network to generate for each image an input-conditional token (vector), which is combined with the learnable context vectors
- CoCoOp gains significant improvements over CoOp in unseen classes

![image](https://user-images.githubusercontent.com/70581043/171557767-14e5de03-60ec-4d7b-923c-918e0c957a9a.png)
- CLIP + CoOp + zero-shot 세 가지를 짬뽕한 느낌
- prediction probability :  
![image](https://user-images.githubusercontent.com/70581043/171558470-4d1d3f7e-9dc3-43e6-bea2-8a93d810885c.png)
    - h(.) : Meta Net ( built with two-layer bottleneck structure , image encoder에서 나온 feature 가 MetaNet의 인풋으로 들어간다)
    - pi = h(x)
    - v_i(x) = v_i + pi
    - t_i(x) = {v_1(x), v_2(x), ... , v_m(x), c_i}
    - c_i : word embedding for the class name

### Results
#### Generalization From Base to New Classes
![image](https://user-images.githubusercontent.com/70581043/171559010-397bc1b1-bc9d-4c93-8c65-53faf58d7331.png)
- 11개의 dataset이 있을 때, 각 데이터 셋 class를 기준으로 훈련데이터 / 테스트 데이터로 분리
- trained using only the base classes while evaluation is conducted on the base and new classes separately to test generalizability.
- CoOp는 base classes와 new classes 간의 성능 차이가 큰다. CoCoOp는 성능 gap이 줄어들었다.

#### Cross Dataset Transfer
![image](https://user-images.githubusercontent.com/70581043/171559260-391c4613-0269-4267-bf45-84958f9e1679.png)
- ImageNet 데이터 셋 중 10개 클래스를 완전히 다른 데이터셋으로 대체
- CoCoOp mostly outperforms CoOp by a clear margin.


