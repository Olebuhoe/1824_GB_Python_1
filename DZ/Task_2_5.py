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

arr_prices.reverse()
for i in range(len(arr_prices)):
    _a = format(arr_prices[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')
print(id(arr_prices))

arr_prices.reverse()
for i in range(len(arr_prices) - 5, len(arr_prices)):
    _a = format(arr_prices[i], '.2f').split('.')
    print(f'{_a[0]} руб {_a[1]} коп', end=', ')
