lst = []
for i in range(1, 1001):
    if i % 2 != 0:
        lst.append(i ** 3)
print(lst)

def sum_of_num(number):
    sum = 0
    while number != 0:
        sum = sum + number % 10
        number = number // 10
    return sum

sum = 0
for i in lst:
    if sum_of_num(i) % 7 == 0:
        sum += i
print(sum)

# Вариант с созданием нового списка
lst_new = []
sum = 0
for i in lst:
    lst_new.append(i + 17)
print(lst_new)

sum = 0
for i in lst_new:
    if sum_of_num(i) % 7 == 0:
        sum += i
print(sum)

# Вариант без создания нового списка
sum = 0
for i in lst:
    new_elem = i + 17
    if sum_of_num(new_elem) % 7 == 0:
        sum += new_elem
print(sum)