# Clinical-BERT: Vision-Language Pre-Training for Radiograph Diagnosis and Reports Generation



Medical domain에 VLP를 적용시키기 어렵다. natural image와 text 같은 경우 대강 의미가 유사한 단어를 쓰더라고 상관없지만 medical data같은 경우 정확한 단어로 설명해야 하기 때문이다. 즉 MeSH (Medical Subject Headings) 단어를 사용해야 한다.

![image](https://user-images.githubusercontent.com/70581043/167625408-c794f333-2cb6-49c4-b0a0-220cbfc96391.png)

해당 논문에서는 1가지 pre training 방법과 3가지 down stream tasks를 제안했다.
1. Clinical Diagnosis (CD)
   - multi-label classification problem
   - 여기서는 14가지의 질병을 4가지 태그(positive, negative, uncertain, abscent)로 분류함
   ![image](https://user-images.githubusercontent.com/70581043/167626060-d9f61e35-1368-44a7-abf8-fedfe422b20d.png)

2. Masked MeSH Modeling (MMM)
    - focus on the prediction of MeSH words
    - 80%는 [MASK] token, 10%는 [MeSH] word, 10%는 remaining unchanged
    ![image](https://user-images.githubusercontent.com/70581043/167626419-2eff61c1-bf16-42eb-953b-597e631638c7.png)

3. Image-MeSH Matching (IMM)
    - aligns the images and MeSH words
    - 방법 2가지 제안 
       1) RSA : Region sparse attention - algin region features for each word
       2) WSA : word sparse attention - MeSH 단어에 영향력을 키운다.
![image](https://user-images.githubusercontent.com/70581043/167626719-e59be2f7-7e4e-47e6-9141-a1bd8dbe9c4d.png)

4. Masked Language Model (MLM)
    - 15% 의 단어 토큰을 [MASK], random token, original token으로 대체한다.
    - bidirectional prediction (bi) 
    - sequence to sequence prediction (s2s)
    ![image](https://user-images.githubusercontent.com/70581043/167626993-f8e10a26-7244-4333-8050-fcab5fe388d0.png)



The overall pre-training loss is:
![image](https://user-images.githubusercontent.com/70581043/167627139-aaf4a15e-9282-49ba-a72a-1cd2cecc4b0d.png)
