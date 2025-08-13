# .json - java script object notation
# josn формат - это зранение данных в виде словаря

# py -> json
# None - null
# True, False - true, false
# Tuples converts in lists

import json

# with open('content2.json', 'r') as f:
#     content = json.load(f)
#     print(content)
# computer_params = content["nested"]
# print(computer_params)

# s = '{"key": 1, "value": 2}'
# data_from_s = json.loads(s)
# print(data_from_s)

# gg = {
#     "hello": "world",
#     "files": ["app.py", "tasks.py"]

# }
# gg_json = json.dumps(gg)# Сериализация
# print(gg_json)

# with open("content.json", 'w') as wr:
#     content["nested"]["ram"] = "8гб"
#     print(content)
#     json.dump(content, wr, indent=4, ensure_ascii=False, sort_keys=True)

# indent - отсутпы от начала строки
# Сериализация - py - > json
# # Десериализация - json -> py (парсинг)
# with open('contact.json', 'r') as rd:
#     content = json.load(rd)
#     print(content)


# def add_contacts(name, number, email):
#     with open('contact.json', 'w') as f:
#         content[name.lower()] = {"Number": number, "Email": email}
#         json.dump(content, f)

# add_contacts("sasha", '+993131313', 'asdada@gmail.com')


# def find_contacts(name):
#     if name.lower() in content.keys():
#         print(f"{name}: {content[name.lower()]}")
#     else:
#         print("Данного контакта нет!")

# find_contacts("Sasha")

# def delete_contact(name):
#     with open('contact.json', 'w') as f:
#         if name.lower() in content.keys():
#             content.pop(name)
#             json.dump(content, f)
#         else:
#             print("Данного контакта нет!")


# delete_contact('sasha')


# with open('task.json', 'r') as r:
#     content = json.load(r)

#     for i in range(len(content) - 1):
#         for j in range(len(content) - i - 1):
#             if content[j]['grades']['math'] > content[j+1]['grades']['math']:
#                 content[j], content[j+1] = content[j+1], content[j]

# with open('task.json', 'w') as wr:

#     # print(content)
#     json.dump(content, wr)



