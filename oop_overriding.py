#Python 中的方法重寫 (Method Overriding)

class Animal:
    def eat(self):
        print('eating')
        
#哺乳類 Mammal
class Mammal():
    def hi(self):
        print('I am mammal')

# 貓 Cat
class Cat(Mammal):
    def eat(self):
        print('drinking water')
        
# 狗 Dog
class Dog(Mammal):
    def eat(self):
        print('chewing bones')
cat=Cat()
cat.eat()
dog=Dog()
dog.eat()
mammel=Mammal()
mammel.hi()

class Rabbit(Animal):
    def eat(self):
        print('eating carrot')
        
animal=Animal()
animal.eat()
rabbit=Rabbit()
rabbit.eat()