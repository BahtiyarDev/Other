from functools import lru_cache

# lru - least recent unit - один из вариантов оптимизации кода

# Big - O - сложности обрабокти кода

# -----------------------------------
# O(1) - константная сложность(не занимает производительность)
# lst = [1, 3, 5]
# first = lst[0]
# -----------------------------------
# O(log2 n) - логарифмиеская сложность(занимает в 2 раза меньше меньше производительности пропорционально числе n)


def binary_search(num, lst):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == num:
            return mid
        elif lst[mid] >= num:
            right = mid - 1
        elif lst[mid] <= num:
            left = mid + 1
    return -1


print(binary_search(1, [1, 2, 3, 4, 5, 6, 7]))


# -----------------------------------
# O(n) - линейная сложность(занимает производительность пропорционально числе n)
# def search(num, lst):
#     for i in range(len(lst)):
#         if (lst[i] == num):
#             return i
#     return -1
# a =search(5, [2, 3, 4, 6, 5])
# print(a)

# -----------------------------------
# O(nlogn) - линейно логарифмическа сложность(занимает производительность в произведнии с O(n) + O(logn))

# def binary_search(num, lst):
#     left, right = 0, len(lst) - 1
#     for i in range(0, len(lst) - 1):
#         mid = (left + right) // 2
#         # print(mid)
#         if lst[mid] == num:
#             return mid
#         elif lst[mid] >= num:
#             right = mid - 1
#         elif lst[mid] <= num:
#             left = mid + 1
#     return -1


# -----------------------------------
# O(N!) - факториальная сложность(занимает производительность пропорционально факториалу n)

# Рекурентные функции содержат две основные части:1)Базовый случай 2) Рекурсивный случай

# @lru_cache
# def fact(n):
#     if n == 1:
#         return n # Базовый случай
#     return n * fact(n - 1)

# print(fact(5))

# -----------------------------------
# O(n^2) - кваратичная сложность(увеличивается порпорционально квадрату числа n)

# # [1,6,2,5,10]
# # buble sort - пузырьковая сортировка
# def bubule_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr) - 1):
#             print(arr[j], arr[j+1])
#             if arr[j] > arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     return arr


# print(bubule_sort([1,6,2,5,10]))

# -----------------------------------
# O(n) + O(n) = O(2n) => O(n) - коэффиценты игнорятся
# O(2*10) + O(2*50) - та же линейная сложность

# for i in range(0, num):
#     print(i)

# for i in range(0, num):
#     print(i)

# -----------------------------------
# O(2^n) - экспоеннциальная сложность(пропорциональна значению 2 в степени числа n)
#


# Кэширование
# @lru_cache
# def fib(num):
#     if num <= 1:
#         return num
#     else:
#         return fib(num - 1) + fib(num - 2)

# print(fib(40))

# Табуляция
# def tab_fib(num):
#     a, b = 0, 1
#     for _ in range(num):
#         a, b = b, a+b
#     return a

# O(n)

# Сортировкка слиянием
# 1 нужно поделить массив на подмассивы(и так пока не останется 2элемента в подмассивах)
# 2 нужно сравнить числа и объединить их в один массив оп порядку

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]

#         merge_sort(left)
#         merge_sort(right)

#         i, k, j = 0, 0, 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#     # добавляем остатки
#         while i < len(left):
#             arr[k] = left[i]
#             i+= 1
#             k+=1
#         while j < len(right):
#             arr[k] = right[j]
#             j+= 1
#             k+=1
#     return arr


# O(n) * O(logn) = O(nlogn)


