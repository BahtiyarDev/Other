# with open("notes.txt", "w") as file:
#     file.write("Hello world\n")

# try:
#     with open("notes.txt", "x") as file:
#         file.writelines(["Hello world ", "Bye World "])
# except FileExistsError:
#     print('File already here')


# with open("notes.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open('notes.txt', 'r+') as file:
#     # r+ - Дает возможность одновременно и читать файл и записывать в него новую инфу
#     content = file.read()
#     print(content)
#     file.write("New Content")

# with open('notes.txt', 'w+') as file:
#     # w+ - Дает возможность одновременно и читать и перезаписывать файл
#     content = file.read()
#     print(content)
#     file.write("New Content")

# encoding - шифрование данных(для разных символов)
# паттерн try except - хорошая прктика для чистого кода

# создать функцию diary которая находит/ создает файл diary.txt и дает возможность записывать события поизошедшие за сегодняшний день т.е. сперва мы вводит дату и потом уже текст: {date:text}
# def write_diary(name):
#     with open(name, 'r+', encoding="utf8") as file:
#         file.writelines(f'Дата: {input("Enter a date: ")}\n')
#         file.writelines(f'Дорогой дневник, {input()}\n')
#         file.writelines('---------------------------------')
#     return

# def read_diary(name):
#     with open(name, 'r+', encoding="utf8") as file:
#         return file.read()

# # write_diary('diary.txt')
# print(read_diary('diary.txt'))


def sort_products(name):
    with open(name, 'r+') as f:
        lines = f.readlines()
    # print(lines)
    N = int(lines[0].split()[0])  # колво изделий
    M = int(lines[0].split()[1])  # сумма на которую мы планируем потратиться

    A_prod = []
    B_prod = []

    # Разбиваем строку в файле на отдельные элементы
    for i in range(1, N + 1):
        price = int(lines[i].split()[0])
        count = int(lines[i].split()[1])
        type_prod = lines[i].split()[2]
    # Распределяем по группам
        if type_prod == "A":
            A_prod.append([price, count])
            M -= price * count
        else:
            B_prod.append([price, count])
    # Сортируем список B, чтобы купить как можно больше товаров
    for i in range(0, len(B_prod), 1):
        for j in range(len(B_prod) - i - 1):
            if B_prod[j][0] > B_prod[j+1][0]:
                B_prod[j], B_prod[j+1] = B_prod[j+1], B_prod[j]
    # Вычитаем расходы на товары B/ Выводим количество купленных товаров B и оставшиеся деньги
    counter = 0
    for prod in B_prod:
        b_price = prod[0]
        b_count = prod[1]

        prod_max = M // b_price
        can_buy = min(b_count, prod_max)

        M -= b_price * can_buy
        counter += can_buy

    print(counter, M)

sort_products('26 (1).txt')
