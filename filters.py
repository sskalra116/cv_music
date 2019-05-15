import numpy as np
import cv2
import math
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import pprint as pp
import time
from sonic import play_music
from psonic import *
from threading import Thread, Condition, Event
from random import choice
import keyboard

count1=0
count2=0
#model cfg for 4 classes
options = {

    'model': 'cfg/yolov2-tiny-voc-4c.cfg',
    'load': 7000,
    'threshold': 0.04,
    'gpu': 1.0
    
}

tfnet = TFNet(options)

colors = [tuple(255* np.random.rand(3)) for _ in range(10)]

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

def camm():

    
    while True:
        stime = time.time()
        ret, frame = capture.read()
        if ret:
            results = tfnet.return_predict(frame)
            for color, result in zip(colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                label = result['label']
                #trigger music here
                play_music(label)
                
                confidence = result['confidence']
                text = '{}: {:.0f}%'.format(label, confidence * 100)
                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(
                    frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            cv2.imshow('frame', frame)
            print('FPS {:.1f}'.format(1 / (time.time() - stime)))
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            #count1 = 0
            #count2 = 0
            #stop_event.set()
            break

    capture.release()
    cv2.destroyAllWindows()


def play_music(label):

    global count1
    global count2
    if(label == 'thumbs_up'):
        if(count1==0):
            
            live_thread_1.start()
            count1+=1
            
        

    if(label == 'peace'):
        if(count2==0):
            
            live_thread_2.start()
            count2+=1
        


def loop_foo():
    while True:
        sample(LOOP_AMEN)
        play(C2,sustain=1,amp=5)
        sleep(1.74)
  

def loop_bar():
    while True:
        for i in range(0,2):
            
            play_pattern_timed( chord(C4, MAJOR), 0.2)
            sleep(0.20)
            i+=1

        for i in range(0,2):
            play(C4, attack=0, release=1)
            sleep(0.25)
            play(A4,attack=0, release=1)
            sleep(0.25)
            play(E4, attack=0, release=1)
            sleep(0.25)
            play(F4,attack=0, release=1)
            sleep(0.25)
            play(D4,attack=0, release=1)
            sleep(0.25)
            i+=1
        


def live_loop_1(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.notifyAll() #Message to threads
        loop_foo()

def live_loop_2(condition,stop_event):
    while not stop_event.is_set():
        with condition:
            condition.notifyAll() #Wait for message
        loop_bar()

condition = Condition()
stop_event = Event()
live_thread_1 = Thread(name='producer', target=live_loop_1, args=(condition,stop_event))
live_thread_2 = Thread(name='consumer1', target=live_loop_2, args=(condition,stop_event))
live_thread_3 = Thread(name='camm', target=camm)

live_thread_3.start()
