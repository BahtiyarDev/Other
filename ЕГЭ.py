# def ege5():
#     schetchik = 0
#     for N in range(100, 3001):
#         lst = []
#         result = 0
#         print(N)
#         n = N
#         nk = N
#         while True:
#             ost = nk % 2
#             nk = nk // 2
#             lst.append(ost)
#             if nk // 2 == 0:
#                 ost = nk % 2
#                 lst.append(ost)
#                 sorted_lst = lst[::-1]
#                 # print(sorted_lst)
#                 break
#         sorted_lst.pop(0)
#         # print(sorted_lst)

#         # Удаление первой единицы и нулей после неё
#         while True:
#             count = len(sorted_lst)
#             if count == 0:
#                 break
#             elif sorted_lst == 0:
#                 sorted_lst.pop(0)
#             else:
#                 break
#         # Подсчет элементов в списке
#         # print(sorted_lst)
#         count = len(sorted_lst)
#         print(f"count = {count}")

#         if count == 0:
#             result = 0
#         else:
#             # Перевод в десятичную запись
#             for i in sorted_lst:
#                 # print(i)
#                 res = i * 2**(count - 1)
#                 # print(f"{i} * 2^{count - 1} = {res}")
#                 count -= 1
#                 result += res
#             # print(result)

#             vichet = n - result
#             # print(f"Результат = {vichet}")
#         schetchik +=1
#         print(f"schetchik = {schetchik}")
#     return schetchik
# a = ege5()
# print(a)


# a = []
# for x in range(100, 3001):
#     i = int(bin(x)[3:], 2)
#     if x - i not in a:
#         a.append(x-i)
# print(len(a))

# def zad5():
#     for N in range(0, 256):
#         lst = []
#         binar = '{:08b}'.format(N)
#         # print(binar)
#         for i in binar:
#             if i == '0':
#                 lst.append('1')
#             elif i == '1':
#                 lst.append('0')
#             # print(lst)
#         mod_binar = ''
#         for i in lst:
#             mod_binar += i
#             # print(mod_binar)
#         dec_numb = int(mod_binar, 2)
#         # print(dec_numb)
#         otv= dec_numb - N
#         # print(f'Получислось число = {otv}')
#         if otv == 133:
#             # print(f'Ответ = {N}')
#             break
#     return N
# otv = zad5()
# print(otv)

# string = ''
# for i in range(1, 78):
#     string += '1'
# while '11' in string:
#     if '222' in string:
#         string = string.replace('222', '1', 1)
#     else:
#         string = string.replace('11', '2', 1)
#     print(string)


# numb = (4**225) + (2**255) - 255
# binar = bin(numb)
# print(binar)
# count = binar.count('1')
# print(f'Count = {count}')
# F = 1
# n = int(input("Ввдеите число: "))
# for i in range(2, n+1):
#     F = F + i
#     print(F)

# lst = []
# f = open('17.txt', 'r')
# for i in f:
#     lst.append(i)
# # print(lst)
# lst = [item.replace('\n', '') for item in lst]
# # print(lst)
# int_lst = list(map(int, lst))
# print(int_lst)


# dec_numb = int(input("Введите число: "))
# print("{:x}".format(dec_numb))
# dec = 0

# for N in range(1, 200):
#     dec = 0
#     binar = '{:b}'.format(N)
#     print(binar)
#     sum = 0
#     for i in binar:
#         sum += int(i)
#     if sum % 2 == 0:
#         binar += '00'
#     else:
#         binar += '11'

#     dec = int(binar, 2)
#     if dec > 114:
#         print(dec)
#         break


# string = '1' + '8'*99 + '1'
# while '81' in string or '8883' in string or '882' in string:
#     if '81' in string:
#         string = string.replace('81', '2', 1)
#     elif '882' in string:
#         string = string.replace('882', '3', 1)
#     else:
#         string = string.replace('8883', '1', 1)
# print(string)


def seti(*perevods):
    otv = ''
    for i in perevods:
        binar = bin(i)[2:]
        otv += (binar + '.')
    return otv


# def F(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         return F(n - 1) + n
#     elif n > 1 and n % 2 != 0:
#        return  2 * F(n - 2)

