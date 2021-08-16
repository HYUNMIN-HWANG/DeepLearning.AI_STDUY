# A deep learning model integrating FCNNs and CRFs for brain tumor segmentation
- https://pubmed.ncbi.nlm.nih.gov/29040911/
- 2018 Jan
- Med Image Anal. 2018 Jan

---


## Summary
brain tumor segmentation를 하기 위해서 그동안 독립적으로 시행되었던 FCN과 CRF(RNN)를 합친다.

- 과정 : 
1. Pre-processing of the imaging data 
> - normalizes image intensity by subtracting the image mode (가장 높은 회색 값? histogram bin → white matter와 gray matter 간의 불연속성을 나타냄)
> - normalizing the standard deviation to be 1

2. FCNNs 
![image](https://user-images.githubusercontent.com/70581043/129564860-7ce789c5-2e9d-41cb-a77a-d101c171f214.png)
> - input 2 different sizes
> - 큰 사이즈의 input은 작은 사이즈의 input과 동일한 크기인 feature map이 된다.
> - 랜덤하게 같은 수만큼 axial view, coronal view or sagittal views slice로부터 특징을 추출한다. (imbalance 문제를 피할 수 있다.)
> - class : healthy tissue, necrosis, edema, non-enhancing core, and enhancing core
                                                                                         
3. CRF-RNN
> - fully connected CRFs를 사용해서 optimization 문제를 해결
> - Fully connected CRF는 라벨 u를 픽셀 I<sub>i </sub>에 할당할 확률을 예측
> - 역전파를 사용할 수 있다.

4. The integration of FCNNs and CRF-RNN.
> (1) training FCNNs using image patches
> (2) training CRF-RNN using image slices with parameters of FCNNs fixed
> (3) fine-tuning the whole network using image slices.

5. Fusing segmentation results obtained in axial, coronal and sagittal views
> - voting strategy를 사용해서 segmentation 결과를 합친다.

6. Post-processing
> - post-processing을 함으로써 성능을 더 높일 수 있었다.
> 1) super high intensities 지역을 분리시킨다.
> 2) intensities가 3보다 아래인 것들은 지운다.
> 3) ![image](https://user-images.githubusercontent.com/70581043/129571743-7bfe65b7-f792-43dc-abc7-1e40511032b2.png) 해당하는 것들은 지운다.
> 4) 비어있는 구멍을 necrosis로 채운다.
> 5) necrosis 영역이 잘못 표시된 것을 고친다. T1c threshold를 기준으로
> 6) non- enhancing 영역은 enhancing core 영역이 매우 작은 경우 부종으로 잘못 표시될 수 있다.
