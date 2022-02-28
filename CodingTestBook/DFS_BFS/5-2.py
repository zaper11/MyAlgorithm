from collections import deque

#queue 구현을 위해 deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.pop()

print(queue)
queue.reverse()
print(queue)