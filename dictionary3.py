# Пользователь вводит число N. Затем он вводит личные данные 
# (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя

print('Введите количество друзей: ')
n = int(input())
dict_friends = []
for i in range(n):
    friend = input(f'Введете имя друга {i+1}: ')
    age_friend = int(input(f'Введите возраст "{friend}": '))
    dict_friends.append({'name': friend, 'age': age_friend})
sum_age = 0
max_name = dict_friends[0]['name']
for dict in dict_friends:
    sum_age += dict['age']
    if len(dict['name']) > len(max_name):
        max_name = dict['name']
print(f'Средний возраст друзей: {sum_age / n}')
print(f'Самое длинное имя: {max_name}')