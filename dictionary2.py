# Пользователь вводит число N. Затем он вводит личные данные 
# (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

print('Введите количество друзей: ')
n = int(input())
dict_friends = []
min_age = 100
for i in range(n):
    friend = input(f'Введете имя друга {i+1}: ')
    age_friend = int(input(f'Введите возраст "{friend}": '))
    if age_friend < min_age:
        min_age = age_friend
    dict_friends.append({'name': friend, 'age': age_friend})

for dict in dict_friends:
    if dict['age'] == min_age:
        print(f"У друга {dict['name']} самый маленький возраст = {min_age}")
        break