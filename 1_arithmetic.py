# 1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна
# быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить
# (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(x, y, action):
    if action == '+':
        print(x + y)
        return

    if action == '-':
        print(x - y)
        return

    if '*' in action:
        print(x * y)
        return

    if '/' in action:
        print(x // y)
        return

    else:
        print('Unknown operation')


arithmetic(x=10, y=2, action='/')
