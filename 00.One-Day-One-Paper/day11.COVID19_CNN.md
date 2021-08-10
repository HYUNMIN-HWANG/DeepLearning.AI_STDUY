# Deep Learning COVID-19 Features on CXR using Limited Training Data Sets
- https://ieeexplore.ieee.org/document/9090149
- IEEE Transactions on Medical Imaging ( Volume: 39, Issue: 8, Aug. 2020)

---

## Abstract
we propose a patch-based convolutional neural network approach with a relatively small number of trainable parameters for COVID-19 diagnosis.

## I. INTRODUCTION
현재 문제점
- RT-PCR results using nasopharyngeal and throat swabs can be affected by sampling errors and low viral load
- Since most COVID-19 infected patients were diagnosed with pneumonia, radiological examinations may be useful for diagnosis and assessment of disease progress
- the routine use of CT places a huge burden on radiology departments and potential infection of the CT suites
in this paper,
- we aim to further investigate deep convolutional neural network and evaluate its feasibility for COVID-19 diagnosis.
- to develop a neural network architecture that is suitable for training with limited training data set,
- COVID-19 in CXR 특징 : bilateral involvement, peripheral distribution and ground-glass opacification
- there are statistically significant differences in the patch-wise intensity distribution >> novel patch-based deep neural network architecture with random patch cropping
- novel probabilistic Grad-CAM : takes into account of patch-wise disease probability in generating global saliency map.

## II. PROPOSED NETWORK ARCHITECTURE
- CXR images are first pre-processed for data normalization
- 1. segmentation network (lung areas can be extracted)
- 2. decision is made based on the majority voting
- 3. probabilistic Grad-CAM saliency map is calculated to provide an interpretable result.

### A. Segmentation network
- Our segmentation network aims to extract lung and heart contour from the chest radiography images.
- fully convolutional (FC)-DenseNet103 to perform semantic segmentation
- L(1) is the cross entropy loss of multi-categorical semantic segmentation
- softmax probability
- s {background, heart, left lung, right lung}

- universal preprocessing step (data normalization)
> - Data type casting (from uint8/uint16 to float32)
> - Histogram equalization (gray level = [0, 255.0])
> - Gamma correction ( = 0.5)
> - Image resize (height, width = [256, 256])

- hyperparameter
> - Adam optimizer
> - learning rate of 0.0001
> - early stopping strategy based on validation performance
> - Batch size was optimized to 2

### B. Classification network
- ResNet-18 as the backbone 을 사용한 이유
> - The first is to prevent from overfitting
> - Secondly, we intended to do transfer learning with pre-trained weights from ImageNet to compensate for the small training data set.
- The labels were divided into four classes: normal, bacterial pneumonia, tuberculosis (TB), and viral pneumonia(include COVID-19 infection + SARS-cov or MERS-cov)

- implemented in two different versions
> 1. global approach
> > - the masked images were resized to 224x224
> > - global appearance of the CXR data
> 2. local approach
> > - our proposed method
> > - the masked images were cropped randomly with a size of 224x224
> > - various CXR images are resized to a much bigger 1024x1024 image for our classification network to reflect the original pixel distribution better
> > - the centers of patches were randomly selected within the lung areas (비어 있는 곳을 crop 하는 걸 방지하기 위해서)

> > - K-number of patches were randomly acquired for each image to represent the entire attribute of the whole image.
> > - K network output the final decision was made based on majority voting
> > - the number of random patches K was set to 100, which means that 100 patches were generated randomly from one whole image for majority voting.

- ImageNet are used for network weight initialization
- Adam optimizer
- learning rate of 0.00001
- 100 epochs
- early stopping
- The batch size of 16
- weight decay
- L1 regularization to prevent overfitting problem

### C. Probabilistic Grad-CAM saliency map visualization
gradient weighted class activation map (Grad-CAM)
- each patch has different score for the COVID-19 class
- to obtain the global saliency map, patch-wise Grad-CAM saliency maps should be weighted with the estimated probability of the class, and their average value should be computed.

