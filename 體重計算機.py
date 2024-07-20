#Python 體重轉換器

weight=float(input("請輸入你的體重"))
unit=input('你的體重計是公斤還是磅?(kg/lb)').upper()

if unit=="KG":
    weight*=2.25
    new_unit="磅"
elif unit=="磅":
    weight/=2.2
    new_unit="KG"
else:
    print('單位不正確')
    exit()

print(f'你的體重是{round(weight)}{new_unit}')