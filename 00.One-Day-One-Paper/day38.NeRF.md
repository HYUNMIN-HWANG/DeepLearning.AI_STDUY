# NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis
- https://arxiv.org/abs/2003.08934
- [Submitted on 19 Mar 2020 (v1), last revised 3 Aug 2020 (this version, v2)]
- https://www.matthewtancik.com/nerf (구현 결과 볼 수 있음, 신기함)
---

## Summary
neural radiance field (NeRF) :   이미지의 위치 x,y,z와 이미지의 방향 θ, φ을 사용하여 continuous scene as a 5D vector-valued function을 생성한다. 

- 전체 과정
![image](https://user-images.githubusercontent.com/70581043/135197880-8c107727-9cb9-41bd-80fc-e41ff26d6921.png)

1) march **camera rays** through the scene to generate a sampled set of 3D points
2) use those points and their corresponding 2D viewing **directions** as input to the neural network to produce an **output set of colors and densities**
3) use **classical volume rendering** techniques to accumulate those **colors and densities** into a 2D image

## Neural Radiance Field Scene Representation
- input :  a 3D location x = (x, y, z) and 2D viewing direction (θ, φ)
- output : an emitted color c = (r, g, b) and volume density σ
- direction as a 3D Cartesian unit vector d.
- MLP network FΘ : (x, d) → (c, σ)
- optimize its weights Θ to map from each input 5D coordinate to its corresponding volume density and directional emitted color

## Result
view synthesis 결과
![image](https://user-images.githubusercontent.com/70581043/135199802-fb3eb9e0-1916-4161-be2c-a12ab3c00fae.png)

