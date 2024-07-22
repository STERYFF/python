#Python迴圈

#name=input("請輸入你的名子")
#if name=="":
 #   print("你沒有輸入名子")
#else:
 #   print(f"你好{name}")
 
 #範例一
name=""
while name=="":
    name=input("請輸入你的名子")
print(f'你好{name}')

########################################################

#範例二

food=input("請輸入你喜歡吃的食物:")
while food !="q":#"!="是不等於的意思
    print(f"你喜歡吃的食物是{food}")
    food=input("請輸入下一個你喜歡吃的食物:")
print("再見!")

##########################################################

#範例三

num=int(input("請輸入1~10之間的整數"))
while num<1 or num >10:
    print("你輸入無效數字")
    num=int(input("請輸入1~10之間的整數"))
print(f'你輸入了{num}')