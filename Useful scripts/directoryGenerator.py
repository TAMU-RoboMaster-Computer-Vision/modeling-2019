from os import listdir
from os.path import isfile, join
import random
import io

# Directory of images
mypath = r"D:\Robomaster\newgitpull\modeling-2019\yolov3\nameplates\images"

# Clear file data
open('test_data.txt', 'w').close()
open('train_data.txt', 'w').close()

# Assign images to train/test
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fileName in onlyfiles:
	rand = random.uniform(0, 1)
	
	if rand >= 0.9:
		with io.open("test_data.txt", "a", encoding="utf-8") as f:
			print("nameplates\\images\\" + fileName, file=f)
	else:
		with io.open("train_data.txt", "a", encoding="utf-8") as f:
			print("nameplates\\images\\" + fileName, file=f)