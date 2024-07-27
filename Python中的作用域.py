#Python中的作用域

#變數範圍與作用域
#LEGB 作用域順序

#L local 區域
#E enclosed
#G global 全域
#B built-in

#變數範圍
a=10

def function_one():
    a=1
    print("a:",a)
    def function_two():
        b=2
        print("b:",b)
        print("a:",a)
    function_two()

function_one()

################################################

from math import e
print(e)
print(round(e))

def function_three():
    print(e)
function_three()