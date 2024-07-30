#Python中的類別變數

#物件的變數
class Car:
    wheels=4
    #物件的變數
    def __init__(self,make,model,year,color):
        #初始化
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        
car1=Car("ford","focus",2023,"white")

print(car1.wheels)
#機車
car2=Car("sym","勁戰",2020,"black")
print(car2.model)
car2.wheels=2
print(car2.wheels)