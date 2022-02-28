n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
result = 0
a = 0
b = n-1
m.sort()
while m[a] < 1 and m[a+1] < 1:
    result += m[a]*m[a+1]
    a += 2
if m[a] < 1:
    result += m[a]
    a += 1
if m[a] == 1:
    result += 1
while a+1 < n and m[a] > 1 :
    result += m[a]*m[a+1]
    a += 2
if a+1 != n:
    result += m[n-1]
print(result)