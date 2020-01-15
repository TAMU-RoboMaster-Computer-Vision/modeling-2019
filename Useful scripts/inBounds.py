import os
	
path = r"D:\Robomaster\newgitpull\modeling-2019\yolov3\nameplates\labels"
outOfBounds = []

for filename in os.listdir(path):
	with open(os.path.join(path,filename)) as fp:
		lines = fp.readlines()
		n = 0
		for line in lines:
			line = line.strip()
			parts = line.split()
			
			for i in range(1, 5):
				if float(parts[i]) > 1:
					#parts[i] = "1.000000"
					outOfBounds.append(filename)
						
				elif float(parts[i]) < 0:
					#parts[i] = "0.000000"
					outOfBounds.append(filename)
			
			parts = " ".join(parts)
			parts += "\n"
			lines[n] = parts
			n += 1
			
			if filename in outOfBounds:
				break
			
	
	with open(os.path.join(path,filename), 'w') as fp:
		fp.writelines(lines)
		
print(outOfBounds)
print("Length:", len(outOfBounds))

for f in outOfBounds:
	os.remove(os.path.join(path,f))
