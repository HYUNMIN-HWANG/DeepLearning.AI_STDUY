# Multivariable Linear Regression
# feature가 여러개 
# h(x) = w1x1 + w2x2 + w3x3 ...

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

# DATA
x1_train = torch.FloatTensor([[73], [93], [89], [96], [73]])
x2_train = torch.FloatTensor([[80], [88], [91], [98], [66]])
x3_train = torch.FloatTensor([[75], [93], [90], [100], [70]])
y_train = torch.FloatTensor([[152], [185], [180], [196], [142]])

# W와 b 초기화
w1 = torch.zeros(1, requires_grad=True)
w2 = torch.zeros(1, requires_grad=True)
w3 = torch.zeros(1, requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# optimizer
optimzer = optim.SGD([w1, w2, w3, b], lr=1e-5) 

nb_epochs = 2000
for epoch in range(nb_epochs) : 
    # hypothesis
    hypothesis = x1_train * w1 + x2_train * w2 + x3_train * w3 + b

    # cost 계산 
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimzer.zero_grad()
    cost.backward()
    optimzer.step()

    if epoch % 100 == 0 :
        print("Epoch : {:4d} / w1 : {:.3f}, w2{:.3f}, w3{:.3f}, b{:.3f}, cost : {:.6f}".format(
            epoch, w1.item(), w2.item(), w3.item(), b.item(), cost.item()
        ))

# Epoch :    0 / w1 : 0.294, w20.294, w30.297, b0.003, cost : 29661.800781
# Epoch :  100 / w1 : 0.674, w20.661, w30.676, b0.008, cost : 1.563634
# Epoch :  200 / w1 : 0.679, w20.655, w30.677, b0.008, cost : 1.497607
# Epoch :  300 / w1 : 0.684, w20.649, w30.677, b0.008, cost : 1.435026
# Epoch :  400 / w1 : 0.689, w20.643, w30.678, b0.008, cost : 1.375730
# Epoch :  500 / w1 : 0.694, w20.638, w30.678, b0.009, cost : 1.319511
# Epoch :  600 / w1 : 0.699, w20.633, w30.679, b0.009, cost : 1.266222
# Epoch :  700 / w1 : 0.704, w20.627, w30.679, b0.009, cost : 1.215696
# Epoch :  800 / w1 : 0.709, w20.622, w30.679, b0.009, cost : 1.167818
# Epoch :  900 / w1 : 0.713, w20.617, w30.680, b0.009, cost : 1.122429
# Epoch : 1000 / w1 : 0.718, w20.613, w30.680, b0.009, cost : 1.079378
# Epoch : 1100 / w1 : 0.722, w20.608, w30.680, b0.009, cost : 1.038584
# Epoch : 1200 / w1 : 0.727, w20.603, w30.681, b0.010, cost : 0.999894
# Epoch : 1300 / w1 : 0.731, w20.599, w30.681, b0.010, cost : 0.963217
# Epoch : 1400 / w1 : 0.735, w20.595, w30.681, b0.010, cost : 0.928421
# Epoch : 1500 / w1 : 0.739, w20.591, w30.681, b0.010, cost : 0.895453
# Epoch : 1600 / w1 : 0.743, w20.586, w30.682, b0.010, cost : 0.864161
# Epoch : 1700 / w1 : 0.746, w20.583, w30.682, b0.010, cost : 0.834503
# Epoch : 1800 / w1 : 0.750, w20.579, w30.682, b0.010, cost : 0.806375
# Epoch : 1900 / w1 : 0.754, w20.575, w30.682, b0.010, cost : 0.779696