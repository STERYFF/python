#list , set , tuple

goods=[]#列表list
prices=[]

while True:
    good=input("請輸入你想購買的物品:")
    
    if good.lower()=="q":
        break
    
    price=float(input(f"請輸入{good}的價格:"))
    goods.append(good)
    prices.append(price)

print("商品分別為:",goods)
print("價格分別為:",prices)

for index,good in enumerate(goods):
    # print("索引 index:",index)
    # print("商品名稱:",good)
    print(f"第{index+1}個商品為{good}，價格:{prices[index]:.2f}")
    
total=sum(prices)
print(f"總價格:${total}")