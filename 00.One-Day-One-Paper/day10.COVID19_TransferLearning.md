# Deep-COVID: Predicting COVID-19 from chest X-ray images using deep transfer learning
- https://www.sciencedirect.com/science/article/abs/pii/S1361841520301584?via%3Dihub
- code https://github.com/shervinmin/DeepCovid
- [Submitted on 20 Apr 2020 (v1), last revised 21 Jul 2020 (this version, v3)]
- Medical Image Analysis

---

## Abstract

- One of the crucial step in fighting COVID-19 is the ability to detect the infected patients early enough, and put them under special care. Detecting this disease from radiography and radiology images is perhaps one of the fastest ways to diagnose the patients.
- ResNet18, ResNet50, SqueezeNet, and DenseNet-121, to identify COVID-19 disease in the analyzed chest X-ray images

## 1. Introduction

- Due to unavailability of therapeutic treatment or vaccine for novel COVID-19 disease, early diagnosis is of real importance to provide the opportunity of immediate isolation of the suspected person and to decrease the chance of infection to healthy population.
- Chest CT has a high sensitivity for diagnosis of COVID-19 ( Ai et al., 2020 ) and X-ray images show visual in- dexes correlated with COVID-19 ( Kanne et al., 2020 ).
- The reports of chest imaging demonstrated multilobar involvement and periph- eral airspace opacities.
- The com- bined dataset has around 50 0 0 Chest X-ray images (called COVID- Xray-5k), which is divided into 20 0 0 training, and 30 0 0 testing samples.
- Unlike the classical approaches for medical image classification which follow a two-step procedure (hand-crafted feature extraction+recognition), we use an end-to-end deep learning framework which directly predicts the COVID- 19 disease from raw images without any need of feature extraction.
- ResNet18, ResNet50, SqueezeNet, and DenseNet-161
- Two strategies were adopted to address the COVID-19 image scarcity issue in this work: (코로나 사진이 너무 적다는 문제를 해결하기 위해서)
> - data augmentation : flipping, small rotation, adding small amount of distortions
> - we fine-tune the last layer of the pre-trained version of these models on Ima- geNet.
- calculate the confidence interval of the performance metrics
> - Receiver operating characteristic (ROC) curve
> - area under the curve (AUC)

## 2. COVID-Xray-5k Ddataset
COVID-Xray- 5k dataset that contains 2084 training and 3100 test images.
- Covid- Chestxray-Dataset : a mix of chest X-ray and CT images. only anterior-posterior images > 100 COVID-19 images to include in the test set (to meet some max- imum confidence interval value), and 84 COVID-19 images for the training set. > Data augmentation is applied to the training set to in- crease the number of COVID-19 samples to 420 as described above
- ChexPert dataset : 2000 non-COVID images.

## 3. The proposed framework
### 3.1. Transfer learning approach
Transfer learning is mainly useful for tasks where enough training samples are not available to train a model from scratch, such as medical image classification for rare or emerging diseases.
There are two main ways in which the pre-trained model is used for a different task.
1. the pre-trained model is treated as a feature extractor(i.e., the internal weights of the pre-trained model are not adapted to the new task),
2. the whole network, or a subset thereof, is fine-tuned on the new task.
- we only fine-tune the last layer of the con- volutional neural networks, and essentially use the pre-trained models as a feature extractor.

### 3.2. COVID-19 Detection using residual ConvNet –ResNet18 and ResNet50
- 'identity shortcut connection' that skips one or more layers

### 3.3. COVID-19 Detection using SqueezeNet
- light-weight models 
- They alternate a 1 ×1 layer that “squeezes”the incoming data in the vertical dimension followed by two parallel 1 ×1 and 3 ×3 convolutional layers that “expand”the depth of the data again.

### 3.4. COVID-19 Detection using DenseNet
- each layer obtains additional inputs from all preceding layers and passes on its own feature- maps to all subsequent layers.
- Since each layer receives feature maps from all preceding layers, network can be thinner and compact, i.e., number of channels can be fewer

### 3.5. Model training
All employed models are trained with a cross-entropy loss function.
which tries to minimize the distance between the predicted probability scores, and the ground truth probabilities

## 4. Experimental results
### 4.1. Model hyper-parameters
- 100 epochs.
- batch size is set to 20
- ADAM optimizer
- learning rate of 0.0001
- All image 224 ×224

### 4.2. Evaluation metrics
sensitivity and specificity

### 4.3. Model predicted scores
An ideal model should predict the probability of all COVID-19 samples close to 1, and non-COVID samples close to 0.
predicted scores for three classes: COVID-19, Non-COVID normal, and Non-COVID other diseases.
As we can see the Non-Covid images with other disease types have slightly larger scores than the Non-COVID normal cases.
COVID-19 patient images are predicted to have much higher probabilities than the Non-COVID images,

