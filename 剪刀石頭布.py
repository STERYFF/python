import random#引入模組

player=None
computer=None

running=True
options=("剪刀","石頭","布")
while running:
    player=input("請輸入剪刀、石頭、布:")
    while player not in options:
        input("輸入錯誤，請輸入剪刀、石頭、布:")
    computer=random.choice(options)
    print(f"玩家:{player}，電腦:{computer}")
    if player==computer:
        print("平手")
    elif player=="剪刀" and computer=="布":
        print("你贏了")
    elif player=="布" and computer=="石頭":
        print("你贏了")
    elif player=="石頭" and computer=="剪刀":
        print("你贏了")
    else:
        print("你輸了")
    play_again=input("再玩一局?(Y/N)").lower()
    if not play_again=="y":
        running=False
        
print("感謝你的遊玩")