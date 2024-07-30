#Python 中的方法鏈 Method Chaining

#car.turn_on().drive().brake().turn_off()

class Car:

    def turn_on(self):
        print('you turned on the engine')
        #回傳物件本身
        return self

    def drive(self):
        print('you are driving')
        return self

    def brake(self):
        print('you braked')
        return self

    def turn_off(self):
        print('you turned off the car')
        
car=Car()
car.turn_on().drive().brake().turn_off()