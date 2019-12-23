# 1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
# быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
# (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".


def arithmetic (x, y, action):
    if action == '+':
        return x + y

    if action == '-':
        return x - y

    if '*' in action:
        return x * y

    if '/' in action:
        return x // y

    else:
        print('Unknown operation')


arithmetic(x=10, y=2, action='/')
