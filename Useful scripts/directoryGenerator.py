from os import listdir
from os.path import isfile, join
import random

# Directory of images
mypath = r"C:\Users\Kipp\Desktop\images"

# Clear file data
open('test_data.txt', 'w').close()
open('train_data.txt', 'w').close()

# Assign images to train/test
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for fileName in onlyfiles:
	rand = random.uniform(0, 1)
	
	if rand >= 0.9:
		with open("test_data.txt", "a") as f:
			print("nameplates\\images\\" + fileName, file=f)
	else:
		with open("train_data.txt", "a") as f:
			print("nameplates\\images\\" + fileName, file=f)