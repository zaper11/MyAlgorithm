#  <8_2.py>  1로 만들기

import sys

n = int(sys.stdin.readline().strip())

dt = [0] * 30001

for i in range(2,n+1):
    dt[i] = dt[i-1]+1

    if (i % 2 == 0):
        dt[i] = min(dt[i] , dt[i//2]+1)     # i/2로 나타내지 않는 이유는 typeof(i/2) == float이기 때문 
    if(i % 3 == 0):
        dt[i] = min(dt[i] , dt[i//3]+1)
    if(i % 5 == 0):
        dt[i] = min(dt[i] , dt[i//5]+1)


print(dt[n])