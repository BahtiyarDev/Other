import csv

# 1
# with open('broken.csv', 'r') as rd, \
#     open('fixed.csv', 'w', newline='') as wr:
#         lines = rd.readlines()
#         writer = csv.writer(wr)
#         for line in lines:
#             # new_line = line.strip().replace(';', ',').split(',')
#             # print(new_line)
#             writer.writerow(line.strip().replace(';', ',').split(','))

# 2
# with open('students1.csv', 'r') as rd1, \
#     open('students2.csv', 'r') as rd2, \
#     open('students.csv', 'a', newline='') as wr:
#     reader1 = csv.reader(rd1)
#     reader2 = csv.DictReader(rd2)
#     writer = csv.writer(wr)
#     for row in reader1:
#         writer.writerow(row)
#     for row in reader2:
#         writer.writerow([row['id'], row['name'], row['grade']])

# 3
with open('employees_v2.csv', 'r') as rd:
    reader = csv.DictReader(rd)
    list_of_departments = {}
    list_of_employees = {}
    for row in reader:
        if row['department'] not in list_of_departments:
            list_of_departments[row['department']] = {'Salary': int(row['salary']), 'Count': 1, 'Projects_Completed': int(row['projects_completed'])}
        else:
            list_of_departments[row['department']]['Salary'] += int(row['salary'])
            list_of_departments[row['department']]['Count'] += 1
            list_of_departments[row['department']]['Projects_Completed'] += int(row['projects_completed'])
    for department in list_of_departments:
        list_of_departments[department]['Sr_zar'] = round(list_of_departments[department]['Salary'] / list_of_departments[department]['Count'], 3)
    print(list_of_departments)                 
    data_list = list(list_of_departments.items())

    for i in range(len(list_of_departments) - 1):
        for j in range(0, len(list_of_departments) - i - 1):
            if data_list[j][1]['Projects_Completed'] > data_list[j + 1][1]['Projects_Completed']:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    # print(data_list[-1])


with open('employees_v2.csv', 'r') as rd:
    reader = csv.DictReader(rd)
    for row in reader:
        name = row['name']
        department = row['department']
        empl_zar = int(row['salary'])
        if empl_zar > list_of_departments[department]['Sr_zar']:
            if department not in list_of_employees:
                list_of_employees[department] = [name]
            else:
                list_of_employees[department].append(name)
    # print(list_of_employees)

with open('employees_info.txt', 'w', encoding='utf8') as wr:
    wr.write('Средння зарплата по отделам:\n')
    for department in list_of_departments:
        wr.write(f'{department}: {list_of_departments[department]['Sr_zar']}\n')
    wr.write('-------------------------------------------------------\n')
    wr.write(f'Отдел с наибольшим числом завершенных заказов: {data_list[-1][0]}\n')
    wr.write('-------------------------------------------------------\n')
    wr.write('Сотрудники с зарплатой выше средней по отделу:\n')
    for department in list_of_employees:
        wr.write(f'{department}: {list_of_employees[department]}\n')

            
            
                
        
            
            