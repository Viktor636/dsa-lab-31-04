#Раздел 1. Работа с математическими операциями в Python
#1. Считать с клавиатуры три произвольных числа, найти минимальное
#среди них и вывести на экран.

num1 = input("Число 1: ")
while not num1.replace('.', '').replace('-', '').isdigit():
    print("Ошибка! Введите число.")
    num1 = input("Число 1: ")
num1 = float(num1)

num2 = input("Число 2: ")
while not num2.replace('.', '').replace('-', '').isdigit():
    print("Ошибка! Введите число.")
    num2 = input("Число 2: ")
num2 = float(num2)

num3 = input("Число 3: ")
while not num3.replace('.', '').replace('-', '').isdigit():
    print("Ошибка! Введите число.")
    num3 = input("Число 3: ")
num3 = float(num3)

min_number = min(num1, num2, num3)
print(f"Минимальное число: {min_number}")