# print(F(26))


# file = open('17 (3).txt', 'r')
# posled = []
# for line in file:
#     posled.append(int(line))
# file.close()
# print(posled)

# nechet = []
# for nech in posled:
#     if nech % 2 != 0:
#         nechet.append(nech)
# # print(nechet)
# counter = 0
# summ = 0
# count = 0
# max = 0
# for nech in nechet:
#     summ += nech
#     count += 1
# sr_ar = summ / count
# #

# for i in range(len(posled) - 1):
#     usl1 = posled[i] % 5 == 0 and posled[i+1] < sr_ar
#     usl2 = posled[i + 1] % 5 == 0 and posled[i] < sr_ar
#     if usl1 or usl2:
#         counter += 1
#         if (posled[i] + posled[i + 1]) > max:
#             max = (posled[i] + posled[i + 1])
# print(counter, max)


# file = open('1_17.txt', 'r')
# posled = []
# for line in file:
#     posled.append(int(line))
# file.close()


# max2 = 0
# maxsum = 0
# count = 0
# a =[]
# for znach in posled:
#     if znach // 10 != 0 and znach // 100 == 0:
#         if znach > max2:
#             max2 = znach


# for i in range(len(posled) - 1):
#     usl1 = (10 <= posled[i] <= 99 ) and (posled[i + 1] not in range(10, 100))
#     usl2 = (posled[i] not in range(10, 100)) and (10 <= posled[i + 1] <= 99 )
#     if usl1 or usl2:
#         if (posled[i] + posled[i + 1]) %  max2 == 0:
#                 count += 1
#                 if posled[i] + posled[i + 1] > maxsum:
#                      maxsum = posled[i] + posled[i + 1]
# print(count, maxsum)


# file = open('17 (2).txt', 'r')
# posled = []
# for line in file:
#     posled.append(int(line))
# file.close()

# count = 0
# min = 10000
# maxsum = 0
# for numb6 in posled:
#     if str(numb6)[-1]  == '6' and numb6 < min:
#         min = numb6
# print(min)

# for i in range(len(posled) - 1):
#     usl1 = str(posled[i])[-1] == '6' and str(posled[i + 1])[-1] != '6'
#     usl2 = str(posled[i + 1])[-1] == '6' and str(posled[i])[-1] != '6'
#     usl3 = (posled[i]**2  +  posled[i + 1]**2) < min**2
#     if (usl1 or usl2) and usl3:
#         count += 1
#         if (posled[i]**2  +  posled[i + 1]**2) > maxsum:
#             maxsum = (posled[i]**2  +  posled[i + 1]**2)
# print(count, maxsum)


# def func(n):
#     first_part = int(str(n)[0]) + int(str(n)[1])
#     second_part = int(str(n)[2]) + int(str(n)[3])
#     if first_part <= second_part:
#         result = str(first_part) + str(second_part)
#     elif first_part > second_part:
#         result = str(second_part) + str(first_part)
#     return result

# # print(func(2366))

# # count = 0

# for i in range(9999, 999, -1):
#     otv = func(i)
#     if otv == '117':
#         print(i)
#         break
# # print(count)


# def zam(string):
#     while '01' in string or '02' in string or '03' in string:
#         string = string.replace('01', '103', 1)
#         string = string.replace('02', '10', 1)
#         string = string.replace('03', '210', 1)
#     return string.count('2'), string
# string = '0' + 12*'1' + 15*'2' + 17*'3'
# print(zam(string))

# print(seti(255, 255, 254, 0))
# x = 0
# num = 1
# while num % 133 != 0:
#     num = 2 * 18*3 + 8 * 18**2 + x * 18 + 2 + 9 * 12**3 + 3 * 12**2 + x * 12 +5
#     x += 1
#     print(num)

# sum = 0
# def zam(string):
#     while '11' in string:
#         string = string.replace('112', '6', 1)
#         string = string.replace('1', '3', 1)
#     return string
# string =  10*'1' + 3*'2'
# a = zam(string)
# print(zam(string))

# for i in a:
#     sum += int(i)
# print(sum)


# print(seti(206, 158, 124, 67))
# 11111111.11111111.1111110.0000000
# 11001110.10011110.1111100.1000011

