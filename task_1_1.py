duration = int(input('Ведите количество секунд: '))
sec_in_day = 24 * 60 * 60
sec_in_hour = 60 * 60
sec_in_min = 60

day = duration // sec_in_day
hour = (duration - day * sec_in_day)// sec_in_hour
min = (duration - day * sec_in_day - hour * sec_in_hour) // sec_in_min
sec = duration - day * sec_in_day - hour * sec_in_hour - min * sec_in_min

if day == 0 and hour > 0:
    print(f'Такое количество секунд содержится в {hour} час {min} мин {sec} сек')
elif day == 0 and hour == 0 and min > 0:
    print(f'Такое количество секунд содержится в {min} мин {sec} сек')
elif day == 0 and hour == 0 and min == 0:
    print(f'Такое количество секунд содержится в {sec} сек')
else:
    print(f'Такое количество секунд содержится в {day} дн {hour} час {min} мин {sec} сек')