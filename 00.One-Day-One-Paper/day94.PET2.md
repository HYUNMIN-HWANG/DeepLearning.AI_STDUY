# It’s Not Just Size That Matters : Small Language Models Are Also Few-Shot Learners

Exploiting Cloze Questions for Few Shot Text Classification and Natural Language Inference (#180) 와 동일한 저자이며, PET를 좀 더 변형시켜 성능을 올렸다. PET와 차이점은 MASK를 여러 개로 설정할 수 있다는 점


 ### PET with Multiple Masks
![image](https://user-images.githubusercontent.com/70581043/168802246-982a304f-3679-4e93-bbdb-04f61601c68a.png)
- PET의 한계 : the verbalizer _v_ must map each output to a single token
- 예를 들어서, "terrible" 단어가 주어져있을 때 해당 단어를 "terri"와 "ble" 두 개의 tokens로 쪼갤 수 있다.
- 쪼개진 token 수 만큼 k 번의 prediction을 수행한다. : Starting from P^k(X), perform k consecutive predictions,         
#### inference     
![image](https://user-images.githubusercontent.com/70581043/168803156-217d3645-24f4-4115-8771-2a0b740a8ef4.png)            
- 여기서 j는 ![image](https://user-images.githubusercontent.com/70581043/168803220-37393bef-a7a8-45cd-b84e-62ad791baaaa.png) q_M 중에서 가장 큰 값. 따라서 j 위치에 있는 토큰과 그 이외의 토큰들을 k번에 걸쳐 계속 곱해나간다.
#### training
- approximate q_p(y|x)               
![image](https://user-images.githubusercontent.com/70581043/168804203-fedcd58f-5c19-49b6-8ea5-24f4be2d3d85.png)
- 특징 : 합쳐서 1이 되지 않기 때문에 cross entropy를 사용할 수 없다. 대신 multi-class hinge loss를 사용해서 이를 minimize 시킨다 : ![image](https://user-images.githubusercontent.com/70581043/168803619-63719303-e198-4168-a232-ec813e88ad0b.png)


### Experiments
- 지표 : SuperGLUE
- backbone : ALBERT

### Results
![image](https://user-images.githubusercontent.com/70581043/168804506-f3c2c074-cc2e-4aff-8e08-489bb1513a1d.png)
- 많은 데이터셋에서 PET가 GPT 보다 더 좋은 성능을 보였고, 파라미터 수가 확연히 줄어들었다.
- iPET가 PET보다 3가지 tasks 에서 더 좋은 성능을 보임

