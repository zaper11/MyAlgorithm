# Chapter 6 
# <2> 위에서 아래로 

sequence_list = []

n = int(input())

for i in range(n):
    element = int(input())
    sequence_list.append(element)

sequence_list = sorted(sequence_list,reverse=True)

for i in sequence_list:
    print(i, end=' ')