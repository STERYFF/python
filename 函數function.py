#Python中的函式 / 函數 function

#又稱為方法(method)

# def say_hello():#define一個函式
#     print('Hello World!')
# say_hello()
# say_hello()

#傳遞參數

def greeting(name):
    print(f"你好{name}!")
greeting("Steryff")

def add(x,y):
    return x+y

result=add(3,5)
print(result)

def sub(x,y):
    return x-y

result2=sub(5,2)
print(result2)

def mul(x,y):
    return x*y

result3=mul(2,3)
print(result3)

def div(x,y):
    return x/y

result4=div(12,3)
print(result4)

def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last

print(create_name("john","wick"))