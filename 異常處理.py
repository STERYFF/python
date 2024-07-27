#Python中的異常處理(Error Handling)

#exception

try:
    x=int(input("請輸入一個整數:"))
    y=int(input("請輸入另一個整數:"))
    print(x/y)
# except ValueError:
#     print("請輸入整數")
# except ZeroDivisionError:
#     print("除數不能為0")
except (ValueError,ZeroDivisionError):
    print("出現錯誤")
# finally:
#     print("無論正確或出現異常我都會出現")
else:
    print("else其他的錯誤")