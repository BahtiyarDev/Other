<<<<<<< HEAD
#сделат свою прогамму контактов
    # должн быть поля name email number
    # Бонус редактирование имеющихся контактов

# + доделать 26 номер


def add_contact():
    with open('Contacts.txt', 'a', encoding='utf8') as file:
        file.write(f"Имя: {input("Введите имя конттакта:" )}\n")
        file.write(f"Email: {input('Введите email контакта: ')}\n")
        file.write(f"Номер: {input('Введите номер контакта: ')}\n")
        file.write("----------------------------------------------\n")

def read_contacts():
    with open('Contacts.txt', 'r', encoding='utf8') as file:
        return file.read()
    
add_contact()
=======
#сделат свою прогамму контактов
    # должн быть поля name email number
    # Бонус редактирование имеющихся контактов

# + доделать 26 номер


def add_contact():
    with open('Contacts.txt', 'a', encoding='utf8') as file:
        file.write(f"Имя: {input("Введите имя конттакта:" )}\n")
        file.write(f"Email: {input('Введите email контакта: ')}\n")
        file.write(f"Номер: {input('Введите номер контакта: ')}\n")
        file.write("----------------------------------------------\n")

def read_contacts():
    with open('Contacts.txt', 'r', encoding='utf8') as file:
        return file.read()
    
add_contact()
>>>>>>> a4772715d9c8f3291065ab48cbbbadb055430e40
print(read_contacts())