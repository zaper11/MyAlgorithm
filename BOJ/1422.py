import functools
def cmp(a,b):
    tmp1 = a + b
    tmp2 = b + a
    return (int(tmp1) > int(tmp2)) - (int(tmp1) < int(tmp2))

n,m = map(int, input().split())
num = list(input() for _ in range(n))

max = max(int(i) for i in num)
if m-n > 0:
    for _ in range(m-n):
        num.append(str(max))

num = sorted(num, key = functools.cmp_to_key(cmp), reverse=True)
print(str(int(''.join(num))))