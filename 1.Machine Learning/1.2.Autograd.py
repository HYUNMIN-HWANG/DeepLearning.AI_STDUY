# 경사하강법에서의 미분

import torch
w = torch.tensor(2.0, requires_grad=True)   # requires_grad=True ; 이 텐서에 대한 기울기를 저장하겠다
print(w)    # tensor(2., requires_grad=True)

y = w**2
z = 2*y + 5 # z = 2w**2 + 5

# w에 대해 미분
z.backward()

print("수식을 w로 미분한 값 : {}".format(w.grad))
# 수식을 w로 미분한 값 : 8.0