## III. METHOD
### A. Dataset
1) Segmentation network dataset: 
- JSRT dataset, SCR database > training (80%) and validation (20%)  
- USNLM dataset, MC dataset > validation
2) Classification dataset
- to avoid the network from learning biased features from age-related characteristics, we excluded pediatric CXR images.
- Total dataset was curated into five classes; normal, tuberculosis, bacterial pneumoia, viral pneumonia, COVID-19 pneumonia.
- The combined dataset were randomly split into train, validation, and test sets with the ratio of 0.7, 0.1, and 0.2.
3) Dataset for comparison with COVID-Net:
- We prepared a separate dataset to compare our method with existing state of-the art (SOTA) algorithm called COVID-Net
- labels were divided into only three categories including normal, pneumonia, and COVID-19

### B. Statistical Analysis of Potential CXR COVID-19 markers
standard biomarkers from CXR image analysis are investigated.
- Lung morphology, Mean lung intensity, Standard deviation of lung intensity, Cardiothoracic Ratio (CTR), 

### C. Classification performance metrics
- F1 score was used as the evaluation metric for early stopping

## IV. EXPERIMENTAL RESULTS
### A. Segmentation performance on cross-database
- Segmentation performance of anatomical structure was evaluated using Jaccard similarity coefficient
- our universal preprocessing step for data normalization contributes to the processing of cross-database with statistically significant improvement on segmentation accuracy (Jaccard similarity coefficients from 0.932 to 0.943, p < 0.001)

### B. Morphological analysis of lung area
- In normal and tuberculosis cases (the first and the second row of Fig. 3, respectively), overall lung and heart contour were wellsegmented.
- In the bacterial case, however, the segmented lung area was deformed due to wide spread opacity of bacterial pneumonia
- This suggests that abnormal morphology of the segmentation masks may be a useful biomarker to differentiate the severe infections.
- In overall cases of the viral and the COVID-19 classes, lung areas were either normally or partiallyimcompletely segmented

### C. Statistical significancy of potential COVID-19 bio-markers
intensity-related COVID-19 arker candidates were extracted and compared.
1) Lung areas intensity
- COVID-19 cases showed lower mean intensity compared to other cases with statistical significance level (p <0.001 for normal and bacterial, p <0.01 for TB).

2) Lung areas intensity variance
- For both the COVID-19 and the viral cases, the variance values were higher than other classes with statistical significance (p <0.001 for all).
- To investigate the effect of scanning protocol on statistics, we performed additional study by excluding AP Supine radiographs from entire dataset with documented patient information.

3) Cardiothoracic ratio
- Despite there exist statistical differences between the COVID-19 cases to other classes (p <0.001 for normal and TB, p <0.05 for Bacteria), the scatter plot showed broad overlap between several classes.                

*결론 : we found that intensity distribution pattern within the lung area may be most effective in the diagnosis, which highly reflects the reported chest X-ray (CXR) appearances of COVID-19*
- the locally concentrated multiple opacities can cause uneven intensity distribution throughout entire lung area
- different texture distribution within CXR may cause the similar intensity variations.
- From these intra- and inter-patch intensity distribution results, we can infer that intra-patch variance, which represents local texture information, was not crucially informative, 
- whereas the globally distributed multi-focal intensity change may be an important discriminating feature for COVID-19 diagnosis, which is strongly correlated with the radiological findings.
- Therefore, in the classification network, the COVID-19 and viral classes were integrated into one class.
 
### D. Classification performance 
- The proposed local patch-based approach showed consistently better performance than global approach in all metrics.
- our method showed the sensitivity of 92:5% for COVID-19 and viruses

### E. Interpretability using saliency map
- probabilistic Grad-CAM, multifocal GGOs(ground-glass opacification) and consolidations were visualized effectively by our local patch-based approach
- probabilistic Grad-CAM saliency map from our local patch-based approach is more intuitive and interpretable compared to the existing methods.

## V. DISCUSSION
### A. COVID-19 Features on CXR
the globally distributed localized intensity variation is a discriminatory factor for COVID-19 CXR images

### B. Feasibility as a ‘triage’ for COVID-19
our neural network is trained to classify other viral and COVID-19 in the same class. by excluding normal, bacterial pneumonia, and TB at the early stage, we can use RT-PCR or CT for only those patients classified as other virus and COVID-19 cases for final diagnosis.

