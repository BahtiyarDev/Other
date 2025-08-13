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