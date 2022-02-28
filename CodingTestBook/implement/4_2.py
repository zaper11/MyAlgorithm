#book p.110
position = input()
col = int(ord(position[0])) - int(ord('a')) + 1
row = int(position[1])
steps = [(1,2), (1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
i = 0
count = 0
while i<8:
    tempCol = col + steps[i][0]
    tempRow = row + steps[i][1]
    if tempCol>=1 and tempCol<=8 and tempRow>=1 and tempRow<=8:
        count += 1
    i += 1
print(count)
