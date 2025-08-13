# Прочитать CSV и преобразовать его в список словарей students, где каждый элемент:
# {"name": str, "age": int, "score": int}
# Использовать zip() и dict comprehension.

# Добавить категорию grade каждому студенту по правилу:
# A: 90–100
# B: 80–89
# C: 70–79
# D: 60–69
# F: <60
# Реализовать через list comprehension.

# Рассчитать:
# Средний балл (avg)
# Топ-3 студентов по баллу (top3), отсортированных по score по убыванию.
# Построить словари через dict comprehension:
# name_to_score — {имя: балл}
# grade_distribution — {категория: количество студентов в категории}

# Сгруппировать студентов по первой букве имени
# Результат: {первая_буква: [список_имён]}
# Использовать set comprehension для множества букв и dict comprehension для группировки.

# Собрать всё в итоговый словарь report:
# report = {
#     "avg": float,
#     "top3": [{"name": ..., "score": ..., "grade": ...}, ...],
#     "grade_distribution": {...},
#     "name_to_score": {...},
#     "groups_by_first_letter": {...}
# }


import csv

cond = lambda x: "F" if int(x['score']) < 60 else "D" if 60<=int(x['score'])<=69 else "C" if 70<=int(x['score'])<=79 else "B" if 80<=int(x['score'])<=89 else "A" if 90<=int(x['score'])<=100 else "Error!"

with open('students_project.csv') as f:
    reader = csv.DictReader(f)
    students = list(reader)
    print(students)
    students_with_grade = [{"name": student['name'], 'age': int(student['age']), 'score': int(student['score']), 'grade': cond(student) } for student in students]

    summ = sum(list(map(lambda student: student['score'], students_with_grade)))
    avg = summ/len(students_with_grade)
    print(avg)

    sorted_students = sorted(students_with_grade, key=lambda student: student['score'], reverse=True)
    print(sorted_students[:3])

    name_to_score = {student['name']: student['score'] for student in students_with_grade}
    print(name_to_score)

    grade_distribution = {student['grade']: sum(1 for s in students_with_grade if s['grade'] == student['grade']) for student in students_with_grade}
    print(grade_distribution)