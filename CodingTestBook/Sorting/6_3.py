# Chapter 6 
# <3> 성적이 낮은 순서로 학생 출력하기
import sys 

n = int(input())

array_sequence = []

for i in range(n):
    read = sys.stdin.readline().split()
    array_sequence.append((read[0],int(read[1])))

array_sequence = sorted(array_sequence, key=lambda student_info : student_info[1])

for i in array_sequence:
    print(i[0], end=' ')