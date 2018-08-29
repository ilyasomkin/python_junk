class Animal:
    def speak(self):
        print('I\'m animal')

    def reply(self):
        self.speak()


class Mammal(Animal):
    def speak(self):
        print('I\'m animal -> mammal')


class Cat(Mammal):
    def speak(self):
        print('I\'m cat -> mammal')


class Dog(Mammal):
    def speak(self):
        print('I\'m dog -> mammal')


class Primate(Mammal):
    def speak(self):
        print('I\'m primate -> mammal')


class Hacker(Primate):
    pass


spot = Cat()
spot.reply()
data = Hacker()
data.reply()
