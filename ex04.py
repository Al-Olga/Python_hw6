# Создайте список из случайных чисел. 
# Найдите количество различных элементов в нем.

import random

list = []

print('Введите количество элементов: ')
n = int(input())
for _ in range(n):
    list.append(random.randint(0, 10))
print('Созданный массив чисел: ', list)

new_list = set(list)
print(f'список разных элементов: {new_list}')
print(f'В нем {len(new_list)} элементов')