### C. Training stability
Still, thanks to the increasing training data set from the random patch cropping across all image area, our local patch-based algorithm did not showed any sign of overfitting even with the small numbers of training data,

### D. Comparison with COVID-Net
our method showed overall accuracy of 91.9 % which is comparable to that of 92.4 % for COVID-Net
In addition, it is also remarkable that our method uses only about 10% number of parameters (11.6 M) compared to that of COVID-Net (116.6 M)

### E. Cross-database generalization capability
We are aware that the current study has limitations due to the lack of well-curated pneumonia CXR dataset
original COVID-19 data could be well preprocessed to have comparable intensity distribution to that of well-curated normal data.

### F. Segmentation network analysis
1) Comparison with U-Net : FC-Densenet103 vs U-Net > no significant difference 
2) Effect of trainset size  : segmentation performance decreased steeply as the size of trainsets decreased.
3) Segmentation effects on marker analysis and classification : 

### G. Classification network analysis

## VI. CONCLUSION

---
---
---
# Deep Learning COVID-19 Features on CXR using Limited Training Data Sets
- https://ieeexplore.ieee.org/document/9090149
- IEEE Transactions on Medical Imaging ( Volume: 39, Issue: 8, Aug. 2020)

---

## Summary
COVID-19 진단할 수 있으면서 상대적으로 적은 parameter수로 구성된 patch-based convolutional neural network 모델을 제안했다.
(we propose a patch-based convolutional neural network approach with a relatively small number of trainable parameters for COVID-19 diagnosis.)

![image](https://user-images.githubusercontent.com/70581043/128879995-13d0cc85-53ae-4378-8e3a-978586b48906.png)
과정은 크게 3 부분으로 나뉜다.
1. segmentation network (lung areas can be extracted)
2. decision is made based on the majority voting
3. probabilistic Grad-CAM saliency map is calculated to provide an interpretable result.

###  1. segmentation network
- chest radiography images로 부터 폐와 심장 가장자리를 추출하는 작업
- (FC)-DenseNet103
- cross entropy loss of multi-categorical semantic segmentation
- softmax probability

### 2. Classification network
- ResNet-18
- four classes: normal, bacterial pneumonia, tuberculosis (TB), and viral pneumonia( COVID-19 infection + SARS-cov or MERS-cov)
- implemented in two different versions
1. global approach (전체 그림을 한 번에 mask 하는 듯)
> - the masked images were resized to 224x224
> - global appearance of the CXR data
2. local approach (전체 그림을 랜덤하게 K번 mask 하는 듯) -> 해당 논문에서 제안하고자 하는 바
> - our proposed method
> - the masked images were cropped randomly with a size of 224x224

### 3. Grad-CAM saliency map visualization
- gradient weighted class activation map (Grad-CAM) _⛳ Grad-CAM이 뭐지??_
- to obtain the global saliency map, patch-wise Grad-CAM saliency maps should be weighted with the estimated probability of the class, and their average value should be computed

## RESULTS
1. segmentation
![image](https://user-images.githubusercontent.com/70581043/128881205-c0f46f3f-78fd-4a7d-9a0c-69ea412c8851.png)
- Jaccard similarity coefficient로 segmentaion 평가함
- 해당 논문에서 제안한 대로 전처리 했을 때 가장 높은 acc를 보였다.
![image](https://user-images.githubusercontent.com/70581043/128881402-633d23c0-4398-47ef-944b-476591e1913a.png)
segmentation 한 결과는 위 사진과 같다.

2. COVID-19 bio-markers
COVID-19 진단하는 결정적인 특징 : intensity distribution pattern within the lung area may be most effective in the diagnosis

3. Classification
![image](https://user-images.githubusercontent.com/70581043/128882031-7a627e3c-2394-4ec9-b8e1-f2c89891140c.png)
논문 모델 sensitivity of 92.5% for COVID-19 and viruses

4. Grad-CAM
![image](https://user-images.githubusercontent.com/70581043/128882154-02ab7751-257c-4253-8384-2e881ed8c971.png)
global approach로 분석하면 감염된 특정 부위가 아닌 넓은 부위로 인식한다. 반면, our local patch-based approach is more intuitive and interpretable compared to the existing methods.