# Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

# def given_point(d: int) -> float:
#     pi, sign, m = 3, 1, 2
#     while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
#         pi = pi + sign*4/(m**3+3*m**2+2*m)
#         sign = -1*sign
#         m = m+2
#     return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d)

# d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
# pi = given_point(d)
# print(f'С точностью {d=}, число {pi=}; ')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7

# number = int(input("Введите число: "))
# i = 2 
# list = []
# old = number
# while i <= number:
#     if number % i == 0:
#         list.append(i)
#         number //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {list}")

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# import random

# def number_list(n=20, min=10, max=99) -> list:
#     number_list = [random.randint(min, max)]
#     for i in range (1, n):
#         number_list.append(random.randint(min, max)) 
#     return number_list

# def values_list(user_list) -> list:
#     new_list = [user_list[0]]
#     for i in range(1, len(user_list)):
#         for j in range(len(new_list)):
#             if user_list[i] == new_list[j]:
#                 break
#             elif j == len(new_list)-1:
#                 new_list.append(user_list[i])
#     return new_list

# source_list = number_list(20, 10, 50)
# unique_list = values_list(source_list)
# print(f'{source_list} ->')
# print(unique_list)



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0 или 2*x^2 + 4*x + 5 = 0

# import random

# def write_file(st):
#     with open('file33.txt', 'w') as data:
#         data.write(st)

# def rnd():
#     return random.randint(0,101)

# def create_mn(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    
# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# koef = create_mn(k)
# write_file(create_str(koef))