def summator():
    res = 0
    while True:
        numbers = input('Введите строку чисел, разделенных пробелом. x если хотите завершить программу: ').split()
        for i in numbers:
            if i == 'x':
                print(f'Итоговая сумма {res}.')
                return
            else:
                res += int(i)
        print(f'На данном этапе сумма равна: {res}')

summator()
