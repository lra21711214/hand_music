# coding=utf-8
import cv2
import numpy as np
from hand_tracker import HandTracker
from control import Control,Get_data
from landmark import finger
import subprocess
import shlex

hand_detector = HandTracker("./files/palm_detection_without_custom_op.tflite","./files/hand_landmark.tflite","./files/anchors.csv")
cap = cv2.VideoCapture(0)
before = None

def music(hand, Hand_direction_x, Hand_direction_y, before):
    if hand is not before:
        if hand is 'two' and Hand_direction_x == 'right' and Hand_direction_y == 'up':
            Control.next_track()
            return 'Next track'
        elif hand is 'two' and Hand_direction_x == 'left' and Hand_direction_y == 'up':
            Control.back_track()
            return 'Back track'
        elif hand is 'RankaLee' and Hand_direction_x == 'left' and Hand_direction_y == 'up':
            Control.previous_track()
            return 'Previous track'
        elif hand is 'aloha' and Hand_direction_x == 'right' and Hand_direction_y == 'up':
            Control.playpause()
            return 'Playpause'
        elif hand is 'fox' and Hand_direction_x == 'right' and Hand_direction_y == 'up':
            display = f'osascript -e \'display notification \"{Get_data.current_track_artist()}\" with title \"{Get_data.current_track()}\"\''
            subprocess.Popen(shlex.split(display),stdout=subprocess.PIPE)
            return 'display'

while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        landmark, _ = hand_detector(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if landmark is not None:
            hand, Hand_direction_x, Hand_direction_y = finger(landmark)
            control = music(hand, Hand_direction_x, Hand_direction_y, before)
            before = hand
            for landmark_point in landmark:
                x, y = landmark_point
                cv2.circle(frame, (int(x), int(y)), 2, (255, 0, 0), 4)
        cv2.imshow('Hand', frame)
        if cv2.waitKey(10) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break