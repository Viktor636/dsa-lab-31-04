#Раздел 1. Работа с математическими операциями в Python
##целых чисел. Найти:
#i. Сумму всех чисел последовательности (решить задачу
#используя циклическую конструкцию while)
#ii. Количество всех чисел последовательности (решить задачу
#используя циклическую конструкцию while)

numbers = []

print("Введите целые числа:")

while True:
    value = input("Число: ")
    if value == "":
        break
    
    if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):
        numbers.append(value)
    else:
        print("Ошибка! Введите целое число.")

print("Введенные значения:", numbers)

# Подсчет суммы и количества
summ = 0
count = 0
while count < len(numbers):
    summ += int(numbers[count])
    count += 1
print("Сумма чисел:", summ)
print("Количество чисел:", len(numbers))