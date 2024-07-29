import shutil
#copyfile 只複製內容，不複製描述內容
#copy 複製內容，不複製原數據
#copy2 全都複製
w=r"C:\Users\Administrator\Desktop\workspace"
source=f"{w}/source_file.txt"
destination=f"{w}/destination_file.txt"
shutil.copyfile(source,destination)