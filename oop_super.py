#Python Super 函式

class Rectengle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        print("矩形的初始化已執行")
        
class Square(Rectengle):
    def __init__(self, length, width):
        super().__init__(length, width)
        print("正方形的初始化已執行")
        
        
        
square=Square(300,200)

class Cube(Rectengle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height=height
        print(f"立方體的長寬高為:{length},{width},{height}")
        
cube=Cube(20,60,30)