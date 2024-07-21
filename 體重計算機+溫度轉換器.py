#Python 體重轉換器

from tempfile import tempdir
from tokenize import untokenize


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

################################################################

#Python 溫度轉換器

unit= input("請輸入當前的溫度單位(攝氏:C ,華氏:F):")
temp=float(input("請輸入溫度數值:"))

if unit=='C':
    temp=round(temp*9/5+32)
    print(f"當前的溫度為{temp}度(華氏)")
elif unit=='F':
    temp=round((temp-32)*5/9)
    print(f"當前的溫度為{temp}度(攝氏)")
else:
    print('你輸入錯誤')