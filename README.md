# modeling-2019

## Modified version of yolov3-tiny from [ultralytics](https://github.com/ultralytics/yolov3/)

## How to run
-Add images and labels to yolov3\nameplates (should be named image_###.png)

-Make sure data/test_data and data/train_data match the file names

-Add images to data/samples to see bounding boxes being drawn after model is trained
 
 -**Train model:** `python train.py --cfg cfg/yolov3-tiny.cfg --data data/coco.data --epochs (number)` (if you have an Nvidia gpu, download CUDA and add --device 0)

## Useful scripts
-directoryGenerator.py for creating test_data and train_data files (randomly assigns test/train)

-fileRenamer.py for adding underscores in image names