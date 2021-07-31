# Data augmentation using generative adversarial networks (CycleGAN) to improve generalizability in CT segmentation tasks
- https://www.nature.com/articles/s41598-019-52737-x
- Published: 15 November 2019
- Scientific Reports

---

## Abstract
의료 데이터의 문제 : Labeled medical imaging data is scarce and expensive to generate.
논문 제안 : We evaluate the use of CycleGAN for data augmentation in CT segmentation tasks. Using a large image database we trained a CycleGAN to transform contrast CT images into noncontrast images. We then used the trained CycleGAN to augment our training using these synthetic non-contrast images.
결과 : We show that in several CT segmentation tasks performance is improved significantly, especially in out-of-distribution (noncontrast CT) data.

## Intro
- CNN모델 혹은 머신러닝 모델들이 좋은 결과를 얻기 위해서는 많은 데이터가 필요하다. 하지만, Labeling medical image data is a very expensive and time-consuming task.
- we generate a synthetic non-contrast version of training data contrast CTs. We then train on the original data while using the synthetic non-contrast CTs for data augmentation.
- using Cycle-GAN
- 하지만, 실제 이미지가 아니기 때문에 아직 실제 의료 현장에서는 쓰일 수 없음

## Results
### Synthetic non-contrast CT - qualitative evaluation
- One concern in regard to CycleGAN based contrast to non-contrast transformation is that unusual pathology on the images might not be correctly transformed. (질병이 있는 경우, 제대로 이미지 변환을 해주기도 하지만, 잘 못할 때도 있음)
- In summary, the synthetic non-contrast images appear in most cases to be plausible on quick examination. It should be noted that an experienced radiologist would have no problem discriminating between synthetic non-contrast CT images and actual non-contrast CT images on full resolution images but this may be difficult and take longer on scaled-down images.

### Segmentation results
- In-distribution performance (contrast CT) : 0.89 to 0.94, CycleGAN augmented results were slightly improved
- Out-of-distribution performance (non-contrast CT) : 0.06, 0.09 and 0.07, When using
CycleGAN augmentation a dramatic increase of the Dice score

### Volume measurement error results
- in-distribution volume measurement : CycleGAN augmented segmentations were excellent for kidney and liver (3% and 4%, respectively) and reasonable for spleen (8%)
- non-contrast data : CycleGAN augmentation showed the lowest volume estimation errors

### Example images

### Discussion
- 가설 : We hypothesized that by performing data augmentation using generative adversarial networks segmentation performance could be improved in diverse image datasets. 
- 방법 : We evaluated the use of synthetic non-contrast CT images derived from contrast CT as a data augmentation method.
- 결과 : 
    1. our results showed that in certain tasks, especially kidney segmentation, a model trained on contrast images will fail nearly completely on non-contrast images / a deterioration in performance can be expected if training data does not account for presence or absence of  contrast.
    2. we observed that augmentation using CycleGAN-generated synthetic images significantly improved segmentation performance in the non-contrast CT test set.
    3. histogram equalization augmentation led to improved results compared to standard augmentation for liver and spleen but no improvement for kidney
    4. We speculate that segmentation performance of many more structures with relevant contrast enhancement may benefit from this augmentation technique.
- 한계 : CycleGAN method is applied to single slices (2D) of the 3D input volume. This leads to slice-to-slice inconsistencies which may adversely affect performance.
- 결론 : our findings show that generative adversarial networks are a very useful augmentation tool for CT image segmentation

## Methods
### Data
in-distribution dataset (contrast CT)
out-of-distribution (non-contrast CT) 
### Experimental setup
- In standard augmentation flips, rotation, non-rigid deformation and crop were applied
- train/validation/test split was performed with a relation of 75%/5%/20%.
- in-distribution (contrast CT) dataset classic 5-fold cross-validation was used

### Neural network architecture and training
segmentation Model : modified 3D U-Net, leaky ReLU, group normalization (group size 16), a strided convolution, input sizes of up to 256 × 256 × 192 ->  192 × 192 × 192 volumes
Dice loss :  

### Augmentation methods
1. Generation of synthetic non-contrast CT images using CycleGAN
- DeepLesion NIH data set
- This resulted in 10,681 contrast CTs and 603 non-contrast CTs available for the training of the GAN.
- no segmentation labels are available for this data set.
2. Histogram equalization augmentation
-to shift the histogram of contrast CTs toward a non-contrast CT histogram using a Python implementation of the MATLAB function histeq
3. Standard data augmentation.
- A typical 3D data augmentation pipeline was used in all experiments including flipping, random crop, 3D rotation (up to 30), and elastic 3D deformation (b-spline transformation, 10 control points, deformation Gaussian σ = 8)

## Statistical analysis
Test datasets : Dice loss and volume error

## Data availability

----
----
----

# Data augmentation using generative adversarial networks (CycleGAN) to improve generalizability in CT segmentation tasks
- https://www.nature.com/articles/s41598-019-52737-x
- Published: 15 November 2019
- Scientific Reports

---
![image](https://user-images.githubusercontent.com/70581043/127729989-e5368367-976e-425e-b15d-6597385ed80c.png)

## Summary
- 의료 데이터의 문제 : Labeled medical imaging data is scarce and expensive to generate.
- 논문 제안 : We evaluate the use of CycleGAN for data augmentation in CT segmentation tasks. 
> - CycleGAN으로 contrast CT images를 non-contrast images로 변환
>- 새로 만든 non-contrast images를 CycleGAN으로 훈련시켜 이미지 augmentation
- 논문 결과 : We show that in several CT segmentation tasks performance is improved significantly.

## Methods
- Standard augmentation : flips, rotation, non-rigid deformation and crop
- CycleGAN augmentation : 10,681 contrast CTs , 603 non-contrast CTs Data 사용, no segmentation labels
- Histogram equalization augmentation : to shift the histogram of contrast CTs toward a non-contrast CT histogram
- Training Model : U-Net
- Metrics :  

> - Dice loss  ( where s = 1 for training and s = 0 for evaluation )
![image](https://user-images.githubusercontent.com/70581043/127730152-3eeaec5e-d936-45ae-9b73-782efd8f9764.png)
 
> - volume error 
![image](https://user-images.githubusercontent.com/70581043/127730155-44b53de5-e896-426a-8895-16bb3d48eaea.png)

