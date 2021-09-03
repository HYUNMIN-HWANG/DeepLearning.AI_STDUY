# Object recognition from local scale-invariant features
https://ieeexplore.ieee.org/document/790410
- Publisher: IEEE, 1999
---
논문으로는 이해가 잘 안가서 참고자료들 보고 이해했습니다.
https://ballentain.tistory.com/47
https://bskyvision.com/21
https://intuitive-robotics.tistory.com/93

---
## SIFT : Scale Invariant Feature Transform
scale, rotation, brightness에 영향 받지 않는 특징점 추출 알고리즘       
크게 4가지 단계로 구성되어 있다.

### 1. Scale-space extrema detection
![image](https://user-images.githubusercontent.com/70581043/131958133-815cd70d-136d-4dfe-b271-ae393de8037a.png)
- scale-space란? : 원본 이미지를 다양한 크기로 resize 해서 image pyramid를 만들고 각 층의 이미지에 gaussian blur를 점점 크게 적용시켜 얻은 이미지
- octave : 같은 크기 scale인 이미지들의 모임

![image](https://user-images.githubusercontent.com/70581043/131958153-9cb1e7b5-ef4a-44de-9f47-3746e1c07afa.png)
- DoG (difference of gaussian) : 같은 octave 내 서로 다른 blur image를 빼기
- 4개 scale로 이미지 사이즈를 조정한 뒤,  서로 다른 크기의 5가지 gaussian blur를 적용시킨다. DoG로는 한 octave당 4개의 DoG가 나온다. 

![image](https://user-images.githubusercontent.com/70581043/131958189-487415ea-16dd-4049-8a30-3cdfb03e29a1.png)
- extreme detection : target pixel 이 극소값이거나 극대값이면 keypoint 후보군으로 정한다.
- 이때 target pixel 주위에 있는 26개의 pixel끼리 비교를 해서 극점인지를 판단하는 것이다.
- octave2-3-4 , octave 1-2-3 이렇게 2번만 비교할 수 있음 (ocatave1과 4는 위 아래가 없다.) 한 octave당 4장의 DoG가 있기 때문에 총 8개의 keypoint가 추출된다.

### 2. Key point localization
- Keypoint가 정확한 좌표계에 위치하지 않기 때문에 이를 해결하기 위해 테일러 급수를 적용한다.
![image](https://user-images.githubusercontent.com/70581043/131958475-45eb8b20-d839-43e1-81d4-294eeecee006.png)
- 해당 식을 미분했을 때 0이 되는 구간이 극점이 된다.
- 1) 또한, 특정 threshold값보다 낮은 keypoint들은 제거하고
- 2) edge위에 위치한 key값들도 제거한다.

### 3. Orientation assignment
- keypoint의 크기와 방향
![image](https://user-images.githubusercontent.com/70581043/131958651-3619972d-d125-49cc-8830-024a26030969.png)
![image](https://user-images.githubusercontent.com/70581043/131959091-cfc87aa6-a53d-4c52-8ac4-27246699b892.png)
- 이미지를 gaussian blur 처리를 한 후, gradient magnitude와 gradient orientation을 계산한다.

- keypoint의 방향성을 설정하기 위해서 : 360도를 10도씩 구분하여 총 36개의 bin으로 구성된 orientation histogram을 생성한다.
![image](https://user-images.githubusercontent.com/70581043/131958718-71562eec-950b-4616-8bba-c180f1b45fa4.png)
- 가장 높은 bin값이 keypoint의 방향이 되며,
- 가장 높은 bin값의 80%에 해당하는 값이 있다면 orientation을 추가하기도 한다.
- 예 ) keypoint1 : ( x좌표, y좌표, scale factor, octave, orientation ) = ( 10, 20, 2.0, 3, 95 ) , keypoint2 : ( x좌표, y좌표, scale factor, octave, orientation ) = ( 10, 20, 2.0, 3, 205 )

### 4. Key point descriptor
- key point를 식별하기 위한 fingerprint지문과 같은 정보를 추출한다.
![image](https://user-images.githubusercontent.com/70581043/131959187-ecbcec24-0b3c-4d26-8a09-acd23b46cf53.png)
- 16x16 patch를 4x4 sub-patch로 분할한다.
- 각 patch마다 8개 bin으로 이루어진 orientation histogram을 만든다.
- 16개 patch * 8개 bin = 128개 숫자를 가진 descriptor를 만들 수 있다.
- 이미지가 회전했을 때도, 회전한 각도에 영향을 받지 않기 위해 : descriptor 에서 keypoint orientation을 빼준다.
> + 또한, 밝기에 영향을 받지 않기 위해 normalization을 해준다.