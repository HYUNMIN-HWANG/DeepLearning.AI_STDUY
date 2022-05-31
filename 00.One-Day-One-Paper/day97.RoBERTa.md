# RoBERTa: A Robustly Optimized BERT Pretraining Approach

기존에 있는 BERT의 hyperparameter를 조정해서 성능을 올렸다. hyperparameter choices have significant impact on the final results. training procedure improves upon the published BERT results on both GLUE and SQuAD.
- RoBERTa : match or exceed the performance of all of the post-BERT methods
- modification한 것들
   - (1) training the model longer, with bigger batches, over more data; 
   - (2) removing the next sentence prediction objective; 
   - (3) training on longer sequences;
   - (4) dynamically changing the masking pattern applied to the training data
 - contributions 
    - (1) present a set of important BERT design choices and training strategies and introduce alternatives that lead to better downstream task performance; 
    - (2) We use a novel dataset, 
    - (3) masked language model pretraining is competitive with all other recently published methods

### Results
![image](https://user-images.githubusercontent.com/70581043/171093943-14cd1376-be44-49ff-9f83-0c8942e274d3.png)
- our experiment는 static masking perform 보다 dynamic masking일 때 더 좋은 성능을 보인다.
![image](https://user-images.githubusercontent.com/70581043/171094058-f1101c0d-ef4e-4018-8a14-60439bf2f0e5.png)
- Next Sentence Prediction (NSP) loss : 다음 문장이 같은 document에 있는 문장인지 예측
- NSP loss를 없앴을 때 좀 더 좋은 성능을 보였다.
- single document (DOC-SENTENCES) : performs slightly better than packing sequences from multiple documents (FULL-SENTENCES)
![image](https://user-images.githubusercontent.com/70581043/171094943-9443bcfc-cf9e-43ef-9fd0-dd828b7c0fc3.png)
- batch size가 커질 수록 성능이 좋아졌음
#### Text Encoding
- subword units으로 unicode characters가 아닌 bytes(BPE)를 사용함