# print(int('01000011', 2))
# x = 1

# while True:
#     num = x * 14**3 + (1 * 14**4 + 5 * 14**2 + 6 * 14 + 3) + x * 14 + (8 * 14**4 + 7 * 14**3 + 1 * 14**2 + 3)
#     print(num)
#     if num % 24 == 0:
#         print(f'otv = {num / 24}')
#         break
#     x+=1

# count = 0
# def F(n):
#     if n == 0:
#         return 0
#     elif n > 0 and n % 2 == 0:
#         return F(n/2)
#     elif n % 2 != 0:
#         return 1 + F(n - 1)

# for n in range(1, 501):
#     a = F(n)
#     print(a)
#     if a == 8:
#         count += 1
# print(count)


# file = open('17 (4).txt', 'r')
# lst = []
# for line in file:
#     lst.append(line)

# count = 0
# minim = 10000
# maxsum = 0

# for i in range(len(lst) - 1):
#     if lst[i][-2] == lst[i][-3]:
#         if int(lst[i]) < minim:
#             minim = int(lst[i])
# print(minim)


# for i in range(len(lst) - 1):
#     usl1 = (lst[i][-2] == lst[i + 1][-3]) or (lst[i + 1][-2] == lst[i][-3])
#     usl2 = (int(lst[i]) % 7 == 0 and int(lst[i + 1]) % 7 != 0) or (int(lst[i + 1]) % 7 == 0 and int(lst[i]) % 7 != 0)
#     usl3 = (int(lst[i])**2 + int(lst[i+1])**2) <= minim**2
#     if usl1 and usl2 and usl3:
#         count += 1
#         if (int(lst[i])**2 + int(lst[i+1])**2) > maxsum:
#             maxsum = (int(lst[i])**2 + int(lst[i+1])**2)
# print(count, maxsum)


# def f(x,y):
#     if x > y or x == 17:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return f(x + 1, y) + f(x * 2, y)
# print(f(1, 10) * f(10, 21))


# def func(n):
#     first_part = int(str(n)[0]) + int(str(n)[1])
#     second_part = int(str(n)[1]) + int(str(n)[2])
#     if first_part >= second_part:
#         result = str(first_part) + str(second_part)
#     elif first_part < second_part:
#         result = str(second_part) + str(first_part)
#     return result

# print(func(395))
# otv = 0
# for n in range(100, 1000):
#     otv = func(n)
#     if otv == '1412':
#         print(n)
#         break

# def zam(string):
#     while '111' in string:
#         string = string.replace('111', '22', 1)
#         string = string.replace('222', '11', 1)
#     return string.count('1')
# # print(zam(string))

# min = 100

# for n in range(101, 1001):
#     string = '1' * n
#     count = zam(string)
#     if count < min:
#         min = count
#         otv = n
# print(otv)


# print(seti(112))


# # 11111111.11111111.11111000.00000000
# # 1110000.10011010.10000101.11010000

# print(int('10111010000', 2))

# def F(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1
#     if n > 3:
#         return F(n - 3) + F(n - 2) + F(n - 1)
# print(F(9))

# lst = []
# file = open('1_17 (1).txt', 'r')
# for line in file:
#     lst.append(int(line))

# maxsum = 0
# max2 = 0
# count = 0

# for num in lst:
#     if num in range(10, 100):
#         if num > max2:
#             max2 = num

# print(max2)

# for i in range(len(lst) - 1):
#     usl1 = (lst[i] in range(10, 100) and lst[i + 1] not in range(10, 100)) or (lst[i+1] in range(10, 100) and lst[i] not in range(10, 100))
#     usl2 = (lst[i] + lst[i+1]) % max2 == 0
#     if usl1 and usl2:
#         count += 1
#         if (lst[i] + lst[i+1]) > maxsum:
#             maxsum = (lst[i] + lst[i+1])
# print(count, maxsum)


# def func(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return func(x + 2, y) + func(x * 2, y) + func(x + 3, y)
# print(func(2, 11) * func(11, 22))


# file = open('24 (1).txt', 'r')
# a = file.readline()
# file.close()

# left = 0
# countm = 0
# count = 0

