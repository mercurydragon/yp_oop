class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

    def still_food(self, animal):
        self.speak()
        print(f'Я украл еду у {animal.name}')


class Cat(Animal):

    def speak(self):
        print('Мяу')


class Dog(Animal):

    def speak(self):
        print('Гаф-гаф')


m = Cat('Мурзик')
f = Cat('Феликс')
b = Cat('Борис')

r = Dog('Рекс')
p = Dog('Полкан')
d = Dog('Дружок')

m.still_food(b)
r.still_food(f)
p.still_food(d)
b.still_food(r)
