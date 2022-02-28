#  <8_3.py> 개미 전사

import sys

n = int(sys.stdin.readline().strip())

food_warehous = list(map(int,sys.stdin.readline().split()))

dt = [0] * 100

dt[0] = food_warehous[0]
dt[1] = max(food_warehous[0],food_warehous[1])

for i in range(2,n):
    dt[i] = max(food_warehous[i]+dt[i-2],dt[i-1])

print(dt[n-1])