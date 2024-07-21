#email 字串分析

from cgi import print_arguments, print_environ


email=input("請輸入你的email帳號")

index= email.index("@")#擷取@前面的字串

print(index)#前面的字串數量

print(email[:index])

print(email[index:])

print(email[index+1:])
########################################################
#Python f-flash 的字串格式化

price_1=3.321
price_2=-77
price_3=15.11

#小數點的精確度

print(f'價格1為:{price_1:2f}\n'
      f'價格2為:{price_2:2f}\n'
      f'價格3為:{price_3:2f}')

#加上正號 or 負號

print(f"價格1為:{price_1:+.2f}\n"
      f"價格2為:{price_2:-.2f}\n"
      f"價格3為:{price_3:+.2f}")

#對齊 < > ^

print(f"價格1為:{price_1:>10.2f}\n"
      f"價格2為:{price_2:>10.2f}\n"
      f"價格3為:{price_3:>10.2f}")

#混用不同的符號

print(f"價格1為:{price_1:>+.2f}\n"
      f"價格2為:{price_2:>-.2f}\n"
      f"價格3為:{price_3:>+.2f}")