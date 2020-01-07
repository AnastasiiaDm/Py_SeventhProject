'''
4. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень).
'''

def season(monthNum):
    winter = 1, 2, 12
    spring = 3, 4, 5
    summer = 6, 7, 8
    autumn = 9, 10, 11

    if monthNum in winter:
        return str('Winter')

    if monthNum in spring:
        return str('Spring')

    if monthNum in summer:
        return str('Summer')

    if monthNum in autumn:
        return str('Autumn')

'''Enter int in range 1-12'''
season(1)

