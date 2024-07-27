from genericpath import exists, isdir
import os


str=r"C:\Code Life\Pyhton學習"#加上r是直接讓斜線出現
print(str)

if os.path.exists(str):
    print("路徑存在")
else:
    print("路徑不存在")
    
if os.path.isfile(str):
    print("該路徑為檔案")
elif os.path.isdir(str):
    print("該路徑為目錄")
else:
    print("其他")