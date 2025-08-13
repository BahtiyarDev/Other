<<<<<<< HEAD
import json

with open('items.json', 'r') as rd:
    content = json.load(rd)

with open('new_items.json', 'r') as rd:
    new_content = json.load(rd)
    # print(content)

# with open('items.json', 'w') as wr:
#     for dct in content:





with open('new_items.json', 'w') as wr:
    for i in range(len(content)):
        key = content[i]["name"]
        value = content[i]["items"]
        print(key,value)
        content[i].clear()
        if key not in new_content.keys():
            new_content[key] = value
        else:
            new_content[key] += value
    json.dump(new_content, wr)



=======
import json

with open('items.json', 'r') as rd:
    content = json.load(rd)

with open('new_items.json', 'r') as rd:
    new_content = json.load(rd)
    # print(content)

# with open('items.json', 'w') as wr:
#     for dct in content:





with open('new_items.json', 'w') as wr:
    for i in range(len(content)):
        key = content[i]["name"]
        value = content[i]["items"]
        print(key,value)
        content[i].clear()
        if key not in new_content.keys():
            new_content[key] = value
        else:
            new_content[key] += value
    json.dump(new_content, wr)



>>>>>>> a4772715d9c8f3291065ab48cbbbadb055430e40
