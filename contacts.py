import json

with open('contacts.json', 'r') as r:
    content = json.load(r)


def add_contact(name, number, email):
    usl1 = number[0] == '+' and number[1:].isdigit()
    usl2 = email.count('@') > 0
    usl3 = name.lower() in content.keys()
    if usl3:
        print('Контакт с таким именем уже существует!')
        
    else:
        if usl1 and usl2:
            with open('contacts.json', 'w') as wr:
                content[name.lower()] = {"number": number.lower(), "email": email.lower()}
                json.dump(content, wr)
                print("Контакт успешно создан!")
        else:
            print('Пожалуйста перепроверьте ваши данные!')


def find_contact(name):
    if name.lower() in content.keys():
        print(f'{name}: {content[name.lower()]}')
    else:
        print('Такого контакта нет!')


def edit_contact(name, parameter, change):
    usl1 = change[0] == '+' and change[1:].isdigit()
    usl2 = change.count('@') > 0
    if (parameter.lower() == 'number' and usl1) or (parameter.lower() == 'email' and usl2):
        if name.lower() in content.keys() and parameter.lower() in content[name.lower()].keys():
            with open('contacts.json', 'w') as wr:
                content[name.lower()][parameter.lower()] = change
                json.dump(content, wr)
                print('Параметр успешно изменен!')
        else:
            print('Такого контакта или параметра нет!')
    else:
        print('Проверьте введенные данные!')

def delete_contact(name):
    with open('contacts.json', 'w') as wr:
        if name.lower() in content.keys():
            content.pop(name.lower())
            json.dump(content, wr)
        else:
            print('Такого контакта нет!')


# edit_contact('Oleg', 'email', '+4444448748')
while True:
    qst = int(input("""Выберите действие:
                    1.Добваить контакт
                    2.Найти контакт
                    3.Изменить контакт
                    4.Удалить контакт
                    0.Выход
                    ------------------------
                    Ваш выбор: """))
    if qst == 1:
        add_contact(input("Введите имя: "),
                    input("Ввдеите номер: "),
                    input("Ввдеите email: "))
    if qst == 2:
        find_contact(input("Введите имя контакта: "))
    
    if qst == 3:
        edit_contact(input("Введите имя контакта, который хотите изменить: "),
                     input("Введите параметр(name|number|email), который хотите изменить: "),
                     input("Введите значение, на которое хотите поменять выбранный параметр: "))
    if qst == 4:
        delete_contact(input("Введите имя контакта, который собираетесь удалить: "))
    
    if qst == 0:
        print('Хорошего дня!')
        break