# for right in range(len(a) - 1):
#     if  a[right] == 'W' and a[right + 1] == 'W':
#         count += 1
#     if count == 100:
#         dlin = right - left + 2
#         if dlin > countm:
#             countm = dlin
#     elif count > 100:
#         while count != 100:
#             if a[left] == 'W' and a[left + 1] == 'W':
#                 count -= 1
#             left += 1
# print(countm)


# def func(numb):
#     lst = []
#     first_part = int(str(numb)[0]) + int(str(numb)[1])
#     second_part = int(str(numb)[1]) + int(str(numb)[2])
#     third_part = int(str(numb)[2]) + int(str(numb)[3])
#     print(first_part, second_part, third_part)
#     lst.append(first_part)
#     lst.append(second_part)
#     lst.append(third_part)
#     lst = sorted(lst)
#     print(lst)

#     otv = str(lst[-2]) + str(lst[-1])
#     return otv

# # print(func(9575))


# for n in range(9999, 999, -1):
#     result = func(n)
#     if result == '1517':
#         print(n)
#         break


# def zam(string):
#     while '01' in string or '02' in string or '03'in string:
#         string = string.replace('01', '20', 1)
#         string = string.replace('02', '120', 1)
#         string = string.replace('03', '302', 1)
#     return string.count('1')

# string = '0' + 12*'1' + 15*'2' + 17*'3'
# print(zam(string))

# def f(n):
#     if n == 1:
#         return 1
#     if n>1:
#         return f(n-1) * (n+1)

# print(f(4))

# def func(x,y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return func(x+1, y) + func(x * 2, y) + func((2 * x) + 1, y)

# print(func(2, 16))


# file = open('1_24.txt', 'r')
# a = file.readline()
# file.close()

# max = 1
# count = 1

# for i in range(len(a) - 1):
#     if a[i] not in 'ABC' or a[i + 1] not in 'ABC':
#         count +=1
#         if count > max:
#             max = count
#     else:
#         count = 1
# print(max)

# del3013 = []
# otv = 0
# n = 1

# while otv < 10**10:
#     otv = 3013 * n
#     del3013.append(otv)
#     n += 1
#     if del3013[-1] > 10**10:
#         del3013.pop()
# del3013 = set(del3013)

# mask = set()

# for i in range(0, 10):
#     for j in range(0,1000):
#         numb = '1' + str(i) + '3948' + str(j) + '5'
#         mask.add(int(numb))
#         numb = 1
# # print(mask)

# if 1039485 in mask:
#     print('+')
# # print(mask & del3013


# a = (3 * 4**38)+(2 * 4**23)+(4**20)+(3*4**5)+(2*4**4)+1
# print('{:x}'.format(a).count('0'))


# from functools import lru_cache

# @lru_cache(maxsize=None)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1 and n % 2:
#         return F(n - 2) * 3
#     else:
#         return 2*n * F(n-1) + F(n-3)

# print(F(2026)//F(2021))


# def F(x, y):
#     if x > y or x == 13:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return F(x+1, y) + F(x+2, y) + F(3*x, y)


# print(F(1, 10) * F(10, 15))

# from re import compile, match

# mask = '3?1*57'
# divisor =  1991
# max_znach = 10**8
# result ={}


# pattern = '^' + mask.replace('?', r'\d').replace('*', r'\d*') + '$'
# compiled_pattern = compile(pattern)

# num = divisor

# while num <= max_znach:
#     if compiled_pattern.match(str(num)):
#         result[num] = num // divisor
#     num += divisor

# print(result)


# file = open('26.txt', 'r')
# lst = []
# num = ''
# listik = []


# for line in file:
#     for letter in line:
#         num += letter
#         if letter == ' ':
#             print('num', num)
#             listik.append(num)
#             num = ''

#         if letter == '\n':
#             listik.append(num)
#             num = ''
#         # print(letter)
#         if len(listik) == 2:
#             lst.append(tuple(listik))

# print(lst)


# for line in file:
#     lst.append(line.replace('\n', '', 1))
#     for j in line:
#         print(j)
# # print(lst)


