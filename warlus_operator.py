

#獠牙運算符 :=
#賦值表達式 =

happy=True
print(happy)

print(happy:=False)


foods=[]
while True:
    food=input('你喜歡什麼食物?')
    if food=="quit":
        break
    foods.append(food)
    
print(foods)

foods=[]
while (food:=input('你喜歡什麼食物?'))!="quit":
    # if food=="quit":
    #     break
    foods.append(food)
print(foods)