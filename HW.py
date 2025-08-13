#ЗАДАНИЕ IF27

# x = float(input("Введите x: "))
# if x < 0:
#     f = 0
# elif x >= 0 and int(x) % 2 == 0:
#     f = 1
# else:
#     f = -1
# print(f)

#ЗАДАНИЕ IF29

# x = int(input("Введите x: "))
# if x < 0:
#     Znak = "Отрицательное"
# elif x > 0:
#     Znak = "Положительное"
# elif x == 0:
#     Znak = "Нулевое"

# if x%2 == 0:
#     Chet = "четное"
# elif x%2 != 0:
#     Chet = "нечетное"
# print(f"{x} - {Znak}, {Chet} число")

#ЗАДАНИЕ IF30

# x = int(input("Введите x: "))
# if x not in range(1, 1000):
#     print("Мы так не договаривались:( ")
# else:
#     if x%2 == 0:
#         Chet = "Четное"
#     elif x%2 != 0:
#         Chet = "Нечетное"
    
#     if x // 10 == 0:
#         Znach = "Однозначное"
#     elif x // 100 == 0:
#         Znach = "Двузначное"
#     elif x // 1000 == 0:
#         Znach = "Трехзначное"
#     print(f"{x} - {Chet}, {Znach} число")

#ЗАДАНИЕ FOR1

# K = int(input("Введите целое число: "))
# N =int(input("Введите колисество повторений: "))
# for i in range(1,(N + 1)):
    # print(K)

#ЗАДАНИЕ FOR2

# A = int(input("Введите меньшее число: "))
# B = int(input("Введите большее число: "))
# for i in range(A, (B + 1)):
#     print(i)
# N = int(((B - A)/1) + 1)
# print(f"Количество чисел - {N}")

#ЗАДАНИЕ FOR3
 
# List = []
# A = int(input("Введите меньшее число: "))
# B = int(input("Введите большее число: "))
# for i in range((A+1), B):
#     List.append(i)
# print(sorted(List, reverse = True))
# N = int(((B - A)/1) - 1)
# print(f"Количество чисел - {N}")

#ЗАДАНИЕ FOR12

# N = int(input("Введите целое число сомножителей: "))
# a = 1.1
# b = 1.2
# for i in range(1,N):
#     print(f"{a} * {b}")
#     a = a * b
#     b += 0.1
# print(round(a, 3))

#ЗАДАНИЕ FOR13
 
# N = int(input("Введите целое число слогаемых: "))
# a = 1.1
# b = 1.2
# for i in range(1,N):
#     a = a - b
#     b += 0.1
#     b = b * (-1)
# print(round(a, 3))

#ЗАДАНИЕ FOR19

# N = int(input("Введите целое число: "))
# a = float(1)
# b = float(2)
# for i in range(1,N):
#     a = a * b
#     b += 1
# print(f"{N}! = {a}")

#ЗАДАНИЕ FOR15

# A = int(input("Введите число: "))
# N = int(input("Введите степень числа: "))
# a = A
# for i in range(1, N):
#     a = a * A  
# print(f"{A}^{N} = {a}")

#ЗАДАНИЕ FOR16

# A = float(input("Введите число: "))
# N = int(input("Введите целую степень числа: "))
# n = 1
# for i in range(0, N):
#     result = A**n
#     print(round(result, 3))
#     n += 1

#ЗАДАНИЕ FOR17

# A = float(input("Введите целое: "))
# N = int(input("Введите целую степень числа: "))
# result = 1
# for i in range(1, (N + 1)):
#     result = result + (A**i)
# print(round(result, 3))

#ЗАДАНИЕ WHILE15

# vklad = 1000
# P = float(input("Введите процент по вкладу: "))
# K = 0 
# while vklad <= 1100:
#     vklad = vklad * (1 + (P/100))
#     K += 1
#     print(f"{K} месяц")
#     print(vklad) 

#ЗАДАНИЕ WHILE20

# N = int(input("Введите цeлое число: "))
# oform = N
# while True:
#     ost = N % 10
#     N = N // 10
#     if ost == 2:
#         print(f"В числе {oform} присутствует цифра '2' ")
#         break
#     elif N == 0:
#         print(f"В числе {oform} отстутствует цифра '2'  ")
#         break
#     else:
#         continue

# ЗАДАНИЕ WHILE24

# N = int(input("Введите предпологаемое число Фибоначчи: "))
# a = 0
# b = 1
# c = 0
# print(a)
# print(b)
# while True:
#     c = a + b
#     a = b
#     b = c
#     print(c)
#     if c == N:
#         print(f"{N} - число Фибоначчи")
#         break
#     elif c > N:
#         print(f"{N} - не число Фибоначчи")
#         break

# ЗАДАНИЕ WHILE26

# N = int(input("Введите число Фибоначчи: "))
# a = 0
# b = 1
# c = 0
# print(a)
# print(b)
# while True:
#     c = a + b
#     a = b
#     b = c
#     print(c)
#     if c == N:
#         print(f"{a}, {b}, {a + b} ")
#         break
#     elif c > N:
#         print(f"{N} - не число Фибоначчи")
#         break

# ЗАДАНИЕ WHILE30

# A = int(input("A = "))
# B = int(input("B = "))
# C = int(input("C = "))
# c1 = C
# c2 = C
# times = 2
# schet = 1
# count = 1
# if A <= 0 or B <= 0 or C <= 0:
#     print("Длинна стороны не может быть отрицательна! ")
# elif C > B or C > A:
#     print("Квадратов умещается 0")
# else:
#     while True:
#         C += c1
#         print(f"C = {C}")
#         if C > A:
#             times -= 1
#             print(f"times = {times}")
#             break
#         elif C == A:
#             print(f"times = {times}")
#         else:
#             times += 1
#         tm = times
#     while  True:
#         if c1 >= B:
#             print(f"schet = {schet}")
#             break
#         c1 += c2
#         schet +=1
        
#     while count < schet:
#         times += tm
#         count += 1
#     print(f"Количество квадратов - {times}")



# a = int(input("a = " ))
# b = int(input("b  = "))
# c =int(input("c = "))
# count = 0
# while  a >= c:
#     a -= c
#     count_width = 0
#     b_1 = b

#     while b_1 >= c:
#         b_1 -= c
#         count_width += 1

#     count += count_width
# print(f"В прямоугольнике {count} квадратов ")


    









