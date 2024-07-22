#複利計算機
#總金額 = 本金 * (1 + ( 利率 / 100)) ** 時間

#10000*1.05*1.05
#10000*1.05**2
#10000*(1+5/100)**2

amount=0
rate=0
time=0

amount=0
while amount<=0:
    amount=float(input("請輸入本金金額:"))
    if amount<=0:
        print("本金金額不能小於等於0")


rate=0
while rate<=0:
    rate=float(input("請輸入利率:"))
    if rate<=0:
        print("利率不能小於等於零")

time=0
while time<=0:
    time=int(input("請輸入年限:"))
    if time<=0:
        print("年限不能小於等於零")

print(f"{amount}")
print("利率:",rate)
print("年限",time) 

total=amount*(1+(rate/100))**time
print("總金額:",total)