#Раздел 1. Работа с математическими операциями в Python
#2. Считать с клавиатуры три произвольных числа, вывести в консоль
#те числа, которые попадают в интервал [1, 50].

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

print("Числа, попадающие в интервал [1, 50]:")
if 1 <= num1 <= 50:
    print(num1)
if 1 <= num2 <= 50:
    print(num2)
if 1 <= num3 <= 50:
    print(num3)