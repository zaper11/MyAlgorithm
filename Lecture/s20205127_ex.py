def budget(evaluation):
    n = len(evaluation)
    if n == 0:
        return 0
    res = 1
    pre = 1
    start = 0
    prestart = 1
    for i in range(1,n):
        if evaluation[i] == evaluation[i - 1]:
            pre = 1
            start = i
            prestart = pre
        elif evaluation[i] > evaluation[i - 1]:
            pre += 1
            start = i
            prestart = pre
        else:
            res += i - start - 1
            if i - start + 1 > prestart:
                prestart = i - start + 1
                res += 1
            pre = 1
        res += pre
    res = res*1000
    return res