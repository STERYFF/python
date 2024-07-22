menu={
    "pizza":300,
    "pop corn":200,
    "fries":90,
    "chips":60,
    "bread":120,
    "soda":60,
    "lemon water":90
}
cart=[]
total=0
print("菜單:")
print("---------------------")
for item,price in menu.items():
    print(f'{item}:{price}')
    
while True:
    food=input("\n請輸入一個菜單項目:(輸入q結束)\n")
    if food=="q":
        break
    elif menu.get(food) is None:
        print("沒有這個商品")
    else:
        cart.append(food)
        total=total+menu.get(food,0)
        print(food,end=" ")

print(f"總共:{total}元")
print(f"購買項目有:{cart}")