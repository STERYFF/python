import shutil

path_name = input("請輸入磁碟名稱:")
total, used, free = shutil.disk_usage(path_name)

gb = 2**30

print('磁碟容量:{:.2f}GB'.format(total/gb))
print('已使用空間:{:.2f}GB'.format(used/gb))
print('可用空間:{:.2f}GB'.format(free/gb))
