# """Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел."""
# def func(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# func(1,2)
#
# """Функция на вход получает два произвольных числа. Вывести в консоль “yes”,
# если они отличаются друг от друга на 135, иначе вывести на экран “No”"""
# def func1(a, b):
#     if abs(a - b) == 135:
#         print("YES")
#     else:
#         print("NO")
# func1(1,136)
#
# """Функция на вход получает произвольное число
#  от 1 до 12 (номер месяца). Вывести название сезона
#   года в консоль (зима, весна, лето, осень)"""
# def func2(n):
#     if n in (1, 2, 12):
#         print("Winter")
#     elif n in (3, 4, 5):
#         print("Spring")
#     elif n in (6, 7, 8):
#         print("Summer")
#     else:
#         print("Autumn")
# func2(8)

# """Функция на вход получает
#  три произвольных числа. Если все числа больше 10,
#  то вывести на экран “yes”, иначе “no”;"""
#
# def func_3(a, b, c):
#     if a > 10 and b > 10 and c > 10:
#         print("Yes")
#     else:
#         print("No")
# func_3(14,11,15)

# """Функция на вход получает список, состоящий из
# 5 произвольных чисел. Найти количество положительных
#  чисел среди них."""
#
# def func4(a, b, c, x, y):
#     pos = 0
#     lst = [a, b, c, x, y]
#     for i in lst:
#         if i > 0:
#             pos += 1
#     print(pos)

#
# func4(1, 3, -5, 5, 0)

# """Функция на вход получает 2 переменные.
# Кол-во лет (int)
# Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.
# """
#
#
# def func_5(year, month):
#     days = 29
#     month = month + (year*12)
#     print(month*days)
#
#
# func_5(2, 5)


