# Histograms of oriented gradients for human detection
- 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR'05)
- 참고 : https://hohodu.tistory.com/19, https://studyingfox.tistory.com/5?category=849140
---

## Summary
Human Detection을 위한 새로운 feature set을 제안했다.

- feature extraction chain
![image](https://user-images.githubusercontent.com/70581043/132876904-0685c8d0-38a1-4e0c-a057-d6c74eec8ea8.png)
image의 gradient orientation 을 normalize한 후, local histogram으로 만들었다.
1. Gamma / Colour Normalization
- RGB / LAB colour 의 경우, 이를 normalization 하면 보통의 결과가 나온다.
- Square root gamma compression을 하면 성능이 향상되기도 한다.
2. Gradient Computation
- Gaussian smoothing
- Simple 1-D [-1, 0, 1] 일 때 성능이 가장 좋았다.
3. Spatial / Orientation Binning
- Each pixel calculates a weighted vote for an edge orientation histogram channel based on the orientation of the gradient element centred on it, and the votes are accumulated into orientation bins over local spatial regions that we call cells.
- edge orientation histogram : orientation of the gradient 를 기반으로 각 픽셀의 가중치를 계산하여 vote 방식으로 값을 넣는다.
- 9 bins ( 180도 를 9로 나눔, 각각 20도씩)
4. Normalization and Descriptor Blocks
- cell을 group화 하여 larger spatial blocks를 기반으로 normalization을 한다.
- (1) R-HOG : square or rectangular block
- (2) C-HOG : circular blocks
- Batch Normalization
> -  ![image](https://user-images.githubusercontent.com/70581043/132880599-aae46b53-bbb0-4933-b606-5c3607c5f9ac.png)
> - ![image](https://user-images.githubusercontent.com/70581043/132880640-b1f976c9-6fc7-4ed0-9485-dcc140a1ba8b.png)
> - ![image](https://user-images.githubusercontent.com/70581043/132880688-49193873-1023-4851-ae33-6216d0ab286e.png)
> - ![image](https://user-images.githubusercontent.com/70581043/132880736-7266ecdf-2e0c-41f2-a49a-ad61417ba661.png)
5. Detector Window and Context
- 64 * 128 detedction window
- 16 pixels of margin around the person (16을 8로 줄였더니, 성능이 줗었다.)
6. Classifier
- SVMLight


