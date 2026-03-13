#Задание 3.4
#1. Считать из параметров командной строки одномерный массив,
#состоящий из N целочисленных элементов.
#2. Вывести в консоль максимальный элемент массива и его
#порядковый номер.
#3. Вывести в порядке убывания все нечетные числа массива или
#сообщить, что таких чисел нет.

import sys
if len(sys.argv) < 2:
    print("Ошибка: Не переданы аргументы!")
    sys.exit(1)

# Создаем массив
arr = []
for i in range(1, len(sys.argv)):
    arr.append(int(sys.argv[i]))

# Выводим массив
print("Исходный массив:", arr)

# Находим максимальное значение и номер
max_value = arr[0]
max_index = 1
for i in range(1, len(arr)):
    if arr[i] > max_value:
        max_value = arr[i]
        max_index = i + 1

print("Максимальный элемент:", max_value)
print("Порядковый номер:", max_index)

# Находим и выводим нечетные числа
odd_numbers = []
for num in arr:
    if num % 2 != 0:
        odd_numbers.append(num)

if len(odd_numbers) == 0:
    print("Нечетных чисел нет")
else:
    odd_numbers.sort(reverse=True)
    print("Нечетные числа в порядке убывания:", odd_numbers)