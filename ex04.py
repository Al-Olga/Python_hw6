
import random

list = []

print('Введите количество элементов: ')
n = int(input())
for _ in range(n):
    list.append(random.randint(0, 10))
print('Созданный массив чисел: ', list)

list1 = set(list)
print(list1)