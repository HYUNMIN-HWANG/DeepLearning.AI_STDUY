# Automatic Liver and Lesion Segmentation in CT Using Cascaded Fully Convolutional Neural Networks and 3D Conditional Random Fields

- https://arxiv.org/abs/1610.02177
- [Submitted on 7 Oct 2016]
- MICCAI 2016

---

## Summary

①간과 그 외의 기관을 segmentation 한 후, ②간에서 lesion이 있는 부분을 segmentation 하는 작업을 동시에 실행하는 모델을 제안했다. 

![image](https://user-images.githubusercontent.com/70581043/129336050-82b1f0b8-9ce9-4d1a-b95a-c7f89eda2ec8.png)
전체적인 과정 
1. CT data를 HU Windowing, Histogram Equalization, augmentation(translation, rotation and addition of gaussian noise) 전처리 과정을 거친다. 
2. CFCN 모델을 통해서 segment the liver & segment the lesions을 진행한다. (이 논문에서 CFCN는 U-NET 을 기반함)
3. 3DCRF를 통해서 라벨링을 예측한다.

## Result
- Qualitative results
![image](https://user-images.githubusercontent.com/70581043/129337812-02b712eb-7391-4595-a11f-d9f69a6b4e1e.png)
CFCN을 했을 때 UNET(=Single FCN)일 때 보다 lesion을 잘못 예측한 지역이 줄어들었다. 3DCRF를 사용했을 때 Dice 점수가 향상되었다.

- Quantitative results
![image](https://user-images.githubusercontent.com/70581043/129337554-3f50bbf8-e1f0-4582-9058-72b5c7e1c7b0.png)
CFCN을 했을 때 Single FCN일 때 보다 점수가 향상, 3DCRF를 사용했을 때 점수가 더 향상되었다.