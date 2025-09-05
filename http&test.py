def run_quiz():
    quiz_questions = [
        # === Раздел 1. Testing & Code Quality ===
        {
            "question": "1. Какой вид тестов проверяет отдельную функцию или класс?",
            "options": ["a) Unit tests", "b) Integration tests", "c) End-to-End tests"],
            "answer": "a"
        },
        {
            "question": "2. Какой вид тестов проверяет взаимодействие нескольких модулей вместе?",
            "options": ["a) Unit tests", "b) Integration tests", "c) Smoke tests"],
            "answer": "b"
        },
        {
            "question": "3. Что означает аббревиатура TDD?",
            "options": ["a) Test-Driven Development", "b) Technical Debugging Data", "c) Total Design Development"],
            "answer": "a"
        },
        {
            "question": "4. Какой встроенный модуль в Python используется для тестирования?",
            "options": ["a) pytest", "b) unittest", "c) mock"],
            "answer": "b"
        },
        {
            "question": "5. Какой инструмент чаще используется для более простого написания тестов?",
            "options": ["a) pytest", "b) unittest", "c) selenium"],
            "answer": "a"
        },
        {
            "question": "6. Что делает функция assertEqual в unittest?",
            "options": ["a) Сравнивает два значения на равенство", "b) Проверяет, что выражение истинно", "c) Проверяет, что список пуст"],
            "answer": "a"
        },
        {
            "question": "7. В pytest для проверки равенства используется:",
            "options": ["a) self.assertEqual(a, b)", "b) assert a == b", "c) check_equal(a, b)"],
            "answer": "b"
        },
        {
            "question": "8. Для чего используется mocking?",
            "options": ["a) Для имитации работы внешних сервисов или объектов", "b) Для ускорения тестов", "c) Для удаления ошибок"],
            "answer": "a"
        },
        {
            "question": "9. Какой порядок шагов в TDD?",
            "options": ["a) Написать код → написать тест → проверить", "b) Написать тест → написать код → рефакторинг", "c) Запустить программу → исправить ошибки → добавить тесты"],
            "answer": "b"
        },
        {
            "question": "10. Какое преимущество даёт TDD?",
            "options": ["a) Код работает быстрее", "b) Меньше багов и лучшее понимание задачи", "c) Программа потребляет меньше памяти"],
            "answer": "b"
        },

        # === Раздел 2. Python Unit Tests ===
        {
            "question": "11. Что делает конструкция unittest.main()?",
            "options": ["a) Запускает тесты в модуле", "b) Подключает pytest", "c) Запускает только один тест"],
            "answer": "a"
        },
        {
            "question": "12. Что вернёт assert inc(3) == 4?",
            "options": ["a) Ошибку", "b) True", "c) Ничего (если проверка пройдена)"],
            "answer": "c"
        },
        {
            "question": "13. Что произойдёт, если тест падает?",
            "options": ["a) Тесты останавливаются", "b) unittest или pytest выводит ошибку", "c) Код автоматически исправляется"],
            "answer": "b"
        },
        {
            "question": "14. Какая команда запускает все тесты pytest в проекте?",
            "options": ["a) pytest run all", "b) pytest", "c) python test_all.py"],
            "answer": "b"
        },

        # === Раздел 3. Mocking ===
        {
            "question": "15. Как создаётся mock-объект в Python?",
            "options": ["a) fake = Mock()", "b) fake = unittest()", "c) fake = Pytest.Mock()"],
            "answer": "a"
        },
        {
            "question": "16. Что делает fake_api.fetch.return_value = 'Sunny'?",
            "options": ["a) Задает заглушку для метода fetch", "b) Запускает метод fetch", "c) Удаляет метод fetch"],
            "answer": "a"
        },
        {
            "question": "17. Что возвращает get_user_name(api, user_id)?",
            "options": ["a) Строку с именем пользователя", "b) ID пользователя", "c) Список всех пользователей"],
            "answer": "a"
        },

        # === Раздел 4. TDD — практика ===
        {
            "question": "18. При TDD сначала пишем:",
            "options": ["a) Код функции", "b) Тест", "c) Документацию"],
            "answer": "b"
        },
        {
            "question": "19. Что должен делать первый тест?",
            "options": ["a) Успешно выполняться", "b) Падать (так как кода ещё нет)", "c) Проверять скорость работы"],
            "answer": "b"
        },
        {
            "question": "20. Какой результат правильной работы TDD-цикла?",
            "options": ["a) Зелёные тесты", "b) Красные тесты", "c) Нет тестов"],
            "answer": "a"
        },

        # === Раздел 5. Модули, пакеты, API ===
        {
            "question": "21. Что такое модуль в Python?",
            "options": ["a) Отдельный файл .py", "b) Папка с кодом", "c) Встроенная библиотека"],
            "answer": "a"
        },
        {
            "question": "22. Что обязательно должно быть внутри пакета?",
            "options": ["a) main.py", "b) __init__.py", "c) requirements.txt"],
            "answer": "b"
        },
        {
            "question": "23. Что делает from app import *?",
            "options": ["a) Импортирует все функции и классы модуля", "b) Импортирует только circle_area", "c) Ничего не импортирует"],
            "answer": "a"
        },
        {
            "question": "24. Какой метод HTTP используется для получения данных?",
            "options": ["a) GET", "b) POST", "c) PUT"],
            "answer": "a"
        },
        {
            "question": "25. Какой метод HTTP используется для создания данных?",
            "options": ["a) GET", "b) POST", "c) DELETE"],
            "answer": "b"
        },
        {
            "question": "26. Что вернёт response.json()?",
            "options": ["a) Текст в формате HTML", "b) Python-словарь", "c) Строку"],
            "answer": "b"
        },
        {
            "question": "27. Что делает библиотека BeautifulSoup?",
            "options": ["a) Тестирует API", "b) Парсит HTML-код", "c) Создаёт JSON"],
            "answer": "b"
        },

        # === Раздел 6. Дополнительно ===
        {
            "question": "28. В weather.py какие данные случайно генерируются?",
            "options": ["a) Только температура", "b) Температура, влажность, условия", "c) Только город"],
            "answer": "b"
        },
        {
            "question": "29. Что делает json.dumps()?",
            "options": ["a) Загружает JSON из файла", "b) Преобразует Python-объект в строку JSON", "c) Парсит HTML"],
            "answer": "b"
        },
        {
            "question": "30. Какой цвет в colorama используется для температуры выше 25°C?",
            "options": ["a) BLUE", "b) GREEN", "c) RED"],
            "answer": "c"
        },
    ]

    score = 0
    print("=== QUIZ: Testing & Code Quality ===\n")

    for q in quiz_questions:
        print(q["question"])
        for opt in q["options"]:
            print(opt)
        answer = input("Ваш ответ: ").strip().lower()
        if answer == q["answer"]:
            print("✅ Правильно!\n")
            score += 1
        else:
            print(f"❌ Неправильно. Правильный ответ: {q['answer']}\n")

    print(f"Ваш итоговый результат: {score}/{len(quiz_questions)} баллов")


if __name__ == "__main__":
    run_quiz()
