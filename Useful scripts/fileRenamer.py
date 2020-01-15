import os
import re

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)
	
path = r"D:\Robomaster\newgitpull\modeling-2019\yolov3\nameplates\labels"
path2 = r"D:\Robomaster\newgitpull\modeling-2019\yolov3\nameplates\images"

i = 0
j = 0
for filename in sorted_aphanumeric(os.listdir(path)):
	os.rename(os.path.join(path,filename), os.path.join(path,"Image_" + str(i) + ".txt"))
	i+=1
	
for filename in sorted_aphanumeric(os.listdir(path2)):
	os.rename(os.path.join(path2,filename), os.path.join(path2,"Image_" + str(j) + ".jpg"))
	j+=1