Custom object detection training process
Producing dataset - Recorded each gesture as a video file of ~1 minute each and divided one gesture video to 400 images.
Annotating the images - Used draw_box.py program to label gestures to produce .xml files with gesture in YOLO format coordinates inside the .xml file
Manipulating the configuration(cfg) files - changed the number of classes in the region layer to the number of gestures , that is, 4 . Changed the filters variable according to the formula - 5*(5+ classes) inside the convolutional layer.
Getting the equivalent .weights file for the cfg file - Installed the yolov2-tiny.weights file for the cfg file
Listing objects in labels.txt file - All the object(gesture) names were written down in the labels.txt file each in a new line.
Using the training command to train the model - This is where the training begins after the command is entered. The following command was - 
python flow --model cfg/yolov2-tiny-voc-1c.cfg --load bin/yolov2-tiny-voc.weights --train --annotation Annotations --dataset obj --gpu 1.0 --epoch 1000

Since the dataset for each gesture was small(400 images), I used a higher 