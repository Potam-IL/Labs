while True:
    try:
        a = float(input('Введите числовое значение для a: '))
        break
    except ValueError:
        print("Введите числовое значение пожалуйста")
while True:
    try:
        b = float(input('Введите числовое значение для b: '))
        while not b:
            print('Введите число, отличное от 0! ')
            b = float(input('Введите числовое значение для b: '))
        break
    except ValueError:
        print("Введите числовое значение пожалуйста")
sum = a + b
raz = a - b
mult = a * b
div = a / b
#div = round(a / b, 2)
print(f'Сумма числа {a} и числа {b} равна {sum}\n')
print(f'Разность числа {a} и числа {b} равна {raz}\n')
print(f'Произведение числа {a} и числа {b} равна {mult}\n')
print(f'Результат деления числа {a} на {b} равен {div:.3}\n')
