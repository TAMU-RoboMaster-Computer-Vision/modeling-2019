## Purpose
Displays yolo bounding boxes on all images in testing data since Colab will not display images.

Modified version of [YoloBBoxChecker](https://github.com/ivder/YoloBBoxChecker)

## Usage

1. Run this command in Colab (using whatever weights file you want): ```!./darknet detector test data/obj.data cfg/yolov4_training.cfg /mydrive/yolov4/yolov4_training_best.weights -ext_output < data/test.txt > result.txt -dont_show```

2. Download and copy result.txt to this folder (example provided)

3. Put current dataset inside dataset folder

4. Run ```python extract.py``` - this converts result.txt into individual .txt files for each image. It's important to do step 3 before this

5. Run ```python main.py``` and view images in /result

(I'll try to reduce the steps here lol)