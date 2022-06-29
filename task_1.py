"""Дано два списки чисел. Порахуйте, скільки чисел міститься як у першому списку, і у другому. (set)"""
from random import randint

first_list = [randint(0, 99) for i in range(randint(10, 50))]
second_list = [randint(0, 99) for j in range(randint(10, 50))]

print(f'Кількість елементів які є в обох списках: {len(set(first_list) & set(second_list))}')
