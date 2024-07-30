# Duck typing

class Duck:
    def walk(self):
        print('duck is walking')
    def talk(self):
        print('duck is talking')
        
class Chicken:
    def walk(self):
        print('chicken is walking')
    def talk(self):
        print('chicken is talking')
        
#即使沒有繼承的關係，也可以當作同一類型的類別使用

class Person():
    def catch(self,duck):
        duck.walk()
        duck.talk()
        
duck=Duck()
person=Person()
person.catch(duck)