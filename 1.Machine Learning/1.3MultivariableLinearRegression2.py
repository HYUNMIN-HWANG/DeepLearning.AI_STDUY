# Multivariable Linear Regression
# feature가 여러개 
# h(x) = w1x1 + w2x2 + w3x3 ...

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

# DATA
x_train  =  torch.FloatTensor([[73,  80,  75], 
                               [93,  88,  93], 
                               [89,  91,  80], 
                               [96,  98,  100],   
                               [73,  66,  70]])  
y_train  =  torch.FloatTensor([[152],  [185],  [180],  [196],  [142]])

# W와 b 초기화
w = torch.zeros((3,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# optimizer
optimzer = optim.SGD([w, b], lr=1e-5) 

nb_epochs = 2000
nb_epochs = 300
for epoch in range(nb_epochs) : 
    # hypothesis
    hypothesis = x_train.matmul(w) + b

    # cost 계산 
    cost = torch.mean((hypothesis - y_train) ** 2)

    optimzer.zero_grad()
    cost.backward()
    optimzer.step()

    if epoch % 100 == 0 :
        print("Epoch : {:4d} / hypothesis : {}, cost : {:.6f}".format(
            epoch, hypothesis.squeeze().detach(), cost.item()
        ))

    # hypothesis 출력하면 
    # tensor([[154.0278],
    #         [185.0649],
    #         [175.9335],
    #         [198.5128],
    #         [141.2284]], grad_fn=<AddBackward0>)
    # squeeze : 차원의 size가 1인 차원을 없애줌

# Epoch :    0 / hypothesis : tensor([0., 0., 0., 0., 0.]), cost : 29661.800781
# Epoch :  100 / hypothesis : tensor([154.0433, 185.0925, 175.8312, 198.5701, 141.2221]), cost : 5.754573
# Epoch :  200 / hypothesis : tensor([154.0278, 185.0649, 175.9335, 198.5128, 141.2284]), cost : 5.512386
# Epoch :  300 / hypothesis : tensor([154.0120, 185.0385, 176.0329, 198.4569, 141.2353]), cost : 5.281667
# Epoch :  400 / hypothesis : tensor([153.9960, 185.0133, 176.1295, 198.4022, 141.2426]), cost : 5.061868
# Epoch :  500 / hypothesis : tensor([153.9797, 184.9892, 176.2233, 198.3488, 141.2504]), cost : 4.852424
# Epoch :  600 / hypothesis : tensor([153.9632, 184.9662, 176.3143, 198.2966, 141.2586]), cost : 4.652705
# Epoch :  700 / hypothesis : tensor([153.9465, 184.9442, 176.4028, 198.2456, 141.2672]), cost : 4.462287
# Epoch :  800 / hypothesis : tensor([153.9296, 184.9232, 176.4888, 198.1958, 141.2762]), cost : 4.280604
# Epoch :  900 / hypothesis : tensor([153.9126, 184.9032, 176.5724, 198.1471, 141.2855]), cost : 4.107294
# Epoch : 1000 / hypothesis : tensor([153.8955, 184.8841, 176.6536, 198.0995, 141.2951]), cost : 3.941866
# Epoch : 1100 / hypothesis : tensor([153.8782, 184.8660, 176.7325, 198.0530, 141.3051]), cost : 3.783911
# Epoch : 1200 / hypothesis : tensor([153.8608, 184.8486, 176.8092, 198.0075, 141.3153]), cost : 3.633077
# Epoch : 1300 / hypothesis : tensor([153.8434, 184.8320, 176.8838, 197.9630, 141.3257]), cost : 3.488997
# Epoch : 1400 / hypothesis : tensor([153.8259, 184.8163, 176.9563, 197.9195, 141.3364]), cost : 3.351316
# Epoch : 1500 / hypothesis : tensor([153.8083, 184.8013, 177.0268, 197.8770, 141.3473]), cost : 3.219756
# Epoch : 1600 / hypothesis : tensor([153.7908, 184.7870, 177.0953, 197.8355, 141.3584]), cost : 3.093989
# Epoch : 1700 / hypothesis : tensor([153.7732, 184.7734, 177.1620, 197.7948, 141.3697]), cost : 2.973708
# Epoch : 1800 / hypothesis : tensor([153.7556, 184.7604, 177.2268, 197.7551, 141.3811]), cost : 2.858705
# Epoch : 1900 / hypothesis : tensor([153.7380, 184.7481, 177.2899, 197.7162, 141.3927]), cost : 2.748643
