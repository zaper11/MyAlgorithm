import sys
read = sys.stdin.readline

N = int(read())
crane = list(map(int, read().split()))
M = int(read())
box = list(map(int,read().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    print(-1)
    sys.exit()
else:
    answer = 0
    while(True):
        if not box:
            break
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        answer += 1

print(answer)