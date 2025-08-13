# comprehention - в питоне это явное написание использования цикла для лаконичнотсти кода

# выражение for переменная in итерабельный объект

# nums = [1,2,3,4]


# # list comprehention - выражение в списке
# doubled = [x**2 for x in nums]
# print(doubled)

# evens = [x for x in nums if x%2 == 0]
# print(evens)

# new_nums = [(x,y) for x in range(5) for y in range(5,10)]
# print(new_nums)

# # set comprehention - итерируем и получаем уникальные значения
# unique_set = {x+'!' for x in ['apple', 'grape', 'orange', 'apple']}
# print(unique_set)

# # dixtionary comprehention - итерируем в словарь
# dict_of_fruits = {word: len(word) for word in ['apple', 'grape', 'orange', 'apple']}
# print(dict_of_fruits)




# string = 'hello world!'
# dct = {symb: string.count(symb) for symb in string if symb != ' '}
# print(dct)


# lst = [100, 200, 300]
# dct = {price: price * 0.8 for price in lst}
# print(dct)


# string = 'python'
# lst_up = [symb.upper() for symb in string]
# print(lst_up)

# a= ['Texas', 'California', 'Florida']#state
# b= ['Austin', 'Sacramanto', 'Tallahassee']#capital

# result = {state: capital for state, capital in zip(a,b)}
# print(result)
# print(list(zip(a,b))) #создает список из кортежей в виде (эл из a, эл из b)

# print(list(enumerate(['apple', 'grape', 'orange', 'apple'])))#enumerate - то же самое только (индекс, эл

# def decorator_str(x):
#     return f'====={x}======'

# new_cities = [decorator_str(x) for x in b]
# print(new_cities)


# names = ["Ali", "Zara", "Timur"]
# scores = [90, 85, 92]

# dct = {name: score for name, score in zip(names, scores)}
# print(dct)

# matrix = [[1,2,3], [4,5,6]]
# pow_nums = [y**2 for x in matrix for y in x]
# print(pow_nums)

# string = '12345'
# lst = [int(x)**2 for x in string ]
# print(lst)



