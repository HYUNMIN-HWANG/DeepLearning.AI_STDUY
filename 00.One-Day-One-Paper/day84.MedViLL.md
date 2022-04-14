# Multi-modal Understanding and Generation for Medical Images and Text via Vision-Language Pre-Training (MedViLL)

VLP를 메디컬 이미지-텍스트 데이터에 적용시켜 다양한 테스크를 수행할 수 있는 모델을 제안한다.           
- specifically using radiology images and the unstructured report
- Transformer based architecture combined with a novel multimodal attention masking scheme for both vision-language understanding task (e.g., diagnosis classification) and vision-language generation task (e.g., radiology report generation).
- Diagnosis Classification, Medical Image-Report Retrieval, Medical Visual Question Answering, Radiology Report Generation 4가지 task를 모두 수행할 수 있다.

![image](https://user-images.githubusercontent.com/70581043/163338579-77b56259-87cd-4086-956c-e9b7b1543609.png)
### Dataset
- MIMIC-CXR & Open-I
- anteroposterior frontal view chest X ray 이미지만 사용함
- pre-processnig : cut out the marginal space of the original image and resize all the images to 512 x 512, keeping the aspect ratio. Then for the report, we select a longer description (Findings or Impression section) which may contain detailed information associated to the X-ray imaging

### VL Pre-training Model
1. visual feature embedding (A): 
![image](https://user-images.githubusercontent.com/70581043/163339027-73f9d725-fa64-4a52-893e-fdfce5f98575.png)
- CNN to extract visual features from the images
- v_i : visual feature obtained from the last CNN layer
- l_i : location feature
- s_V : semantic embedding vector

2. Language Feature Embedding (B) : 
![image](https://user-images.githubusercontent.com/70581043/163339187-30600df4-9b86-4d96-8d5d-d93ddddec2a6.png)
- BERT에 따라서 encode textual information
- w_i : token are converted to vector representation
- p_i : position embeddings
- s_L : semantic embedding vector

3. Joint Embedding : 
- visual embedding & language embedding

4. Pre-training ohjectives : 
- MLM : ![image](https://user-images.githubusercontent.com/70581043/163339660-a2a08699-2ca5-4439-b2b0-b16600303988.png)
- ITM : ![image](https://user-images.githubusercontent.com/70581043/163339698-520bcc06-909e-4272-b4d6-2fc08c6f78a7.png)

### Self-Attention Mask Schemes
![image](https://user-images.githubusercontent.com/70581043/163339800-339f4a32-53c5-4f96-a67f-78a10dbf9bfc.png)
(a)와 (d)를 혼합시키는 새로운 maks 방법을 제안함 (b) Bidirectional Auto-regressive (BAR)


