n = int(input())
a = list(map(int,input().split()))
m = int(input())
b =  list(map(int,input().split()))

a.sort()

def binary(c, a, start, end):
    if start > end:
        return 0
    half = (start+ end)//2
    if c == a[half]:
        return 1
    elif c < a[half]:
        return binary(c, a, start, half-1)
    else:
        return binary(c, a, half +1,end)

for i in b:
    print(binary(i,a,0,len(a)-1))
