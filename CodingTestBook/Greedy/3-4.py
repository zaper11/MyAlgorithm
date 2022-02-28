n,k = map(int, input().split())
result = 0

while True:
    if n == 1:
        break;
    if n%k != 0:
        use = (n // k) * k
        result += n - use
        n -= use
    n = n//k
    result += 1

print(result)