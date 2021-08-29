# Classification of Brain Tumors from MRI Images Using a Convolutional Neural Network
- https://www.mdpi.com/2076-3417/10/6/1999
- Published: 15 March 2020
---
## Summary
brain tumor 3가지 종류를 MRI 영상 데이터를 기반으로 classification했다. 각 tumor 마다 신체에 끼치는 영향이 다르기 때문에 초기에 발견해 적절한 조치를 취하는 것이 중요하다.
1. gliomas
2. meningiomas
3. pituitary tumors

## Network Architecture
![image](https://user-images.githubusercontent.com/70581043/131242936-96beed98-478e-4b64-8bb3-0fb8da13e917.png)
- Block A : Convolution layer (input 이미지 보다 2배 작은 이미지를 output), RELU, Dropout, max pooling
- Block B : Convolution layer (input이미지와 동일한 사이즈 이미지를 output), RELU, Dropout, max pooling
- Classification : Flatten FC -> tumor 종류와 동일한 수의 unit으로 마무리
 
### Training
- k-fold cross-validation method를 사용함
- 2가지 접근방식
>  1. record-wise cross-validation : randomly divide the data into 10 approximately equal portions → each tumor category was equally present in each portion
> 2. subject-wise cross-validation : randomly divide the data into 10 approximately equal portions → the data from a single subject could only be found in one of the sets

## Results
### record-wise
- record-wise 10-fold cross-validation (from the original dataset)
![image](https://user-images.githubusercontent.com/70581043/131243153-469d2965-a447-415c-bcff-ef2c594b0254.png)
- record-wise 10-fold cross-validation (augmented dataset)
- augmented 한 게 안 한 것보다 성능이 더 좋다.
![image](https://user-images.githubusercontent.com/70581043/131243191-2cd3948f-f6fc-4672-8d0a-d1e3617c8a43.png)

### subject-wise
- subject-wise 10-fold cross-validation (from the original dataset)
![image](https://user-images.githubusercontent.com/70581043/131243244-e998a421-f0be-4392-aaef-7f455324c3d1.png)
- subject-wise 10-fold cross-validation (augmented dataset)
- augmented한 것이 안 한 것보다는 성능이 좋지만, 결과적으로 record-wise에서의 성능이 더 좋았다.
![image](https://user-images.githubusercontent.com/70581043/131243252-bb114edb-7aaa-4730-80c5-3824e74dd282.png)

### Comparison with State-of-the-Art-Methods
- 선행 연구와 비교해도 가장 성능이 좋다.
![image](https://user-images.githubusercontent.com/70581043/131243271-cfff4e98-5ba8-4ead-9928-414f97f6f2ba.png)
