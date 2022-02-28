num = int(input())
n = int(input())
m = list(map(int,input().split()))
result = 0
m.sort()
a = 0
b = num -1
while m[a]<=m[b] and a!=b:
    if(m[a] + m[b] == n):
        result += 1
        a += 1
        b -= 1
    elif m[a] + m[b] < n:
        a += 1
    else:
        b -= 1
print(result)