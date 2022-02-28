import sys

def AC(p,n,x):
    num_r = 0
    while len(x) != 0 and len(p) != 0:
        if p[0] == "R":
            del p[0]
            num_r += 1
        elif p[0] == "D":
            if num_r % 2 == 0:
                num_r = 0
                del x[0]
                del p[0]
            else:
                x.reverse()
                del x[0]
                del p[0]
                num_r = 0
        else:
            del p[0]
    while len(x) == 0 and p[0] == "R":
        del p[0]
    if len(x) == 0 and p[0] == "D":
        print("error")
    else:
        print(x)

T = int(sys.stdin.readline())
for i in range(T):
    p = list(sys.stdin.readline())
    n = sys.stdin.readline()
    x = sys.stdin.readline()
    x = x[1:len(x)-2]
    x = x.split(",")
    AC(p,n,x)

'''
import sys
from collections import deque

t = int(input())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
'''