# List = []
# num = ''
# listik = []
# lst = ['1234 5678', '54667 1231']
# for el in lst:
#     print('el=', el)
#     for letter in el:
#         print(letter)
#         num += letter
#         if letter == ' ':
#             print('+')
#             listik.append(int(num))
#             num = ''
#             continue
#         if len(listik) == 2:
#             print('++')
#             List.append(tuple(listik))
#             listik.clear()


# print(List)


# alph = '0123456789ABCDEF'


# for x in alph:
#     vir1 = ('1' + x + 'BAD')
#     vir2 = ('2C' + x + 'FE')
#     vir = int(vir1, 16) + int(vir2, 16)
#     if vir % 15 == 0:
#         print(x)
#         print(vir//15)


# def F(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     if n == 3:
#         return 1
#     else:
#         return F(n-3) + F(n-2) + F(n-1)

# print(F(9))


# lst = []

# file = open('17 (5).txt', 'r')
# for line in file:
#     lst.append(int(line))
# file.close()


# maxsum = 0
# count = 0

# for i in range(len(lst) - 1):
#     for j in range(i+1, len(lst)):
#         if (lst[i] + lst[j]) % 120 == 0:
#             count += 1
#             if (lst[i] + lst[j]) > maxsum:
#                 maxsum = lst[i] + lst[j]

# print(count, maxsum)


# dec = 16**4 + 8**4 + 4**6 - 64
# print('{:b}'.format(dec).count('1'))


# def F(n):
#     if n == 1:
#         return 0
#     else:
#         return F(n-1) + n


# def G(n):
#     if n == 1:
#         return 1
#     else:
#         return G(n-1)*n

# print(F(5) + G(5))


# lst = []
# file = open('17 (6).txt', 'r')
# for line in file:
#     lst.append(int(line))
# file.close()

# maxsum = 0
# count = 0

# for i in range(len(lst) - 1):
#     usl1 = (lst[i]*lst[i+1]) % 15 == 0
#     usl2 = (lst[i]+lst[i+1]) % 7 == 0
#     if usl1 and usl2:
#         count+=1
#         maxsum = max(lst[i]+lst[i+1], maxsum)

# print(count, maxsum)


# def func(x, y):
#     if x > y:
#         return 0
#     if x == y:
#         return 1
#     else:
#         return func(x+1, y) + func(x*3, y)

# print(func(3, 33))


# def F(n):
#     if n <= 10:
#         return n
#     if 10<n<=36:
#         return n//4 + F(n-10)

# print(F(18))


# file = open('24 (3).txt', 'r')
# string = file.readline()
# file.close()


# def count_len(str):
#     maxlen = 0
#     for i in range(len(string) - 1):
#         for j in range(1, len(string) - 1):
#             if string[i] == string[j]:
#                 if (i - j + 1) > maxlen:
#                     maxlen = i - j + 1
#     return maxlen


# print(count_len(string))

# dct = {}
# maxlen = 0

# for i, char in enumerate(string):
#     if char not in dct:
#         dct[char] = i

#     elif char in dct:
#         if (i - dct[char] + 1) > maxlen:
#             maxlen = (i - dct[char] + 1)
#             dct.clear()

# print(maxlen)

# file = open('24 (4).txt', 'r')
# string = file.readline()
# file.close()

# count_usl = 0
# maxlen = 0
# left = 0

# for i in range(0, len(string), 1):
#     if string[i] in 'BCDF' and string[i+1] in 'AE':
#         count_usl += 1

#     if string[i] not in 'BCDF' or string[i+1] not in 'AE':
#         string[i+1] 


#     if count_usl == 130:
#         right = i
#         res = right - left + 1
#         count_usl = 0
#         left = right + 1
#         if res > maxlen:
#             maxlen = res

    

# file = open('24 (3).txt', 'r')
# string = file.readline()
# file.close()
# string = 'A123456789B987654321A'
# maxlen = 0
# left = 0
# right = 1


# while right <= (len(string) - 1):
#     # print(f'left = {left}')
#     # print(f'right = {right}')
#     if string[left] == string[right]:
#         # print(left, right)
#         length = right - left + 1
#         # print(length)
#         maxlen = max(maxlen, length)
#         left += 1
#         right = left + 1

#     else:
#         right += 1

    
# print(maxlen)