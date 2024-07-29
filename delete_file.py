import os
import shutil
path=r"C:\Users\Administrator\Desktop\workspace"

#刪除檔案

os.remove(f"{path}/destination_file.txt")

#刪除空資料夾

os.rmdir(f"{path}/dirc")

#刪除資料夾及其內容

shutil.rmtree(f"{path}")