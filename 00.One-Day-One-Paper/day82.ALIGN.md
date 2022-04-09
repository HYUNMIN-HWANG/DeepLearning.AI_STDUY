# ALIGN: Scaling Up Visual and Vision-Language Representation Learning With Noisy Text Supervision

![image](https://user-images.githubusercontent.com/70581043/162569853-be99e2b8-bf8f-46a6-8df1-307587ebb473.png)
- 이전 Vision-Language Representation의 가장 큰 문제점은 데이터 셋이 현저히 작다는 것, 해당 논문에서는 심플한 필터링만 사용하여 큰 image-text dataset을 만들고, 이를 dual encoder에 넣어 학습하고자 했다.

1. Large Nosisy dataset
   -  leverage a noisy dataset of over one billion image alt-text pairs, obtained without expensive filtering or post-processing steps in the Conceptual Captions dataset.
   - get a version of raw English alt-text data (image and alt-text pairs).
   - apply minimal frequency-based filtering (예, porn 이미지 삭제, 200 픽셀 모다 큰 이미지, ratio 3 보다 작은 거, 중복된 이미지 제거)
 
2. Dual encoder architecture 
   - image encoder : EfficientNet + global pooling
   - text encoder : BERT + CLS toekn + FC layer
   - optimized via normalized softmax loss
   - ![image](https://user-images.githubusercontent.com/70581043/162572213-01c41544-2c56-4bb7-a1e3-ee2203dff779.png)


3. Experiment
![image](https://user-images.githubusercontent.com/70581043/162572352-abf24f6f-c8db-4283-92a2-c49c10aecab0.png)
- Transferring to Image-Text Matching & Retrieval
    - ALIGN achieves SOTA results in all metrics of Flickr30K and MSCOCO benchmarks. (zero shot , fine tune 모두 성능 좋았음)
    
![image](https://user-images.githubusercontent.com/70581043/162572417-6a10f54c-0266-4d21-8ea9-14a2f7ea2355.png)
- Transferring to Visual Classification
    - directly feed the texts of classnames into the text encoder
    - Similar to CLIP, ALIGN shows great robustness on classification tasks with different image distributions.