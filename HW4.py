# Написать рекурсивную функци. для подсчета суммы цифр числа {например, sum_digits(123) = 6

# Найти первое/послженее вхождение элемента в отсортированном массиве с дубликатами
# [1,1,1,1,2,2,|2|,2,2,3,3,3,3]
# => (1) letf:0, right:2
# => (2) left: 3, right: 10
# Создать подобие кеша для сохранения данных



# 1
# def summa(numb):
#     if numb < 10:
#         return numb
#     return (numb % 10) + summa(numb // 10)
    
# print(summa(1))


# 2
# def binary_search(num, lst):
#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] > num:
#             right = mid - 1
#         elif lst[mid] <= num:
#             left = mid + 1
#     right_ind = right

#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] >= num:
#             right = mid - 1
#         elif lst[mid] < num:
#             left = mid + 1
#     left_ind = left
        
#     return left_ind, right_ind
# # 
# print(binary_search(3, [1,1,1,1,2,2,2,2,3,3,3,3]))

# 3

# cache = {}
# def fact(n):
#     if n == 1:
#         return n # Базовый случай
#     if n not in cache:
#         cache[n] = n * fact(n - 1)
#         return cache[n]
#     if n in cache:
#         return cache[n]
#     return -1
# print(fact(40), cache)


