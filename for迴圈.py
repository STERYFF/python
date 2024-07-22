#Python中的 for 迴圈

for x in range(1,11):#in 後面接可迭代的物件
    print(x)
    
for x in reversed(range(1,11)):#reversed從1~10倒數回來
    print(x)
print("Happy New Year!!")

credit_card="1234-5678-9012-3456"
for x in credit_card:
    print(x)

for x in credit_card:
    if x =='9':#發現之中有"9"
        continue#去掉"9"繼續打印
    else:
        print(x)

for x in credit_card:
    if x =="9":
        break#遇到"9"就停住
    else:
        print(x)
        
#字典 dictionary
#鍵 key : 值 value
my_dict={"a":1,"b":2,"c":3}#宣告字典

for x in my_dict:
    print(x)
    
for key,value in my_dict.items():#分別抓出 key 還有 value
    print("key",key)
    print("value",value)