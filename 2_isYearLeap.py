'''
2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
False иначе.
'''


def is_year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print('Год высокосный:', False)
    else:
        print('Год высокосный:', True)


is_year_leap(2020)