import sys 
n , k = map(int, sys.stdin.readline().split())

array_1 = list(map(int,sys.stdin.readline().split()))

array_2 = list(map(int,sys.stdin.readline().split()))

array_1 = sorted(array_1)
array_2 = sorted(array_2)

for i in range(k):
    array_1[i] = array_2[n-1-i] if array_1[i] < array_2[n-1-i] else array_1[i]


print(sum(array_1))