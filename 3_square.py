'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью
кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
'''


def square(side):
    perimeter = side * 4
    area = side ** 2
    diagonal = side * 1.41421
    result_in_tuple = perimeter, area, diagonal
    return result_in_tuple


square(10)
