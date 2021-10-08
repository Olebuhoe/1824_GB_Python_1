"""
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на экран фразы вида: 'Привет,
Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду. Можно ли при
этом не создавать новый список?
"""
arr_prices = [86, 45.8, 21.56, 7.2, 56.3, 99.99, 2, 33.45, 15.6, 20.55, 3.45, 72.07]
for i in range(len(arr_prices)):
    _a = format(arr_prices[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')
print(id(arr_prices))

arr_prices.sort()
for i in range(len(arr_prices)):
    _a = format(arr_prices[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')
print(id(arr_prices))

from copy import copy
arr_prices_new = copy(arr_prices)
arr_prices_new.reverse()
for i in range(len(arr_prices_new)):
    _a = format(arr_prices_new[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')
print(id(arr_prices_new))

for i in range(len(arr_prices) - 5, len(arr_prices)):
    _a = format(arr_prices[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')

# не совсем понял поставленную задачу, поэтому второй вариант - из начального списка без форматирования:
print(sorted(arr_prices)[-5:])
