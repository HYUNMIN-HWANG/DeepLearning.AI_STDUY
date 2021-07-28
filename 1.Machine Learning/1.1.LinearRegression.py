# linear Regression

# 기본 셋팅
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

'''DATA'''
x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

print(x_train)
print(x_train.shape)
# tensor([[1.],
#         [2.],
#         [3.]])
# torch.Size([3, 1])

print(y_train)
print(y_train.shape)
# tensor([[2.],
#         [4.],
#         [6.]])
# torch.Size([3, 1])

'''가중치, 편향 초기화'''
# y = wx + b : w와 b를 초기화시켜준다.
W = torch.zeros(1, requires_grad=True)  # 해당 텐서에 대한 계산 모두 tracking해서 기울기 구해주기
print(W)    # tensor([0.], requires_grad=True)

b = torch.zeros(1, requires_grad=True)
print(b)    # tensor([0.], requires_grad=True)

'''경사 하강법 구현'''
# SGD : 경사 하강법 중 하나
# lr : learning rate
optimizer = optim.SGD([W, b], lr = 0.01)

nb_epochs = 2000
for epoch in range(nb_epochs) :

    '''hypothesis'''
    hypothesis = x_train * W + b
    # print(hypothesis)
    # tensor([[0.],
    #         [0.],
    #         [0.]], grad_fn=<AddBackward0>)

    '''cost 함수 선언'''
    cost = torch.mean((hypothesis - y_train) ** 2)
    # print(cost) # tensor(18.6667, grad_fn=<MeanBackward0>)

    # gradient를 0으로 초기화
    optimizer.zero_grad()
    # 비용 함수를 미분하여 gradient 계산
    cost.backward()
    # W와 b 업데이트
    optimizer.step()

    if epoch % 100 == 0 :
        print("Epoch : {:4d} / W : {:.3f} , b : {:.3f} , Cost : {:.6f}".format(
            epoch, W.item(), b.item(), cost.item()
        ))

# Epoch :    0 / W : 0.187 , b : 0.080 , Cost : 18.666666
# Epoch :  100 / W : 1.746 , b : 0.578 , Cost : 0.048171
# Epoch :  200 / W : 1.800 , b : 0.454 , Cost : 0.029767
# Epoch :  300 / W : 1.843 , b : 0.357 , Cost : 0.018394
# Epoch :  400 / W : 1.876 , b : 0.281 , Cost : 0.011366
# Epoch :  500 / W : 1.903 , b : 0.221 , Cost : 0.007024
# Epoch :  600 / W : 1.924 , b : 0.174 , Cost : 0.004340
# Epoch :  700 / W : 1.940 , b : 0.136 , Cost : 0.002682
# Epoch :  800 / W : 1.953 , b : 0.107 , Cost : 0.001657
# Epoch :  900 / W : 1.963 , b : 0.084 , Cost : 0.001024
# Epoch : 1000 / W : 1.971 , b : 0.066 , Cost : 0.000633
# Epoch : 1100 / W : 1.977 , b : 0.052 , Cost : 0.000391
# Epoch : 1200 / W : 1.982 , b : 0.041 , Cost : 0.000242
# Epoch : 1300 / W : 1.986 , b : 0.032 , Cost : 0.000149
# Epoch : 1400 / W : 1.989 , b : 0.025 , Cost : 0.000092
# Epoch : 1500 / W : 1.991 , b : 0.020 , Cost : 0.000057
# Epoch : 1600 / W : 1.993 , b : 0.016 , Cost : 0.000035
# Epoch : 1700 / W : 1.995 , b : 0.012 , Cost : 0.000022
# Epoch : 1800 / W : 1.996 , b : 0.010 , Cost : 0.000013
# Epoch : 1900 / W : 1.997 , b : 0.008 , Cost : 0.000008
