#if else elif控制流程

#Boolean 布林值

for_sale=True #true false 先設定好了)
if for_sale: #(如果for_sale為true)
    print('此項目正在出售')
else:        #(如果for_sale為false)
    print('此項目未出售')

#if else

age=int(input('請輸入你的年齡:'))

if age >=18:
    print("你可以註冊")
else:
    print("你不能註冊")

#elif=>else if 的縮寫

age=int(input('請輸入你的年齡:'))
if age>=100:
    print('你年紀太大')
elif age>=18:
    print('你可以註冊')
elif age<0:
    print('你還沒出生')
else:
    print('你要買18歲')

#練習{計算機}

operator=input("請輸入運算符(加法:+ 減法:- 乘法:* 除法:/ )")
num1=float(input('請輸入第一個數字:'))
num2=float(input('請輸入第二個數字:'))

if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator== '*':
    result=num1*num2
elif operator=='/':
    result=num1/num2
else:
    print('你輸錯了')

print(f'你的結果為{result}')