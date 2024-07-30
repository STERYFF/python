#父類別 <-> 子類別

#動物
class Animal:
    alive=True
    
    def eat(self):
        print('eating')
    def sleep(self):
        print('sleeping')
        
#兔子
class Rabbit(Animal):#括號裡面加上繼承的東西
    def jump(self):
        print('jumping')
        
animal=Animal()
rabbit=Rabbit()
animal.eat()
animal.sleep()
# animal.jump 沒有這個
rabbit.jump()

#魚
class Fish(Animal):
    def swim(self):
        print('swimming')
        
#老鷹

class Hawk(Animal):
    def fly(self):
        print('flying')
        
fish=Fish()
hawk=Hawk()

fish.swim()
hawk.fly()