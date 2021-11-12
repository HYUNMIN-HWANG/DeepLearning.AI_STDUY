# Attention Is All You Need
- https://arxiv.org/abs/1706.03762
- 2017 - papers.nips.cc
---
## Transfoermer
기존 sequence modeling and transduction problems 으로 사용되었던 RNN, LSTM, Conv layer와 다른 새로운 모델을 제안했다 . 기존의 모델들은 sequence의 길이가 길어지면, computation cost가 증가함. 
![image](https://user-images.githubusercontent.com/70581043/141444766-a8315680-3f28-4752-a8fd-ab602d846eef.png)
전체적인 모델 구조 특징
- encoder - decoder를 사용
- 각 sub-layers에 Multi-head self-attention mechanism 사용함
- Residual connection around each of sub-layers, followed by layer normalization.
- Embeddings : Learned embeddings to convert the input tokens and output tokens to vectors of dimension
- Linear transform + Softmax
- Positional Encoding : 위치를 나타내는 정보가 없기 때문에 추가함

### Result
![image](https://user-images.githubusercontent.com/70581043/141445474-ef97a6c4-2223-4f20-8832-baa423bf2261.png)
BLEU 점수를 봤을 때, Transformer 모델일 때 꽤 좋은 성능을 보여주었다. 