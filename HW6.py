# 1
# class SmartHome:
#     def __init__(self):
#         self.__settings = {'lights': 'off',
#                            'temperature': '36', 'alarm': 'off'}
#         self.__password = 'qwerty'

#     def change_settings(self, key, value, password):
#         if password == self.__password:
#             self.__settings[key] = value

#         else:
#             print("Введенный пароль неверен! Доступ запрещен!")

#     def get_settings(self, password):
#         if password == self.__password:
#             print(self.__settings)
#         else:
#             print("Введенный пароль неверен! Доступ запрещен!")


# smart_home = SmartHome()
# smart_home.get_settings(input("Введите пароль: "))

# smart_home.change_settings(input("Элемент, который вы хотите изменить: "),
#                            input("Значение, наа кторое хотитет изменить: "),
#                            input("Пароль: "))

# smart_home.get_settings(input("Введите пароль: "))

# 2
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount == 0:
#             print("Невозможная операция! ")
#         else:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("На вашем счету недостаточно средств для выполнения операции!")
#         else:
#             self.__balance -= amount

#     def get_balace(self):
#         return self.__balance


# class SavingAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate):
#         super().__init__(account_number, balance)
#         self.__interest_rate = interest_rate

#     def withdraw(self, amount):
#         if self.get_balace() - amount < 1000:
#             print("Ошибка при проведении снятия! ")
#         else:
#             super().withdraw(amount)


# class CreditAccount(BankAccount):
#     def __init__(self, account_number, balance, credit_limit):
#         super().__init__(account_number, balance)
#         self.__credit_limit = credit_limit

#     def withdraw(self, amount):
#         if self.get_balace() - amount >= self.__credit_limit:
#             super().withdraw(amount)
#         else:
#             print('Невозможно снять денег из-за кредитного лимита!')


# savings = CreditAccount(input('Введите номер аккаунта:'),
#                         int(input('Введите баланс:')),
#                         int(input('Введите процент по кредиту:')))
# savings.withdraw(50)
# print(savings.get_balace())


# 3
class Warrior:
#     def __init__(self):
#         pass

#     def attack(self):
#         return 'Атака мечом!'

# class Mage:
#     def __init__(self):
#         pass
#     def cast_spell(self):
#         return 'Атака магией!'


# class BattleMage(Warrior, Mage):
#     def __init__(self):
#         super().__init__()
#     def dual_attack(self):
#         return self.attack() + ' ' +self.cast_spell()

# player = BattleMage()
# print(player.dual_attack())
