A = [1 2; 3 4; 5 6]
b = [11 12; 13 14; 15 16]
C = [1 1; 2 2]

A*C
%      5     5
%     11    11
%     17    17

A .* B
%     11    24
%     39    56
%     75    96

A .^ 2
%      1     4
%      9    16
%     25    36

v = [1; 2 ; 3]
1 ./ v
%    1.000000000000000
%    0.500000000000000
%    0.333333333333333

log(v)
%                    0
%    0.693147180559945
%    1.098612288668110

exp(v)
%    2.718281828459046
%    7.389056098930650
%   20.085536923187668

abs([-1; 2; -3])
%      1
%      2
%      3

-v
%     -1
%     -2
%     -3

v + ones(length(v),1)
%      2
%      3
%      4

v+1
%      2
%      3
%      4

A'
%      1     3     5
%      2     4     6

(A')'
%      1     2
%      3     4
%      5     6

a = [1 15 2 0.5]
val = max(a)    % 15
[val, ind] = max(a)
% val = 15
% ind = 2

max(A)
%      5     6

a < 3
%    1   0   1   1

find(a<3)
%      1     3     4

A = magic(3)    % 행, 열, 대각선 값이 모두 같다.
%      8     1     6
%      3     5     7
%      4     9     2

[r,c] = find(A >= 7)
% r =
%      1
%      3
%      2
% 
% 
% c =
%      1
%      2
%      3

sum(a)
%   18.500000000000000
prod(a)
% 모든 값의 곲 : 15
floor(a)
% 내림      1    15     2     0
ceil(a)
% 올림      1    15     2     1

max(rand(3), rand(3))
%    0.865030266556087   0.166849289221477   0.972086547944457
%    0.370018336149305   0.829674663686537   0.848251155537354
%    0.806944118318323   0.741582252090375   0.473569074128759

max(A, [], 1)
% 각 컬럼마다 가장 큰 값
%      8     9     7

max(A, [], 2)
% 각 열마다 가장 큰 값
%      8
%      7
%      9

max(max(A))% 9

A = magic(9)

sum(A,1)
% 각 컬럼 값 더하기
%    369   369   369   369   369   369   369   369   369

sum(A,2)
% 각 행 값 더하기
%    369
%    369
%    369
%    369
%    369
%    369
%    369
%    369
%    369

A .* eye(9)
%     47     0     0     0     0     0     0     0     0
%      0    68     0     0     0     0     0     0     0
%      0     0     8     0     0     0     0     0     0
%      0     0     0    20     0     0     0     0     0
%      0     0     0     0    41     0     0     0     0
%      0     0     0     0     0    62     0     0     0
%      0     0     0     0     0     0    74     0     0
%      0     0     0     0     0     0     0    14     0
%      0     0     0     0     0     0     0     0    35

sum(sum(A .* eye(9)))
%    369

flipud(eye(9))
%      0     0     0     0     0     0     0     0     1
%      0     0     0     0     0     0     0     1     0
%      0     0     0     0     0     0     1     0     0
%      0     0     0     0     0     1     0     0     0
%      0     0     0     0     1     0     0     0     0
%      0     0     0     1     0     0     0     0     0
%      0     0     1     0     0     0     0     0     0
%      0     1     0     0     0     0     0     0     0
%      1     0     0     0     0     0     0     0     0

A = magic(3)
temp = pinv(A) % inverse of A
%    0.147222222222223  -0.144444444444445   0.063888888888889
%   -0.061111111111112   0.022222222222224   0.105555555555554
%   -0.019444444444444   0.188888888888888  -0.102777777777777

temp * A
%    1.000000000000003   0.000000000000001  -0.000000000000003
%   -0.000000000000006   1.000000000000000   0.000000000000006
%    0.000000000000003  -0.000000000000000   0.999999999999996


