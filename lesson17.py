# lambda arguments: expression

# a = lambda x: x**2
# print(a(2))


# Функции высшего порядка(HOF) - функции, принимающие в аргументах другую функцию

# map - неявный цикл, принимающий два аргумента:
# 1) выражение которое мы должны выполнить
# 2) каждого элемента во втором аргументе(list, tuple)

# lst = [1,2,3,4,5,6,7]
# added1 = list(map(lambda x: x+1, lst))
# print(added1)


# filter - неявный цикл, принимает два аргумента:
# 1) выражение которое(должно возвращать будевое значение) мы должны выполнить
# 2) каждого элемента во втором аргументе(list, tuple)

# lst = [1,2,3,4,5,6,7]
# odd_numbers = list(filter(lambda x: x%2 != 0, lst))
# even_numbers = list(filter(lambda x: x%2 == 0, lst))
# print(odd_numbers)
# print(even_numbers)


# sorted - тоже принимает список и выражение(обычная или лямбда функция)

# students = [
#     {
#         'name':'Alex',
#         'score':85
#     },
#     {
#         'name':'Geroge',
#         'score':91
#     },
#     {
#         'name':'Siri',
#         'score':60
#     }
# ]


# lst = [1,2,3,4,5,6,7]
# sorted_numb= sorted(lst, key= lambda x: abs(10-x))
# print(sorted_numb)


# from functools import reduce
# reduce - функция высшего порядка, которая принимает два аргумента:
# 1) принимает 2 аргумента в лице списка и вырадения
# 2) он обобщает(суммирует, конктирует...) по заданному вырадению
# 3) третьиим аргументом мы можем указать нулевое значение(по дефолту нуль)
# new_var = reduce(lambda acc,x: acc + x, lst)
# acc - точка опоры - нулевое значение, начальная точка

# lst = [1,2,3,4,5,6,7]
# summed = reduce(lambda acc, x: acc + x, lst, 3)
# print(summed)


# f1 = lambda x: x*2
# f2 = lambda x: x%2 == 0
# f3 = lambda x: len(x)


# lst= ['car', 'elephant', 'hi', 'notebook']
# print(list(filter(lambda x: len(x)> 4 ,lst )))

# lst = [{
#     'name': 'Ali',
#     'age': 30
# },
#     {
#     'name': "Zara",
#     'age': 25
# }

# ]
# sorted_lst = sorted(lst, key=lambda x: x['age'])
# print(sorted_lst)

# lst = [1,2,3]
# new_lst = list(map(lambda x: 'odd' if x % 2 else 'even', lst))
# print(new_lst)

# ----------------------------------------------------------------------------------------------
# words = ['apple', 'banana', 'apricot', 'blueberry', 'avocado']
# dct={}
# f = lambda x: dct[x[0]] = [] if x[0] not in dct.keys() else dct[x[0]].append(filter(lambda b: b[0] == x[0], lst))
# ----------------------------------------------------------------------------------------------


# users = [
#     {"name": "Ali", "contacts": {"email": "a@mail.com"}},
#     {"name": "Zara", "contacts": {}},
#     {"name": "Timur", "contacts": {"email": "timur@mail.com"}},
# ]

# filt_users = list(filter(lambda x: 'email' in x['contacts'].keys(), users))
# print(filt_users)

# products = [
#     {"name": "Monitor", "price": 200, "discount": 0.1},
#     {"name": "Mouse", "price": 50, "discount": 0},
#     {"name": "Keyboard", "price": 80, "discount": 0.2}]

# sorted_prods = sorted(products, key= lambda x: x['price'] * x['discount'])
# print(sorted_prods)



# lst = [{
#     'name': 'Ali',
#     'age': 30
# },
#     {
#     'name': "Zara",
#     'age': 25
# }

# ]


# def makes_filter(key, treshold):
#     return lambda x: x[key] > treshold

# filtered_lst = list(filter(makes_filter('age', 25), lst))
# print(filtered_lst)


# from functools import reduce
# names = ['Ali', 'Zara', 'Oleg']
# reduced_names = reduce(lambda acc, x: acc + " " + x, names)
# print(reduced_names)