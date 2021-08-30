# Dropout: A Simple Way to Prevent Neural Networks from Overfitting
- https://jmlr.org/papers/v15/srivastava14a.html
- Nitish Srivastava, Geoffrey Hinton, Alex Krizhevsky, Ilya Sutskever, Ruslan Salakhutdinov; 15(56):1929−1958, 2014.
---
총 30페이지..ㅎㅎ 오늘은 개념 정리하고, 내일은 결과 부분 읽겠습니다.

## Summary
dropout 기법을 사용함으로써 overfitting을 막을 수 있고, neural network를 다양하게 조합하면서 다양한 architecture를 만들 수 있다.

  ---
![image](https://user-images.githubusercontent.com/70581043/131343895-e1907f94-472f-4c2d-90dc-1f964ea20b2c.png)
(a) drop out을 적용하지 않은 architecture
(b) drop out을 적용한 'thinned net' (train을 할 때마다 dropout할 노드가 랜덤하게 정해진다. 2의 n승 개의 모델 구조를 만들 수 있다. weight를 공유한다.)

---
![image](https://user-images.githubusercontent.com/70581043/131344049-83fa22d7-f05f-423b-b57c-ecbd094e27b6.png)
- train 단계 : train을 할 때마다 dropout할 노드가 랜덤하게 정해진다. 2의 n승 개의 모델 구조를 만들 수 있다. weight를 공유한다.
- test 단계 : approximate averaging method, test 단계에서는 dropout이 없다. train할 때 확률 p를 보유하고 있다면 test 에서는 weight에 p를 곱한다.

---
![image](https://user-images.githubusercontent.com/70581043/131345186-70ecce59-8287-40bb-ba67-fcd26632206e.png)
![image](https://user-images.githubusercontent.com/70581043/131345214-4ad7e1a8-5a6b-447c-a869-05c7cbcca0a4.png) : Bernoulli random variables each of which has probability p of being 1.
![image](https://user-images.githubusercontent.com/70581043/131345368-5aebb960-70f6-4b16-9b25-9d7f12c79798.png) : thinned output, input og the next layer
![image](https://user-images.githubusercontent.com/70581043/131345421-3ac5d94b-2e44-48e1-bbf5-701f91a829ee.png) : inputs into layer l+1
![image](https://user-images.githubusercontent.com/70581043/131345568-0c2048a2-ab39-4a01-9685-4678ba04abae.png) : apply activation function





