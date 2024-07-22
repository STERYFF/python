#Python 字典
#鍵 (key) => 值 (value)

capital={
    "United States" : "Washinton DC",
    "Japan" : "Tokyo",
    "France" : "Paris",
    "Russia" : "Moscow"
}

#get()取得鍵值對
print(capital.get("Japan"))
print(capital.get("France"))

#update() 更新鍵值對
capital.update({"Germany":"Berlin"})
print(capital)

#pop()刪除鍵值對

capital.pop("Germany")
print(capital)

#values() 獲得所有值
print(capital.values())

#items()獲得所有鍵值對
print(capital.items())