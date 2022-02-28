#  <8_5.py> 효율적인 화폐 구성 

import sys

n,m = map(int,sys.stdin.readline().split())

money_list = list(map(int,sys.stdin.readline().split()))
money_list = sorted(money_list)

dt = [sys.maxsize]*10001

for i in money_list:
    dt[i] = 1   

for i in range(0,m+1):
    for money in money_list:
        if(i-money<0):
            continue
        if(dt[i-money]==sys.maxsize):
            continue
        dt[i] = min(dt[i],dt[i-money]+1)

if(dt[m]!=sys.maxsize):
    print(dt[m])
else:
    print(-1)