Вот расширенная версия многоязычного калькулятора с задержкой выхода 30 секунд:

```python
import math
import time

# Языковые настройки
languages = {
    'ru': {
        'welcome': 'Выберите операцию:',
        'operations': {
            '1': 'Сложение (+)',
            '2': 'Вычитание (-)',
            '3': 'Умножение (*)',
            '4': 'Деление (/)',
            '5': 'Возведение в степень (^)',
            '6': 'Квадратный корень (√)',
            '7': 'Факториал (!)',
            '8': 'Логарифм (log)',
            '9': 'Выход'
        },
        'choose_lang': 'Выберите язык (ru/en): ',
        'choose_op': 'Введите номер операции (1-9): ',
        'first_num': 'Введите первое число: ',
        'second_num': 'Введите второе число: ',
        'number': 'Введите число: ',
        'base': 'Введите основание логарифма (по умолчанию 10): ',
        'result': 'Результат: ',
        'error_num': 'Ошибка! Введите число.',
        'div_zero': 'Ошибка! Деление на ноль.',
        'sqrt_neg': 'Ошибка! Корень из отрицательного числа.',
        'fact_neg': 'Ошибка! Факториал отрицательного числа.',
        'log_neg': 'Ошибка! Логарифм от неположительного числа.',
        'goodbye': 'До свидания! Программа завершит работу через 30 секунд...'
    },
    'en': {
        'welcome': 'Choose operation:',
        'operations': {
            '1': 'Addition (+)',
            '2': 'Subtraction (-)',
            '3': 'Multiplication (*)',
            '4': 'Division (/)',
            '5': 'Power (^)',
            '6': 'Square root (√)',
            '7': 'Factorial (!)',
            '8': 'Logarithm (log)',
            '9': 'Exit'
        },
        'choose_lang': 'Choose language (ru/en): ',
        'choose_op': 'Enter operation number (1-9): ',
        'first_num': 'Enter first number: ',
        'second_num': 'Enter second number: ',
        'number': 'Enter number: ',
        'base': 'Enter logarithm base (default 10): ',
        'result': 'Result: ',
        'error_num': 'Error! Enter a number.',
        'div_zero': 'Error! Division by zero.',
        'sqrt_neg': 'Error! Square root of negative number.',
        'fact_neg': 'Error! Factorial of negative number.',
        'log_neg': 'Error! Logarithm of non-positive number.',
        'goodbye': 'Goodbye! Program will exit in 30 seconds...'
    }
}

def get_language():
    lang = input(languages["ru'"]["choose_lang"]).strip().lower()
    if lang not in languages:
        print("Неверный выбор языка! Будет использован русский.")
        return 'ru'
    return lang

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return languages[lang]['div_zero']
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return languages[lang]['sqrt_neg']
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        return languages[lang]['fact_neg']
    return math.factorial(int(x))

def logarithm(x, base=10):
    if x <= 0:
        return languages[lang]['log_neg']
    return math.log(x, base)

def main():
    global lang
    lang = get_language()
    
    print(f"\n{languages[lang]['welcome']}\n")
    for key, value in languages[lang]['operations'].items():
        print(f"{key}. {value}")

    while True:
        choice = input(languages[lang]['


