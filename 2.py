# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
N = int (input('Введите длину массива '))
X = int (input('Какое число ищем? '))
arr = []
index = 0
for i in range(N):
    n = random.randint(2,7)
    arr.append(n)

res = abs(X - arr[0])
for i in range(1,N):
    temp = abs (X - arr[i])
    if temp < res:
        res = temp
        index = i 

print(arr)         
print(f'Ближайшее к искомому числу {X} - это {arr[index]}')




