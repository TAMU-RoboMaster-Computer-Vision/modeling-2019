import os
import sys
import cv2

resultDirectory = "result.txt"
outputDirectory = "output/"
datasetDirectory = "dataset/"
percentThreshold = 0 # 0 to 100
imgType = ".png"

if len(sys.argv) > 1:
    percentThreshold = float(sys.argv[2]) * 100

f = open(resultDirectory, "r")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

""" Extract bounding box data and output to .txt files """
curFile = -1
curImg = -1
prevLine = ""
allFiles = set()
for line in f:
    if line[0] == '0' or line[0] == '1' or line[0] == '2':
        if curFile == -1:
            fileName = prevLine[9:].partition(":")[0][:-4]
            curFile = open(outputDirectory + fileName + ".txt", "w")
            curImg = cv2.imread(datasetDirectory + fileName + imgType)
            allFiles.add(fileName)

        splitted = line.split(":")
        imgH, imgW = curImg.shape[:2]

        objClass = line[0]
        percent = splitted[1].partition("%")[0].strip()
        leftX = str(float(splitted[2].partition("t")[0].strip()) / imgW)
        topY = str(float(splitted[3].partition("w")[0].strip()) / imgH)
        width = str(float(splitted[4].partition("h")[0].strip()) / imgW)
        height = str(float(splitted[5].partition(")")[0].strip()) / imgH)
        
        if int(percent) > percentThreshold:
            curFile.write(objClass + " " + leftX + " " + topY + " " + width + " " + height + "\n")
    else:
        curFile = -1
    prevLine = line

""" Remove all unused images """
for root, dirs, files in os.walk(datasetDirectory):
    for name in files:
        if name.partition(".")[0] not in allFiles:
            os.remove(os.path.join(root, name))