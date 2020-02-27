def  my_func(x, y):
    return 1 / x ** abs(y)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(my_func(a, -b))

############################################

def my_func1(x, y):
    for i in range(abs(y + 1)):
        x *= x
    return float(1 / x)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

print(my_func1(a, -b))
