def delitel(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Деление на ноль запрещено'


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(delitel(a, b))
