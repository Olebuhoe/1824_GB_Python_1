for i in range(1, 101):
    ending = ['а', 'ов']
    if i % 10 == 1 and i != 11:
        print(f'{i} процент')
    elif (i % 10 == 2 or i % 10 == 3 or i % 10 == 4) and i not in range(12, 15):
        print(f'{i} процент{ending[0]}')
    else:
        print(f'{i} процент{ending[1]}')