n, k = map(int, input().split())
elc = list(map(int, input().split()) for _ in range(k))

m = [0]*101
for i in elc:
    m[i] += 1
    
print(elc)