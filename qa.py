import random

q_list = [
    "蘋果的英文是",
    '一打雞蛋用掉兩個，還剩下幾個:',
    "問世間，情為何物?的下一句",
    "一天一個樣，之後又重複。(猜一天體)"
]

a_list = [
    'apple',
    '10',
    '直教生死相許',
    '月亮'
]


def words(status=True):
    right = ['好棒棒', '讚啦', '水歐', '答對了']
    wrong = ['再接再厲', '要加油歐', '可惜阿', '你好爛']

    if status:
        msg = random.choice(right)
    else:
        msg = random.choice(wrong)

    print(msg)


score = 0
i = 0
total = len(q_list)

while i < total:
    q = q_list[i]
    a = a_list[i]
    i += 1

    print(q, end=' ')
    ans = input().lower().strip()

    if ans == a:
        score += 10
        words()
    else:
        status = False
        words()

    print()
print("總分:", score)
