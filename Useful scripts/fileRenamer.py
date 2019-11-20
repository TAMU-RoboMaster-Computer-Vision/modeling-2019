import os

path = r"C:\Users\Kipp\Desktop\labels"
path2 = r"C:\Users\Kipp\Desktop\images"

for filename in os.listdir(path):
    os.rename(os.path.join(path,filename), os.path.join(path,filename[:5]+'_'+filename[5:]))
for filename in os.listdir(path2):
    os.rename(os.path.join(path,filename), os.path.join(path,filename[:5]+'_'+filename[5:]))