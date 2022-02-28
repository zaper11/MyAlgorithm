import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    ip = sys.stdin.readline().split()
    if ip[0] == "push":
        stack.append(int(ip[1]))
    elif ip[0] == "top":
        if len(stack) != 0:
            print(stack[len(stack) - 1])
        else:
            print(-1)
    elif ip[0] == "size":
        print(len(stack))
    elif ip[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ip[0] == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
