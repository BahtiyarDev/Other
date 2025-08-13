# # list - может хранить дуюликаты, изменемый
# lst = ["apple", "pear", "banana"]

# print(lst)

# lst.append("mango")

# print(lst)
# print(lst[0])

# lst[0] = ' '
# print(lst)

# # lst.insert(index. element)

# lst.insert(0, 'orange')
# print(lst)

# lst.remove("apple")
# print(lst)

# # [start:end:step]

# print(lst[0:3])

# print(lst[3:0:-1])

# print(lst)
# lst.reverse()
# print(lst)

# # tuple - используется для конкретных данных в виде списка(их нельзя менять), может хранить дубликаты

# week_days = ("Monday", "Tuesday")

# print(week_days.count("Monday"))
# # .count - выводит количество элементов
# print(f"index_Monday = {week_days.index("Monday")}")
# # .inedx -выводит индекс элемента

# print(list(week_days)) 
# print(tuple(lst))

# # set - список с уникальными элементами, изменяем, удаляет лишние элементы

# st = {1, 2, 2, 3}
# print(st)

# st.add(10)
# print(st)

# st.remove(10)
# print(st)

# st.pop()
# print(st)

# #  & union - обьединение
# # | intersection - пересечение

# classmates = {"sasha", "mark", "oleg"}
# coursemates = {"mark", "alena", "vika"}
# friends = classmates | coursemates
# print(friends)

# i_tam_i_tam = classmates & coursemates
# print(i_tam_i_tam)

# # dict - те же списки, только вместо индексов у них ключи - строчки в виде уникального идентификатора


# user1 = {"name": "Bahtiyar", "age": 16}
# print(user1["age"])

# user1["occupation"] = "student"
# print(user1)

# user1.pop("age")
# print(user1)

# print("name" in user1)


# for key in user1:
#     print(key)
#     print(user1[key])
#     if key == "age":
#         user1[key] = 18
#     print(user1)


# def listik(lst):
#     return list(set(lst))
# a = listik([1, 2, 2, 3])
# print(a)

# def naoborot(lst):
#     return sorted(lst, reverse=True)
# a =naoborot([1, 2, 3 ,4 , 5])
# print(a)




for i in range(10):
    print(i)