import time  # Импортируем модуль для работы со временем

# Получаем операцию от пользователя
start = input("What are you going to do? (*, +, -, /): ")

# Получаем числа от пользователя
try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
except ValueError:
    print("Error! Please enter valid numbers.")
    time.sleep(10)  # Задержка 10 секунд перед выходом
    exit()

# Выполняем операцию с проверкой
if start == "*":
    result = a * b
elif start == "+":
    result = a + b
elif start == "-":
    result = a - b
elif start == "/":
    if b == 0:
        print("Error! Division by zero is not allowed.")
        time.sleep(10)  # Задержка 10 секунд перед выходом
        exit()
    result = a / b
else:
    print("Error! Invalid operation.")
    time.sleep(10)  # Задержка 10 секунд перед выходом
    exit()

# Выводим результат
print(f"Result: {result}")
time.sleep(10)  # Задержка 10 секунд перед завершением программы
