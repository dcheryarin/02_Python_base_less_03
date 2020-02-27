def my_func(x, y, z):
    mass = [x, y, z]
    mass.remove(min(x, y, z))
    return sum(mass)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

print(my_func(a, b, c))
