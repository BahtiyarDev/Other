from abc import ABC, abstractmethod
from time import sleep

# 1
# class SmartDevice(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass


# class Light(SmartDevice):
#     def turn_on(self):
#         return 'Lights turned on'

#     def turn_off(self):
#         return 'Lights turned off'



# class Thermostat(SmartDevice):
#     def turn_on(self):
#         return 'Thermostat turned on'

#     def turn_off(self):
#         return 'Thermostat turned off'



# class Camera(SmartDevice):
#     def turn_on(self):
#         return 'Camera turned on'

#     def turn_off(self):
#         return 'Camera turned off'


# devices = [Camera(), Thermostat(), Camera()]

# def home_scenario(devices):
#     for device in devices:
#         print(device.turn_on())
#     print("....................")
#     sleep(5)
#     print('Five seconds later')
#     print("....................")
#     for device in devices:
#         print(device.turn_off())


# home_scenario(devices)


# class Behavior(ABC):

#     @abstractmethod
#     def execute(self):
#         pass

# class AggressiveBehavior(Behavior):
#     def execute(self):
#         return  'ведет себя агрессивно'

# class DefensiveBehavior(Behavior):
#     def execute(self):
#         return 'защищается'


# class AICharacter:
#     def __init__(self, name):
#         self.name = name
#         self.current_behavior = DefensiveBehavior()
#         self.aggr = AggressiveBehavior()
#         self.defensive = DefensiveBehavior()

#     def set_aggr_behavior(self):
#         self.current_behavior = AggressiveBehavior()
#         print(f'{self.name} теперь {self.aggr.execute()}')

#     def set_defensive_behavior(self):
#         self.current_behavior = DefensiveBehavior()
#         print(f'{self.name} теперь {self.defensive.execute()}')

#     def get_behavior(self):
#         return self.current_behavior.execute()


# cat = AICharacter('cat')
# print(cat.get_behavior())
# cat.set_aggr_behavior()
# print(cat.get_behavior())


# class BankAccount(ABC):
#     def __init__(self, account_number, balance):
#         self.balance = balance
#         self.account_number = account_number

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             return "Ошибка!"

#     def get_balance(self):
#         return self.balance

#     @abstractmethod
#     def calculate_interest(self):
#         pass


# class SavingAccount(BankAccount):
#     def __init__(self,account_number, balance,  interest_rate):
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate

#     def calculate_interest(self):
#         interest = (self.interest_rate/100) * self.balance
#         self.balance += interest
#         return interest


# class CreditAccount(BankAccount):
#     def __init__(self, account_number, balance, interest_rate, credit_limit):
#         super().__init__(account_number,balance)
#         self.interest_rate = interest_rate
#         self.credit_limit = credit_limit

#     def withdraw(self, amount):
#         if self.balance - amount >= - self.credit_limit:
#             self.balance -= amount

#         else:
#             return "Кредитный лимит превышен"

#     def calculate_interest(self):
#         interest = abs(self.balance) * (self.interest_rate / 100)
#         self.balance -= interest
#         return interest


# class Bank:
#     def __init__(self):
#         self.accounts = {}

#     def create_saving_account(self, account_number, balance, interest_rate):
#         if account_number not in self.accounts:
#             self.accounts[account_number] = SavingAccount(account_number, balance, interest_rate)
#         else:
#             return 'Аккаунт уже в базе данных'
        
#     def create_credit_account(self, account_number, balance, interest_rate, credit_limit):
#         if account_number not in self.accounts:
#             self.accounts[account_number] = CreditAccount(account_number, balance, interest_rate, credit_limit)
#         else:
#             return 'Аккаунт уже в базе данных'
    
#     def deposit(self, account_number, amount):
#         if account_number in self.accounts:
#             return self.accounts[account_number].deposit(amount)
#         else:
#             return 'Аккаунта нет в базе данных'
        
#     def withdraw(self, account_number, amount):
#         if account_number in self.accounts:
#             return self.accounts[account_number].withdraw(amount)
#         else:
#             return 'Аккаунта нет в базе данных'

#     def calculate_interest(self, account_number):
#         if account_number in self.accounts:
#             return self.accounts[account_number].calculate_interest()
#         else:
#             return 'Аккаунта нет в базе данных'
        
#     def get_balance(self, account_number):
#         if account_number in self.accounts:
#             return self.accounts[account_number].get_balance()
#         else:
#             return 'Аккаунта нет в базе данных'

# bank = Bank()
# bank.create_saving_account('12432', 100, 56)
# bank.deposit('12432', 500)
# print(bank.get_balance('12432'))
# print(bank.calculate_interest('12432'))

# bank.create_credit_account('123', 500, 5, 300)
# print(bank.withdraw('123', 1500))