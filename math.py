#python中的數學

#加減乘除

apples=3
apples=apples+1#印出來等於3+1=4
print(apples)

apples+=1 #功能一樣但是更簡短
print(apples)

############################################

apples=apples-1
print(apples)

apples-=1#跟"+="一樣的原理
print(apples)

############################################

apples=apples*2
print(apples)

apples*=2
print(apples)

############################################

apples=apples/2
print(apples)

apples/=2
print(apples)

#指數(平方、三次方)

box=int(3)
box=box**2#"**"如同"^"
print(box)

box**=3
print(box)

#模數 mod

#10 mod 3 等於 3 餘 1
print(10%3)
#11 mod 3 等於 3 餘 2
print(11%3)
#12 mod 3 等於 4 餘 0
print(12%3)

#內置數學函數

#次方 pow

print(pow(2,5))#2的5次方

#最大值Max 與最小值 Min

x=1
y=2
z=int(3)
print(max(x,y,z))
print(min(x,y,z))

#四捨五入 round

a=3.14
print(round(a))
b=3.5
print(round(b))

#絕對值

c=-4
print('絕對值:',abs(c))#要加逗號再接abs

#四捨五入、無條件進位、無條件捨去
import math

#引入數學模塊
x=9.5
print(round(x))
print(math.ceil(x))#無條件進位
print(math.floor(x))#無條件捨去

#圓周率 pi

print(math.pi)#3.141592653589793

#計算園的周長

radius=float(input('請輸入圓的半徑'))
c=2*math.pi*radius

print(f'圓的周長為:{round(c,2)}')#四捨五入算出來的結果，c後面點二是小數後第二位

#計算圓面積

radius=float(input('請輸入圓的半徑:'))
area=math.pi*radius*radius#也可以radius**2，也可以用pow
print(f'圓的面積為:{round(area,3)}平方單位')