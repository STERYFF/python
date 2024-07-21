#Python中的邏輯運算符

#and or not

temp=float(input('請輸入現在的溫度'))

temp=25
if temp>0 and temp<30:
    print('溫度是適宜的')
else:
    print('溫度不是適宜的')
    
#or

if temp<=0 or temp>=30:
    print("溫度不是適宜的")
else:
    print('溫度適宜')