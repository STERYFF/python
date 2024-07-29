str=r"C:\Users\Administrator\Desktop\workspace\test.txt"

try:
    with open(str) as file:
        print(file.read())
except FileNotFoundError:
    print("file not found")
# with open(str) as file:
#     print(file.read())
