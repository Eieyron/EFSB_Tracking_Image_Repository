import cv2
import numpy as np 
import sys
# import copy

def draw_rect(frame, box, thickness=2):

	x,y,w,h = box
	cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), thickness)


# def label_image(image_name, objects_to_track)
num_of_objects = 5
bboxes = []

image = cv2.imread('1.jpg',1)
temp = cv2.imread('1.jpg',1)

box = (1,1,1,1)

while box != (0,0,0,0):

	box = cv2.selectROI(temp, False, False)

	print(box) 

	bboxes.append(box)

	draw_rect(temp, box)


# print(bboxes)