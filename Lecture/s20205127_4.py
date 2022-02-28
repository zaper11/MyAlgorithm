def LanguageOrder(words):
    adj = {c:set() for w in words for c in w}
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        Len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:Len] == w2[:Len]:
            return ""
        for j in range(Len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break
    visit = {}
    res = []

    def dfs(c):
        if c in visit:
            return visit[c]

        visit[c] = 1
        for i in adj[c]:
            if dfs(i):
                return 1
        visit[c] = 0
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)