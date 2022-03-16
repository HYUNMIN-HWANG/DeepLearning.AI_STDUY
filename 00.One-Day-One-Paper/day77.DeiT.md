# Training data-efficient image transformers &distillation through attention

그동안 ViT의 단점 : 큰 데이터 셋을 사용해야 했음( pre-trained with hundreds of millions of images using a large infrastructure, thereby limiting their adoption )              
이를 해결하기 위해서 DeiT 제안함 : Imagenet 데이터만 사용해서 훈련시키는 transformer 모델을 제안함.          
Contributions : 
    - teacher-student strategy 사용
    - distillation token 추가 (class token과 거의 같은 role을 수행함, 근데 teacher 에서 추론한 label값을 사용한다는 차이점)
    - 다른 transformer 모델과 경쟁적인 결과를 보였음
    - image classification task 수행 잘 함

# DeiT (Data-efficient image Transformers)


### MSA (Multi-head Self Attention layers)
- query vector와 key vector의 inner products -> softmax로 normalization -> k weights 얻음 -> attention을 통과시켜 k value vectors의 평균을 구함 -> root d로 나눔으로써 normalization -> "h" 개 attention heads로 구성됨

### Transformer
- MSA 다음에 Feed Forward Network 추가함 -> GeLu activation 추가함 -> skip connection, layer normalization 
- 이미지 데이터를 16*16 pixels로 N patches 로 자름
- position 정보를 모르기 때문에 positional embeddings를 추가함
- class token 
   - predict the class
   - appended to the patch tokens before the first layer

### Distillation through attention
![image](https://user-images.githubusercontent.com/70581043/158523833-9ad56c09-9b1f-4f5e-ba4e-6a641b3e908b.png)
- Soft distillation : minimizes the Kullback-Leibler divergence between the softmax of the teacher and the softmax of the student model
![image](https://user-images.githubusercontent.com/70581043/158526961-1618cd59-d6eb-4950-976f-e47971e002e5.png)

- Hard-label distillation : variant of distillation where we take the hard decision of the teacher as a true label.  The teacher prediction yt plays the same role as the true label y.
![image](https://user-images.githubusercontent.com/70581043/158527021-9d1d846d-6e9f-4f45-9fda-b9db2729304b.png)

- Distillation token : class token과 유사하게 self-attention에 임베딩할 때 들어감, 네트워크의 마지막 레이어의 아웃풋으로 나옴

## Results
![image](https://user-images.githubusercontent.com/70581043/158528104-eccf32a1-e364-46b8-b3d2-1997bb59d18c.png)
- Hard distillation significantly outperforms soft distillation for transformers
- two tokens provide complementary information useful for classification (class token & distillation token)
