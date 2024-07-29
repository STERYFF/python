#物件導向程式設計 OOP

#物件(Object)是類別(Class)的實例(Instance)

#car 4 個輪子
#car.bow()

#車 => 類別 Class
#每一台生產的車子 => 物件 Object

from shutil import make_archive


class Car:
    def __init__(self,make,model,year,color):
        #初始化
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        
    def drive(self):
        print(self.model+"正在行駛")
        
    def stop(self):
        print(self.model+"已停止")
        
        
car1=Car("Toyota","Altis","2021","blue")
car2=Car("Ford","Kuga","2020","white")

car1.drive()
car2.drive()
car2.stop()

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)