### 4.4. Model sensitivity and specificity
sensitivity and specificity rates for dif- ferent thresholds, using ResNet18, ResNet50, SqueezeNet, and DenseNet-121 models, respectively.
the best performing model obtains a sensitivity rate of 98% and specificity rate of 92.9%. SqueezeNet and ResNet18 achieve slightly better performance than the other models.

### 4.5. Small number of COVID-19 cases and model reliability
The confidence interval of the accuracy rates
z : confidence interval (the number of standard deviation of the Gaussian distribution),

### 4.6. The ROC curve, precision recall curve, and confusion matrix
- precision- recall curve
> - Precision : defined as the true positive images divided by the total number of images flagged as positive by the model
> - recall : the same as sensitivity rate
- Receiver operating characteristic (ROC) curve,
> - which provides the true positive rate as a function of false positive rate
> - SqueezeNet achieving a slightly higher AUC than the other models.

### 4.7. The heatmap of potentially infected regions
Once we repeat this procedure for different slid- ing windows of N ×N , each time shifting them with a stride of S ,

## 5.Conclusion
For a sensitivity rate of 98%, these models achieved a specificity rate of around 90% on average.
However, due to the limited number of COVID-19 images publicly available so far, further experiments are needed on a larger set of cleanly labeled COVID-19 images for a more reliable estimation of the accuracy of these models.

---
---
---

# Deep-COVID: Predicting COVID-19 from chest X-ray images using deep transfer learning
- https://www.sciencedirect.com/science/article/abs/pii/S1361841520301584?via%3Dihub
- code https://github.com/shervinmin/DeepCovid
- [Submitted on 20 Apr 2020 (v1), last revised 21 Jul 2020 (this version, v3)]
- Medical Image Analysis

---

## Summary
ResNet18, ResNet50, SqueezeNet, and DenseNet-121 4가지 모델로 chest X-ray을 학습시켜 COVID-19 를 예측했다.

- dataset(COVID-Xray-5k dataset) : 
![image](https://user-images.githubusercontent.com/70581043/128684786-69312608-dd9d-47e8-815e-c8d3dbd5e46e.png)
COVID-Xray 이미지가 다른 Xray 보다 데이터의 수가 훨씬 적기 때문에 data augmentation과 pre-trained 모델을 활용했다.
- Transfer learning : 이미지 특징을 추출하기 위해서 pre-trained models을 사용했고, 마지막 layer를 fine tuning 했다.
1. ResNet18 and ResNet50
![image](https://user-images.githubusercontent.com/70581043/128685224-77fea539-5636-47b0-84e3-bad348728958.png)
> - ImageNet dataset 으로 훈련이 되어 있음
> - identity shortcut connection : 한 개 이상의 layer를 skip함으로써  이 전의 layer에 직접적인 경로를 제공해줌
> - ResNet50 은 ResNet18보다 층 수가 더 많다.

2. SqueezeNet
![image](https://user-images.githubusercontent.com/70581043/128685253-b2250242-2cde-450e-8f82-8b29d9cfc42b.png)
> - light-weight models
> - “squeezes”(1X1 layer)와 “expand” (1×1 and 3 ×3 layer)를 번갈아 사용

3. DenseNet
![image](https://user-images.githubusercontent.com/70581043/128685270-362a0dbb-ab91-4a29-9a01-57bfce1787fc.png)
> - 모든 레이어들은 이전 레이어들로부터 인풋을 받고, 각 feature map이 그 다음 레이어에 전달된다.

## Train
- Model hyper-parameters
> - 100 epochs.
> - batch size is set to 20
> - ADAM optimizer
> - learning rate of 0.0001
> - All image 224 ×224

- Evaluation metrics
![image](https://user-images.githubusercontent.com/70581043/128686742-661359fb-816a-4062-86f6-2bc246fbc9e2.png)
![image](https://user-images.githubusercontent.com/70581043/128687031-a42d3954-145c-4e00-adc3-0857f7b0c1e6.png)
신뢰구간은 95% (z=1.96)을 사용함
 
- Receiver operating characteristic (ROC) curve,
![image](https://user-images.githubusercontent.com/70581043/128688473-7ec895f7-a1ec-4b64-be58-ef0f6be27367.png)
4개 모델 모두 거의 비슷함 (SqueezeNet이 조금은 성능 좋음)

- heatmap
![image](https://user-images.githubusercontent.com/70581043/128691695-931081cc-1eb5-4aa0-a7ba-30e6f6587b4a.png)
감염되어 있다고 예측되는 곳을 heatmap으로 표시함. 방사선 전문의가 표시한 지역과 거의 동일

---
실험이 너무 단순했다. (이미지 데이터 모아서 전이학습에 넣으면 끝) 단순했는데도 결과가 잘 나와서 놀라기도 했다.
ResNet18, ResNet50, SqueezeNet, and DenseNet-121 4가지 모델에 대해서 대략적으로만 알고 있는데 나중에 논문 읽으면서 공부해야겠다.