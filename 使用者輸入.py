#input 取得使用者輸入

#name=input('請輸入名子:')
#print(f'你的名字式:{name}')

#練習一:填詞遊戲

#adj1=input('請輸入第一個形容詞:')
#noun=input('請輸入名詞:')
#adj2=input('請輸入第二個形容詞:')
#verb=input('請輸入動詞:')
#dj3=input('請輸入第三個形容詞:')

#print(f'今天我去了一個{adj1}的動物園，在展覽中我看到了{noun}，這個{noun}很{adj2}，正在{verb}，我感到很{adj3}')


#練習二:計算矩形面積

#length=float(input('請輸入矩形的長度:'))#讓輸入的值變成浮點數
#width=float(input('請輸入矩形的寬度:'))

#area=(length*width)
#print(f"面積為:{area}平方單位")

#練習三:購物車程式

item=input('你想購買甚麼物品?')
price=float(input('價格多少?'))
quantity=int(input('買幾件?'))

total=(price*quantity)

print(f'您購買了{item} 價格為:{price} 買了:{quantity}件 總價為:{total}元')