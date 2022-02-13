"""Пример реализации наследования"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     def voice(self):
#         print('ИгоГо')
#
# jack = Horse('Jack')
# jack.voice()


"""Пример реализации множественного наследования"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     def voice(self):
#         print('ИгоГо')
#
#
# class Donkey(Animal):
#     def voice(self):
#         print('Иииаа')
#
#
# class Mule(Horse, Donkey):
#     pass
#
#
# ia = Mule('Ia')
# ia.voice()
# print(Mule.__mro__)



"""Пример полиморфизм"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def voice(self):
#         raise NotImplemented
#
#
# class Horse(Animal):
#     def voice(self):
#         print('ИгоГо')
#
#
# class Donkey(Animal):
#     def voice(self):
#         print('Иа Иа')
#
#
# jack = Horse('Jack')
# jack.voice()
#
# stefan = Donkey('Stefan')
# stefan.voice()



"""Пример инкапсуляция"""
# class Animal:
#     def __init__(self, name, age, weight):
#         # объявляем публичные свойства
#         self.name = name
#         self.age = age
#         self.weight = weight
#         # объявляем свойства с ограничением доступа
#         self._protected_value = True  # объявляем protected свойство
#         self.__private_value = True  # объявляем private свойство
#
#     def voice(self):
#         print('ИгоГо')
#
#
# class Horse(Animal):
#     def voice(self):
#         self.voice()
#
#     def __get_age(self):
#         print(self.age)
#
#     def _get_weight(self):
#         print(self.weight)
#
#
# jack = Horse('Jack', 6, 2)
# jack._get_weight() # Попытка обращения к методу protected не вызовет ошибки
# print(jack._protected_value) # тоже самое с protected свойствами
# jack.__get_age() # Попытка обращения к методу private вызовет ошибку
# print(jack.__private_value) # тоже самое с private свойствами
# jack._Horse__get_age()  # Обход ограничения private метода
# print(jack._Animal__private_value)  # Обход ограничения private свойства
