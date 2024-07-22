#一個迴圈裡面再包一個迴圈

for x in range(1,10):
    print(x,end=" ")#全部印在同一行上

for y in range(5):#外部迴圈
    for x in range(1,10):#內部迴圈
        print(x,end=" ")
    print()

rows=int(input('請輸入行數:'))
cols=int(input('請輸入列數:'))
symbol=input('請輸入符號:')

for i in range(rows):
    for j in range(cols):
        print(symbol,end=" ")
    print()#執行一次換一行]

################################################################    

import time

my_time=int(input("請輸入秒數"))

for x in range(my_time,0,-1):#0是數到0，-1是倒數的意思
    #120s=2:00
    seconds=x%60
    minutes=x//60%60#兩個除號把原本會變成符點數的變回整數
    print(f"{minutes:02}:{seconds:02}")#:2顯示兩位
    time.sleep(1)#每次間隔一秒
print("時間到了!")