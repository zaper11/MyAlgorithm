from collections import deque


def move():
    location = set()
    for i in range(R):
        for j in range(C):
            if board[i][j]: location.add((i, j))
    for i, j in location:
        speed, direction, size = board[i][j].popleft()
        if direction == UP:
            i = i - speed
            if i >= 0:
                board[i][j].append([speed, direction, size])
            else:
                i = (-i) % ((R - 1) * 2)
                if i <= R - 1: direction = DOWN  # 방향
                i = row_list[i]  # 위치
                board[i][j].append([speed, direction, size])
        elif direction == DOWN:
            i = i + speed
            if i <= R - 1:
                board[i][j].append([speed, direction, size])
            else:
                i = i % ((R - 1) * 2)
                if i == 0 or i >= R: direction = UP  # 방향
                i = row_list[i]  # 위치
                board[i][j].append([speed, direction, size])
        elif direction == LEFT:
            j = j - speed
            if j >= 0:
                board[i][j].append([speed, direction, size])
            else:
                j = (-j) % ((C - 1) * 2)
                if j <= C - 1: direction = RIGHT
                j = col_list[j]
                board[i][j].append([speed, direction, size])
        elif direction == RIGHT:
            j = j + speed
            if j <= C - 1:
                board[i][j].append([speed, direction, size])
            else:
                j = j % ((C - 1) * 2)
                if j == 0 or j >= C: direction = LEFT
                j = col_list[j]
                board[i][j].append([speed, direction, size])
    for i in range(R):
        for j in range(C):
            if len(board[i][j]) > 1:
                board[i][j] = deque([max(board[i][j], key=lambda x: x[2])])


if __name__ == '__main__':
    R, C, M = map(int, input().split())
    board = [[deque() for j in range(C)] for i in range(R)]

    for _ in range(M):
        r, c, s, d, z = map(int, input().split())
        board[r - 1][c - 1].append([s, d, z])
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4
    row_list = [i for i in range(R)]
    for i in range(R - 2, 0, -1): row_list.append(i)

    col_list = [i for i in range(C)]
    for i in range(C - 2, 0, -1): col_list.append(i)

    king = -1
    sv = 0
    while True:
        king += 1
        for i in range(R):
            if board[i][king]:
                shark = board[i][king].pop()
                sv += shark[-1]
                break
        move()
        if king == C - 1: break
    print(sv)