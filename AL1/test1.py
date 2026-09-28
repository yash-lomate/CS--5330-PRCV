#Yash Lomate
#09/21/2026
import cv2
import numpy as np
import matplotlib.pyplot as plt

# # image = cv2.imread('testimage1.png')
# # image2 = cv2.imread('testimage1.png',0)
# # image3 = cv2.imread('testimage1.png',cv2.IMREAD_GRAYSCALE)
# # #print(image[100,100]) #Prints off a single pixel value at (100,100)
# # #print(image2[100,100]) #Prints off a single pixel value at (100,100)
# # #cv2.imshow('image', image)
# # #cv2.imshow('image2', image2)
# # print(image.shape) #Prints the shape of the image
# # height, width, channels = image.shape
# # print(height, width, channels) #Prints the height, width and number of channels in the image

# # '''Create your own image'''
# # #create a random greyscale with values between 0-255 image size 500*500
# # #random_image = np.random.randint(0, 256, (500, 500), dtype=np.uint8)
# # #cv2.imshow('Random Image', random_image)


# # #cv2.waitKey(0)
# # #cv2.destroyAllWindows()

# # '''Histogram of an image'''
# # #print(image.ravel())#change hte image into a 1d array of values
# # #plt.hist(image.ravel(), 256, [0, 256])
# # #plt.show() 

# # random_image = np.random.randint(0, 256, (500, 500), dtype=np.uint8)
# # dark_image = np.random.randint(0, 100, (500, 500), dtype=np.uint8)
# # light_image = np.random.randint(200, 256, (500, 500), dtype=np.uint8)
# # #cv2.imshow('Random Image', random_image)
# # #cv2.imshow('Dark Image', dark_image)
# # cv2.imshow('Light Image', light_image)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # plt.hist(random_image.ravel(), 256, [0, 256])
# # plt.show()

# # #histogram equalization
# # equalized_image = cv2.equalizeHist(light_image)
# # cv2.imshow('Equalized Image', equalized_image)

# # plt.hist(equalized_image.ravel(), 256, [0, 256])
# # plt.show()

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# xray_image = cv2.imread('xray.jpeg', 0)
# cv2.imshow('X-ray Image', xray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# equalized_xray = cv2.equalizeHist(xray_image)
# cv2.imshow('Equalized X-ray Image', equalized_xray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



image = cv2.imread('dog.jpeg', cv2.IMREAD_GRAYSCALE)

# Invert each grayscale pixel: black becomes white and white becomes black.
inverted_image = 255 - image

cv2.imshow('Dog Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cv2.imshow('Inverted Dog Image', inverted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()