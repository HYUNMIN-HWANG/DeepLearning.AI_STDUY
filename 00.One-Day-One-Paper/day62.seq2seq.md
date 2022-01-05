# Sequence to Sequence Learning with Neural Networks
- https://arxiv.org/abs/1409.3215
- NIPS 2014
---
## 기존 DNN (Deep Neural Network)의 한계점
- input 와 targets이 같은 dimentionality여야지 encode를 할 수 있었다.
- 이 길이를 모르면 많은 task를 수행하기 어려웠음

## Seq2seq의 특징
- 2 종류의 LSTM을 사용 : 
    - 하나는 input sequence를 읽고 _고정된 차원의 vector_를 얻는다 
    - 다른 하나는 vector로 부터 output sequence를 출력한다.
- source  sentence의 순서를 역전시킴으로써 긴 문장도 잘 훈련이 되는 효과를 얻었다
    - 원래 LSTM은 긴 문장을 훈련시키는 데 어려움이 있었으나, reverse 시킴으로써 이 한계가 극복되었다.
    - source sequence에서 앞쪽에 있는 단어들이 target sequence에서 연관 있는 단어들과의 거리가 좁혀지기 때문에
 -  deep LSTM(4 layers)이 얕은 LSTM보다 더 좋은 성능을 보였다.
 - 각 층마다 1000 cell, 1000 dimensional word embedding을 사용함
 - input vocabulary 160,000개, output vocabulary는 80,000개

## Experiment
- WMT'14 English to French translation task
- Decoding
    ![image](https://user-images.githubusercontent.com/70581043/148211808-f0a95fb0-ef35-4261-9e14-7049294e27ff.png)        
    - maximizing the log probability of a correct translation T given the source sentence S
   
    ![image](https://user-images.githubusercontent.com/70581043/148212029-9c2d1c01-8c0a-416d-9608-d8d038d22582.png)     
    - produce translations by finding the most likely translation according to the LSTM
- Results
   ![image](https://user-images.githubusercontent.com/70581043/148212320-37195c0d-063e-4efd-a365-3743e5f88449.png)     
   - BLEU score 34.81
   - 다른 Neural Network 보다 좋은 성능을 보여줌 

   
