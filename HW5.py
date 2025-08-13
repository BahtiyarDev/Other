<<<<<<< HEAD
from random import *

# Быстрая сортировка
# берется рандомный элемент из массива
#  массив делится в 2 подмассива: меньше и больше этого числа

# O(nlogn) - лучший случай
# O(n^2) - худший случай

# Задача: написать рекурсивную функцию для подсчета шагов в гипотезе Коллатца
# Если четно: делить на 2
# Если нечетно: умножить на 3 и добавить 1
# Остановиться когда число станет 1\


# 1

# lst = [1,5,7,9,3,2,10,7,5,45]
# def fast_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     elif len(arr) > 1:
#         rand = choice(arr)
#         left = []
#         right = []
#         mid = []
#         for numb in arr:
#             if numb > rand:
#                 right.append(numb)
#             elif numb < rand:
#                 left.append(numb)
#             else:
#                 mid.append(numb)
#         return fast_sort(left) + mid + fast_sort(right)
# print(fast_sort(lst))

# 2

# def collatz(numb, count = 0):
#     print(numb)
#     print('count', count)
#     if numb == 1:
#         return count
#     if numb % 2 == 0:
#         return collatz(numb // 2, count + 1)
#     if numb % 2:
#         return collatz((numb * 3) + 1, count + 1)


# print(collatz(313213))
=======
from random import *

# Быстрая сортировка
# берется рандомный элемент из массива
#  массив делится в 2 подмассива: меньше и больше этого числа

# O(nlogn) - лучший случай
# O(n^2) - худший случай

# Задача: написать рекурсивную функцию для подсчета шагов в гипотезе Коллатца
# Если четно: делить на 2
# Если нечетно: умножить на 3 и добавить 1
# Остановиться когда число станет 1\


# 1

# lst = [1,5,7,9,3,2,10,7,5,45]
# def fast_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     elif len(arr) > 1:
#         rand = choice(arr)
#         left = []
#         right = []
#         mid = []
#         for numb in arr:
#             if numb > rand:
#                 right.append(numb)
#             elif numb < rand:
#                 left.append(numb)
#             else:
#                 mid.append(numb)
#         return fast_sort(left) + mid + fast_sort(right)
# print(fast_sort(lst))

# 2

# def collatz(numb, count = 0):
#     print(numb)
#     print('count', count)
#     if numb == 1:
#         return count
#     if numb % 2 == 0:
#         return collatz(numb // 2, count + 1)
#     if numb % 2:
#         return collatz((numb * 3) + 1, count + 1)


# print(collatz(313213))
>>>>>>> a4772715d9c8f3291065ab48cbbbadb055430e40
