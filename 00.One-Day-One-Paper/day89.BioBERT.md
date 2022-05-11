# BioBERT: a pre-trained biomedical language representation model for biomedical text mining

BERT가 NLP task에 좋은 성능을 보였지만, medical text애 대해서는 좋은 성능을 보여주지 못했다. 해당 논문에서는 medical text를 pre-training한 BioBERT 모델을 제안했다. 

![image](https://user-images.githubusercontent.com/70581043/167777234-2b26cc85-22b6-46b9-a18b-fdd6c3137081.png)
- introduced pre-trained language model BERT can be adapted for biomedical corpora
1. **initialize BioBERT** with weights from BERT, which was pretrained on general domain corpora (English Wikipedia and BooksCorpus)
2. BioBERT is **pre-trained** on biomedical domain corpora (PubMed abstracts and PMC full-text articles)
![image](https://user-images.githubusercontent.com/70581043/167777845-02009000-aa08-4fe0-9413-2fe87c03a04b.png)
    - tokenization : BioBERT uses WordPiece tokenization
    - used the original vocabulary of BERT_BASE
4. BioBERT is **fine-tuned** and evaluated on three popular biomedical text mining tasks (NER, RE and QA) 
    -  NER (Named entity recognition) : recognizing numerous domain-specific proper nouns in a biomedical corpus
    - RE (Relation extraction) : classifying relations of named entities in a biomedical corpus.
    - QA (Question answering) : answering questions posed in natural language given related passages