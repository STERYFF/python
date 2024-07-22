#Python 中的集合 list,sets,tuple

#list 列表

fruit=["蘋果","柳橙","香蕉","椰子"]

print(fruit[0])

for i in fruit:
    print(i)

fruit.append("芭樂")#列表中加入"芭樂"
print(fruit)

fruit.remove("椰子")#列表中刪除"椰子"
print(fruit)

print(fruit.index("香蕉"))
fruit.append("蘋果")
print(fruit)
print(fruit.count("蘋果"))

print(fruit)
fruit.reverse()
print(fruit)

#################################################

#set

fruit_set={"a","b","c"}#不能重複且沒有順序
fruit_set.add("a")#沒用
fruit_set.add("d")
for fruit in fruit_set:
    print(fruit,end=" ")
if "a" in fruit_set:
    print("這裡面有a")
else:
    print("這裡沒有a")

##################################################

#tuple 元組

fruits_tuple=("q","w","e","q")#有順序且不能改變
result=fruits_tuple.count("q")
print(result)

result=fruits_tuple.index("w")
print(result)