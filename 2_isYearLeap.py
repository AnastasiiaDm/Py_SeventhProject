'''
2. Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и
False иначе.
'''

def is_year_leap(year):
    if year == 365:
        print('Год высокосный:', False)

    else:
        print('Год высокосный:', True)


is_year_leap(366)