import time
import json
# import pdb
# try, except, else, finally

# def devide(a, b):
#     try: # пишем код который возможно выдаст ошибку
#         return a/b
#     except ZeroDivisionError: # исключение в виде деления на ноль
#         print('На ноль делить нельзя!')
#     except TypeError:
#         print('Используйте числовой формат пж!')

#     except (ZeroDivisionError, TypeError):
#         print("Используйте только числа кроме нуля пж!")


# print(devide(5, "2"))

# ZeroDividionError- ошибка при делении на ноль
# TypeErroe - ошибка при конфликте типов данных
# ValueError - ошибка при неправильном значении переменной
# NameError - ошибка при отсутствии некой переменной

# c = 0
# while True:
#     try:
#         c+=1
#         print(c)
#         time.sleep(1)
#     except KeyboardInterrupt:
#         print('Время истекло')
#         print(f'Ваш показатель {c} секунд!')


# try:
#     file = open('tasks.json', 'r')
#     print(json.load(file))
# except FileNotFoundError:
#     print('Указано неверное название файла или нет такого файла!')
# except json.JSONDecodeError:
#     print('Файл поврежден!')


# def calc(a, act, b):
#     try:
#         return eval(f'{a} {act} {b}')
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#     except (SyntaxError, NameError):
#         print('Проверьте ваш пример!')
    

# print(calc('1','0', '6'))

# def averageNumber(num_lst):
#     pdb.set_trace()
#     # breakpoint() - то же самое что и pdb.set_trace() но нам не нужен импорт библиотеки
#     # Команды для pdb(интерактивный дебаггер python - кода):
#         # p - вывод нынешней операци в консоль
#         # s - следующий шаг(операция)
#         # n - следующая строка
#         # l - вывод исходного кода
#         # b - ставит breakpoint(точку остановки)
#         # c - переход к ближайшему breapoint()
#     return sum(num_lst)/(len(num_lst))

# print(averageNumber(['2',3,4,5]))



import pdb

# def factorial(n):
#     # pdb.set_trace()
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result

# print(factorial(5))  # Ожидается 120, но получаем 0
# try:
#     file = open('tasks.json', 'r')
#     content = json.load(file)
#     print(content)
# except Exception as e:
#     print(f"Произошла ошибка: {e}")

# else:
#     print('Дальше нужно закрыть файл!')

# finally:
#     file.close()



# class Safe:
#     def __init__(self, filename, mode='r'):
#         self.file = None
#         self.filename = filename
#         self.filemode = mode

#     def __enter__(self):
#         try:
#             self.file = open(self.filename, self.filemode)
#             print('Файл успешно открыт!')
#             return self.file
#         except FileNotFoundError:
#             print('File not found!')

#     def __exit__(self, exc_type, exc_value, exc_tb):
#         if self.file:
#             self.file.close()


# with Safe('tasks.txt') as file:
#     print(file.read())





# class EmailVerificationException(Exception):
#     def __init__(self, email, message='Incorrect format for email!'):
#         self.email = email
#         self.message = message
#         super().__init__(self.message)

# try:
#     raise EmailVerificationException('user@')
# except EmailVerificationException as e:
#     print(f'{e.message}: {e.email}')


class InvalidEmailError(Exception):
    def __init__(self, email, message='Invalid email!'):
        self.email = email
        self.message = message
        super().__init__(self.message)

class IvalidAgeError(Exception):
    def __init__(self, age, message='Invalid age!'):
        self.age = age
        self.message = message
        super().__init__(self.message)
        
class UserValidator:
    def __init__(self, email, age):
        self.age = age
        self.email = email

        
    def valid_age(self):
        if self.age >= 18:
            return 'Age validation completed!'
        else:
            raise IvalidAgeError(self.age)
        
    def valid_email(self):
        if '@' in self.email:
            return 'Email validation completed!'
        else:
            raise InvalidEmailError(self.email)
        
user1 = UserValidator('@fsfdsfsf', 18)
print(user1.valid_email())

        