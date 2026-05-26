# class Student:
#     def __init__(self):
#         self.name="rimel"
# s=Student()
# print(s.name)        

# class Student:
#     def __init__(self):
#         self.__name="rimel"

# class Bank:
#     def __init__(self):
#         self.__balance=5000
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("invalid balance")
# b=Bank()
# print(b.get_balance())
# b.set_balance(6000)
# print(b.get_balance())

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Tesla(Car):
#     def start(self):
#         print("tesla is starting")

# c=Tesla()

# print(c.start())

# class Student:
#     def __init__(self):
#         self.name="rimel"
# s=Student()
# print(s.name)

# class Student:
#     def __init__(self):
#         self._name="rimel"

# class Name:
#     def __init__(self):
#         self.__name="rimel"

# class Bank:
#     def __init__(self):
#         self.__balance=900
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("invalid")
# b=Bank()
# print(b.get_balance())
# b.set_balance(1000)
# print(b.get_balance())

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Tesla(Car):
#     def start(self):
#         print("tesla is starting")

# n=Tesla()
# print(n.start())

class Animal:
    def cat(self):
        print("cat can sound meow")
    
class Dog:
    def cat(self):
        print("dog is barking")

c=Dog()
d=Animal()
c.cat()
d.cat()


