A = [1 2;3 4;5 6]
size(A)
%      3     2

sz = size(A)
%      3     2

size(A,1)   % 3
size(A,2)   % 2

v = [1 2 3 4]
length(v)   % 4

pwd
%     '/MATLAB Drive'

% cd : 디렉토리 이동
% ls : list of directory

% load featuresX.dat : 데이터 로드하기
% load('featureX.dat')
who
% A    C    I    a    ans  c    d    sz   v    w 

whos
%   Name      Size               Bytes  Class     Attributes
% 
%   A         3x2                   48  double              
%   C         2x3                   48  double              
%   I         4x4                  128  double              
%   a         1x1                    8  double              
%   ans       1x13                  26  char                
%   c         1x2                    4  char                
%   d         1x1                    8  double              
%   sz        1x2                   16  double              
%   v         1x4                   32  double              
%   w         1x10000            80000  double 

% clear featureX
% v = priceY(1:10) : 1열부터 10열까지

% save hello.mat v; v를 hello.mat으로 저장하기
save hello.txt A -ascii % 아스키코드로 저장

clear   % 모든 변수 지우기

A = [1 2; 3 4; 5 6]
A(3,2)  % 6
A(2, :) % ":" means every element along that row/cloums
%      3     4
A([1 3],:)
%      1     2
%      5     6
A(:,2) = [10; 11; 12]
%      1    10
%      3    11
%      5    12

A = [A, [100; 101; 102]] % append another column vector to right 
%      1    10   100
%      3    11   101
%      5    12   102

size(A)
%      3     3

A(:)    % put all elements of A into a single vector
%      1
%      3
%      5
%     10
%     11
%     12
%    100
%    101
%    102

A = [1 2; 3 4 ; 5 6];
B = [11 12; 13 14; 15 16]
[A B]
%      1     2    11    12
%      3     4    13    14
%      5     6    15    16

[A, B]
%      1     2    11    12
%      3     4    13    14
%      5     6    15    16

C = [A B]
%      1     2    11    12
%      3     4    13    14
%      5     6    15    16

C = [A; B]
%      1     2
%      3     4
%      5     6
%     11    12
%     13    14
%     15    16

