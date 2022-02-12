"""
fizbaz.py

    Берем все числа от 1 до 100 включительно:
        - Если число делится на 3, то
        fizz
        - Если число делится на 5, то
        buzz
        - Если и на 3 и на 5, то
        fizzbuzz
"""

the_list = list()
for n in range(1, 101):
    the_list.append(n)

fizzbazz = list()
for i in range(0, 100, 15):
    fizzbazz.append(i)
fizzbazz.pop(0)

fizz = list()
for i in range(0, 100, 3):
    fizz.append(i)
fizz.pop(0)

bazz = list()
for i in range(0, 100, 5):
    bazz.append(i)
bazz.pop(0)

for element in the_list:
    if type(element) == int:
        if element in fizzbazz:
            the_list[the_list.index(element)] = 'fizzbazz'
        if element in fizz:
            the_list[the_list.index(element)] = 'fizz'
        if element in bazz:
            the_list[the_list.index(element)] = 'bazz'
    else:
        continue

print(the_list)