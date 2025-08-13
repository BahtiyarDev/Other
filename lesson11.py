import csv
# # r, w, a, x


# with open('data.csv', mode='r') as f:
#     reader = csv.reader(f) # Созает список из списков([ [], [], [] ])
#     for row in reader:
#         print(row)

# with open('data.csv', mode='r') as f:
#     reader = csv.DictReader(f) # Создает список из словарей([{}, {}, {}])
#     for row in reader:
#         print(row['name'], row['age'])

data = [['sasha', 'sash@gmail.com']]
row = [{'name':'Sasha', 'age':15}, {'name':'Zhora', 'age':16} ]
keys = ['name', 'age']
with open('data.csv', mode='w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys, delimiter='|')
    writer.writeheader()
    writer.writerows(row)

# csv.register_dialect("semicolon",delimiter=';')
# with open('data.csv', 'r') as f:
#     reader =csv.reader(f, dialect='semicolon')
#     for r in reader:
#         print(r)
# try:
#     with open('employees.csv', 'r') as file_input, \
#         open('data.txt', 'w', encoding='utf8') as file_output, \
#         open('high_salary.csv', 'w', newline='') as f:
#             reader = csv.DictReader(file_input)
#             keys = ['name', 'salary']
#             for employee in reader:
#                 file_output.write(f'{employee['name']} работает в отделе {employee['department']} и получает заплату {employee['salary']}$\n')
#                 if int(employee['salary']) > 60000:                           
#                     writer = csv.DictWriter(f, fieldnames=keys)
#                     writer.writeheader()
#                     #    writer.writerow({'name': employee['name'], 'salary': employee['salary'] })
                    
#                     #    writer.writerow(employee)
#                     print(employee)
                                  
# except FileExistsError:
#        print('Данного файла не существует!')
# except csv.Error as e:
#        print(f'Библиотека csv выдает ошибку {e}')


# def format(csv_file):
#     # with open(csv_file, 'r') as f:
#     f = open(csv_file, 'r')
#     count = 0
#     counter = 0
#     summ = 0
#     reader = csv.reader(f)
#     for row in reader:
#         if count == 0:
#             name_of_columns = row
#             name_of_columns = list(name_of_columns)
#         count += 1
#         for value in row:
#             try:
#                 value = int(value)
#             except ValueError:
#                 pass
#             if isinstance(value, int):
#                 summ += value
#                 counter += 1


                    
#     return count, name_of_columns, round((value/counter), 3)

# print(format('employees.csv'))