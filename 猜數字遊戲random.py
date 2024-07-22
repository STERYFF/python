import random
# help(random)

# randint()(指定 a 到 b 之間的整數)
print(random.randint(1,10))

#random()(0到 1之間的浮點數)
print(random.random())

#列表中隨機選擇一個元素
options=["剪刀","石頭","布"]
rand_option=random.choice(options)
print("電腦選擇的是:",rand_option)

#將一個列表打亂
cards=['2','3','4','5','6','7','8','9']
random.shuffle(cards)
print(cards)

###################################################

#猜數字遊戲

import random

low=1
high=100
number=random.randint(low,high)
guesses=0

while True:
    guess_num=int(input('請猜一個數字:'))
    guesses+=1
    if guess_num==number:
        print('Bingo!!')
        print(f"數值就是{number}!!")
        print(f'你一共猜了{guesses}次')
        break
    elif guess_num>number:
        print('lower')
    elif guess_num<number:
        print('higher')
    else:
        print('輸入值在100和0之間')
        