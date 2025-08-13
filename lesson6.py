from re import compile, match  # re - regular expressions


# max_value = 10**10
# mask = '1?3948*5'
# divisor = 3013
# # ? -> одна цифра (\d), * -> любое колтчество цифр (\d*), ^ и $ - якоря начла и конца стоки

# def mask_matches(mask):
#     result = [] #Список подходящих чисел
#     regex_pattern = '^' + mask.replace('?', r'\d').replace('*', r'\d*') + '$'
#     compiled_pattern = compile(regex_pattern)
#     number = divisor
#     while number <= max_value:
#         if compiled_pattern.match(str(number)):
#             result.append(number)
#         number += divisor

#     print('Найденное число: ')
#     for num in result:
#         print(num)

# print(mask_matches(mask))


# knapsack(weights[], values[], W, n)
# weights - список веса вещей
# values  - список ценности вещей
# W - макс вес который выдержит рюкзак
# n - количество вещей
# длина values и weights должна совпадать
# нужно собрать максимальное количесвто ценных вещей в рюкзаке

# weights = [5, 1, 6, 8, 2]
# values = [100, 45, 63, 30, 13]


# def knapsack(weights, values, W, n):

#     items = {}
#     lst = []

# # Создаем словарь элементов
#     for i in range(n):
#         items[values[i]] = weights[i]
#         # print(items)

# # Преобразуем в лист кортежей
#     for key in items:
#         listik = []
#         listik.append(key)
#         listik.append(items[key])
#         listik = tuple(listik)
#         lst.append(listik)
#     print(f'lst do = {lst}')

# # Сортируем по ценности
#     for s in range(n):
#         for i in range(n - 1):
#             print(lst[i][0], lst[i+1][0])
#             if lst[i][0] > lst[i+1][0]:
#                 lst[i], lst[i + 1] = lst[i + 1],  lst[i]

# # Считаем суммарый вес предметов
#     summ_weight = 0
#     for tup in lst:
#         summ_weight += tup[1]
#     print("summ_weight", summ_weight)

# # Удаляем излишки
#     while summ_weight > W:
#         summ_weight -= lst[0][1]
#         lst.pop(0)
#     return lst


# def knapsack(weights, values, W, n):
#     if n == 0 or W == 0:
#         return 0
#     if weights[n - 1] > W:
#         return knapsack(weights, values, W, n - 1)
#     return max(values[n - 1] + knapsack(weights, values, W - weights[n - 1], n - 1),
#                knapsack(weights, values, W, n - 1))

# print(knapsack(weights, values, 20, 5))




# class Animal:
#     def __init__(self, name, weight, voice ):# Инициализация класса
#         #  атрибуты должны быть приватными
#         self.__name = name#Атрибут класса
#         self.__weight = weight#Атрибут класса
#         self.__voice = voice#Атрибут класса

#     def get_voice(self):# метод класса
#         print(f'{self.__name} says {self.__voice}')

# cat1 = Animal('cat', '5 kg', 'meow')
# cow = Animal('cow', '50 kg', 'moooo')
# cat1.get_voice()
# cow.get_voice()


# class Domestic(Animal):
#     def __init__(self, name, weight, voice):
#         super().__init__(name, weight, voice)

# goat = Domestic('GOAT', '40 kg', 'beee')
# goat.get_voice()
