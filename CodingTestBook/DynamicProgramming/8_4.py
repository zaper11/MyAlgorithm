#  <8_4.py> 바닥 공사

import sys

n = int(sys.stdin.readline().strip())

dt = [0]*1001

dt[0] = 1
dt[1] = 1
dt[2] = 3


for i in range(3,n+1):
    dt[i] = (dt[i-1]+ dt[i-2]*2)%796796

print(dt[n])

