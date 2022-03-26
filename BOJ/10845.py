import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    ip = sys.stdin.readline().split()
    if ip[0] == "push":
        queue.append(int(ip[1]))

    elif ip[0] == "size":
        print(len(queue))

    elif ip[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif ip[0] == "pop":
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)

    elif ip[0] == "front":
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)

    elif ip[0] == "back":
        if len(queue) != 0:
            print(queue[len(queue) -1])
        else:
            print(-1)