# инкапсуляция - скрытие неких атрибутов класса от внешнего взаимодействия(классы - капсулы)
# наследование - перенимать атрибуты и методы у родительского класса(другого класса)
# полиморфизм - "многообращие форм", многообразность классов(многофункцианальнсть атрибутов и методов)
# абстракция - упрощение атрибутов и методов класса по возможности

# class BankAccount:

#     def __init__(self):
#         self.__balance = 0 #общепринятая конвенция для обозначения приватных  атрибутов(__)
#         self.__transactions = []

#     def deposit(self, amount):
#         if amount == 0:
#             print("Невозможная операция")
#         else:
#             self.__balance += amount
#             self.__transactions.append({'type': 'deposit', 'amount': amount, 'balance': self.__balance})

#     def withdraw(self, amount):
#         if amount == 0:
#             print("Невозможная операция")
#         if amount > self.__balance:
#             print('На вашем счету недостаточно средств')
#         else:
#             self.__balance -= amount
#             self.__transactions.append({'type': 'withdraw', 'amount': amount, 'balance': self.__balance})

#     def history_of_transactions(self):
#         return self.__transactions



#     def get_balance(self):
#         return self.__balance
    

# my_first_bank_account = BankAccount()
# my_first_bank_account.deposit(100)
# # print(my_first_bank_account.get_balance())
# my_first_bank_account.withdraw(1000)

# def get_any_balace(entity):
#     return f'На вашем балансе {entity.get_balance()} денег'

# # print(get_any_balace(my_first_bank_account))
# print(*my_first_bank_account.history_of_transactions())


# class Safe:
#     def __init__(self, password):
#         self.__password = password

#     def check_password(self, input_password):
#         if input_password == self.__password:
#             return  "Верный пароль"
#         return "Вы ввели неверный пароль!"

# # лаконичность - + в твой кодинг

# safe_password = Safe(4567)
# inp_password = int(input("Введите пароль: "))
# print(safe_password.check_password(inp_password))



# class TV:
#     def __init__(self):
#         self.__channel = 1

#     def change_channel(self, input_channel):
        # if input_channel in range(1, 101): # O(1)
#         # if 1 <= input_channel <= 100 - O(1)
#             self.__channel = input_channel
#             return
#         return "Такого канала нет"
    
#     def get_channel(self):
#         return self.__channel
    
# tv_channel = TV()
# print(tv_channel.get_channel())

# tv_channel.change_channel(8)
# print(tv_channel.get_channel())



class Device:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def charge(self, source):
        print(f"{self.name} charges from {source}")

class Mobile_Device(Device):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.battery = 0

    def set_charger(self, source):
        print(f"{self.name} charges from {source}")
        self.battery += 100
    
    def get_charge(self):
        return self.battery

lamp = Device('lamp', 'mobile')

lamp.charge('socket')

scales = Mobile_Device('scales', 'mobile')
scales.set_charger('battery pill')
print(scales.get_charge())

    