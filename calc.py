op = input("language язык? en ru")
if op == en: start = input("what are you gonna doing? * + - /")
a = float(input("1 number"))
b = float(input("2 number"))
if start == "*": result = a * b
elif start == "+": result = a + b
elif start == "-":result = a - b
elif start == "/":result = a / b
else:
print("wrong!")
exit()
print(result)