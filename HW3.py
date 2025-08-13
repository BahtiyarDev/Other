# дается список из слов, сосчитать все гласные буквы
# ['apple, 'pear''] => 4

# дается список из чисел нужно найти нехватающие [1,3,6 => 2, 4, 5]


# count = 0
# glasn = 'euioa'
# lst = ['applee', 'pear', 'orange']
# for word in lst:
#     # print(word)
#     for letter in word:
#         # print(letter)
#         if letter in glasn:
#             count += 1
#             # print(f'count = {count}')
# print(count)


# lst1 = [1, 3, 6, 10]
# lst2 = []
# for i in range(1, lst1[-1] + 1):
#     lst2.append(i)
# print(lst2)
# for i in lst1:
#     if i in lst2:
#         lst2.remove(i)
# print(lst2)


# ARRAY 1

# import array
# a = -1
# N = int(input("Введите число: "))
# array = array.array('i',[])
# for i in range(1, N+1):
#     a += 2
#     array.append(a)
# print(array)

# ARRAY 8
# N = int(input('Введите число N: '))
# lst = []
# K = 0
# for i in range(1, N+1):
#     lst.append(i)
# print(lst)
# for i in range(len(lst)):
#     if lst[i] % 2 == 0:
#         print(lst[i], end=' ')
#         K += 1
# print()
# print(f'Количество четных элементов - {K}')


# ARRAY 16

# N = int(input('Введите число N: '))
# A = []
# ind = -1
# lst1 = []
# lst2 = []
# for i in range(1, N+1):
#     A.append(i)
# print(A)
# for i in range(len(A) - 1):
#     if A[i] == A[ind]:
#         print(A[i])
#         break
#     if A[i] in lst2 or A[ind] in lst1:
#         break
#     lst1.append(A[i])
#     print(A[i], end=', ')
#     lst2.append(A[ind])
#     print(A[ind], end= ', ')
#     ind -= 1

# ARRAY 23

# sum = 0
# num = 0
# N = int(input("Введите число элементов N: "))
# K = int(input('Введите нижнюю границу K: '))
# L = int(input("Введите верхнюю границу L: "))
# lst = []
# for i in range(1, N+1):
#     lst.append(i)
# print(lst)
# for i in range(len(lst)):
#     if i in range(K-1, L):
#         pass
#     else:
#         print(f'{i} +')
#         sum += lst[i]
#         num +=1
# print(sum)
# sr_ar = sum / num
# print(f"Среднне арифметическое ряда равно = {sr_ar} ")


# ARRAY 52

# A = []
# B = []
# N = int(input("Введите число элементов N: "))

# for i in range(1, N+1):
#     A.append(i)

# for i in A:
#     if i < 5:
#         B.append(2*i)
#     else:
#         B.append(i/2)
# print(A)
# print(B)

# ARRAY 64

# A = []
# B = []
# C = []

# D = []

# Na = int(input("Введите Na: "))
# Nb = int(input("Введите Nb: "))
# Nc = int(input("Введите Nc: "))

# for i in range(1, Na + 1):
#     A.append(i)
# for i in range(1, Nb + 1):
#     B.append(i)
# for i in range(1, Nc + 1):
#     C.append(i)

# A = A[::-1]
# B = B[::-1]
# C = C[::-1]

# print(f'A - {A}')
# print(f'B - {B}')
# print(f'C - {C}')


# vib = max(Na, Nb, Nc)

# if Na == vib:
#     vib1 = A
#     vib2 = B
#     vib3 = C

# elif Nb == vib:
#     vib1 = B
#     vib2 = A
#     vib3 = C
# elif Nc == vib:
#     vib1 = C
#     vib2 = B
#     vib3 = A


# for i in vib1:
#     D.append(i)
#     if i in vib2:
#         D.append(i)
#         # print('vib2 +')
#     if i in vib3:
#         D.append(i)
#         # print('vib3 +')
# print(D)
