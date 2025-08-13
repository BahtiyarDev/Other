# tuples
# 1 вариант
# def counter():
#     tup = tuple(input("Введите кортеж: "))
#     print(tup)
#     element = input("Введите элемент для подсчета: ")
#     count = tup.count(element)
#     return count
# a = counter()
# print(f"Элементов {a} штук")
# 2 вариант
# def counter(tup, element):
#     count = tup.count(element)
#     return count
# print(counter((1, 2, 2, 3, 3), 1))

# a = input()
# b = input()
# print(f"a до: {a}")
# print(f"b до: {b} ")
# tup = (a, b)
# a = tup[1]
# b = tup[0]
# print(f"a после: {a}")
# print(f"b после: {b}")

# set

# lst1 = [1, 2, 3, 4, 4, 5, 6, 6]
# lst2 = [1, 1, 7, 5, 6, 7, 2]
# st1 = set(lst1)
# st2 =set(lst2)
# st = st1 & st2
# print(st)

# lst1 = [1, 2, 3, 4]
# st = set(lst1)
# lst2 = list(st)
# if lst1 == lst2:
#     print("Дубликатов нет")
# else:
#     print("Дубликаты есть")

# dictionary

# def word_counter(lst):
#     word_count = {}
#     for word in lst:
#         print(word)
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#     return word_count
# a = word_counter(["apple", "pear", "pear","orange"])
# print(a)

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"v": 8, "b": 5, "g": 9}
# dictionary = dict2 | dict1
# print(dictionary)

# lst = [("a", 3), ("b",4), ("c", 7)]
# dictionary = dict(lst)
# print(dictionary)

# lst1 = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# lst2 = []
# for listik in lst1:
#     for i in listik:
#         lst2.append(i)
# print(lst2)



