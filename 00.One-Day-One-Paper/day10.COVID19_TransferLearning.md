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

