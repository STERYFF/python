#Python的字串方法

#字串指令:"len()"、"find()"、"capitalize()"、
# "upper()"、"lower()"、"count()"、"replace()"

#help(str)查詢字串指令

#使用者的全名

name="steryff"

#幾個字元len
length=len(name)
print("您的全名共有",length,"幾個字元。")

#找到第一個空格name.find("你要的字元")
name="Ste ry ff"
space_pos=name.find(" ")
print("第一個空格出現在第",space_pos,"個字元")

#第一個字母大寫capitalize
name="steryff"
name_capitalize=name.capitalize()
print("你的名子(第一個字母大寫):",name_capitalize)

#全部字母變大寫 upper()
name_upper=name.upper()
print("你的名字全部大寫為:",name_upper)

#全部變小寫 lower()
name="STERYff"
name_lower=name.lower()
print("你的名子全部小寫為:",name_lower)

#count
phone_number=input("請輸入你的電話號碼:")
dash_count=phone_number.count("-")
print("你的電話號碼共有",dash_count,"個短橫線")

#replace
phone_number=phone_number.replace("-", "_")
print("我的電話",phone_number)

#程式練習
#使用者名稱不能超過12個字元
#使用者名稱不包含空格
#使用者名稱不包含數字
#如果都符合顯示"歡迎+使用者名稱"

username=input("請輸入你的使用者名稱:")

if username.isalnum():
    print("全部都是英文字")
else:
    print('包含其他字元')

if len(username)>12:
    print("使用者名稱不能超過12個字元")
elif " "in username:
    print("使用者名稱不包含空格")
elif not username.isalpha():
    print("使用者名稱不包含數字")
else:
    print(f"歡迎 {username}")