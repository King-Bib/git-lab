def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("Деление на ноль невозможно")
    return a / b
def modulo(a, b):
    if b == 0: raise ValueError("Остаток от деления на ноль не определён")
    return a % b
def main():
    print("Учебный калькулятор: +, -, *, /, %")
    try:
        a = float(input("Первое число: ")); op = input("Операция: ").strip(); b = float(input("Второе число: "))
        operations = {"+": add, "-": subtract, "*": multiply, "/": divide, "%": modulo}
        if op not in operations: raise ValueError("Неизвестная операция")
        print("Результат:", operations[op](a, b))
    except ValueError as exc: print("Ошибка:", exc)
if __name__ == "__main__": main()
