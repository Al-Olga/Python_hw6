# "Пора учить английский язык", - сказал себе Степа 
# и решил написать программу для изучения английского языка. 
# Программа получает на вход слово на английском языке 
# и несколько его переводов на русском языке. Составьте словарь, 
# в котором ключ - это английское слово, а значение - это список русских слов. 
# В этой задаче нужно использовать строчный метод split()

n = int(input('Введите количество слов: '))
dict_translate = {}
for i in range(n):
    eng_rus = input(f'Введите строку {i+1}: ')
    list = eng_rus.split(' - ')
    dict_translate[list[0]] = list[1].split(', ')
print(dict_translate)