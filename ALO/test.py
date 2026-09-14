import matplotlib
import numpy
import pandas
import sklearn
import cv2

print("All libraries installed successfully.")


image = cv2.imread('testimage1.png', 0)
if image is None:
	raise FileNotFoundError('Could not load testimage1.png')

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#To run anytime 
#source .venv/bin/activate
#python your_file.py