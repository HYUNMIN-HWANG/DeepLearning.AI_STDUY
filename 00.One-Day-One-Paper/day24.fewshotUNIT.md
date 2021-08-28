# Few-Shot Unsupervised Image-to-Image Translation
- https://arxiv.org/abs/1905.01723
- [Submitted on 5 May 2019 (v1), last revised 9 Sep 2019 (this version, v2)]
-  International Conference on Computer Vision (ICCV) 2019
---
## Summary
![image](https://user-images.githubusercontent.com/70581043/131204976-92fb7fa1-309d-486e-a839-6c542db3cb8c.png)

기존의 비지도 image-to-image translation에서 few shot기능을 추가했다. 즉, test 단계에서 n개의 target class image를 제공함으로써 image-to-image translation의 성능을 높였다.

> we propose the **Few-shot UNsupervised Image-to-image Translation (FUNIT)** framework, aiming at learning an image-to-image translation model for mapping an image of a source class to an analogous image of a target class **by leveraging few images of the target class given at test time.**   

     


기존의 unsupervised image-to-image translation framework와의 차이점
1. we assume many source class images but few target class images.
2. we assume that the few target class images are only available at test time and can be from many different object classes.




## Learning
- 전체적인 train : minimax optimization problem
![image](https://user-images.githubusercontent.com/70581043/131205098-395255f1-27e9-453a-ad7b-9f40da255a31.png)

- GAN loss : binary prediction score of the class
![image](https://user-images.githubusercontent.com/70581043/131205104-201c7758-e185-4b0b-a7e5-70ed423ca43d.png)

- content reconstruction loss : G learn a translation model
![image](https://user-images.githubusercontent.com/70581043/131205133-a3845208-efec-4f91-9009-e4a52c685ee9.png)

- feature matching loss : 
![image](https://user-images.githubusercontent.com/70581043/131205150-79f1ee79-e39c-4752-93db-8ad73779aa25.png)


## Results
- FUNIT에서의 성능이 가장 좋았으며, few shot 이미지 개수가 많을 수록 성능이 좋았다.
![image](https://user-images.githubusercontent.com/70581043/131205196-6275af10-4cae-4f5f-8a87-1091dff312c2.png)
- FUNIT-5의 결과, 
> - class images y1y2 | input content image x | translation output ¯x
![image](https://user-images.githubusercontent.com/70581043/131205213-78eac3ad-331b-4ebb-9b5d-804a952b649e.png)
