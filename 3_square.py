'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
'''

def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal =  side * 1.41421
    # print('side:', side, '\nperimeter:', perimeter, '\narea:', area, '\ndiagonal:', diagonal)
    resultInTuple = perimeter, area, diagonal
    # print(type(resultInTuple))
    print(resultInTuple)


square(10)