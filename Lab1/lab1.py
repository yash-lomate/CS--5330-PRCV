#Yash Lomate
#09/21/2026
# Lab 1: converting a color image to grayscale using two different methods

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Name of the input image
image = 'flowers.jpg'

# Read the original color image and the grayscale version using OpenCV
# IMREAD_COLOR loads the image in BGR format
color_image = cv2.imread(image, cv2.IMREAD_COLOR)
# IMREAD_GRAYSCALE loads a single-channel grayscale image directly
builtin_image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

# Check whether the image files were loaded correctly
if color_image is None or builtin_image is None:
    raise FileNotFoundError(f'Could not load {image}')

# OpenCV grayscale conversion reference (used for comparison in the lab)
cvt = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

# Split the color image into its red, green, and blue channels
# OpenCV uses BGR order, not RGB
b, g, r = cv2.split(color_image)

# Convert channel arrays to float for calculation accuracy
b = b.astype(np.float64)
g = g.astype(np.float64)
r = r.astype(np.float64)

# Helper function to clip values to 0-255 and convert back to uint8
# This ensures valid image intensity values after calculation
def to_unit8(arr):
    arr = np.clip(arr, 0, 255)
    return arr.astype(np.uint8)

# Method 1: Average method
# Each channel contributes equally to the final grayscale value
average = to_unit8((b + g + r) / 3)

# Method 2: NTSC method (standard luminance conversion)
# This uses different weights because human eyes are more sensitive to green
ntsc = to_unit8(0.299 * r + 0.587 * g + 0.114 * b)

# This function was used earlier for comparison testing.
# It is left in the file for reference, but not used in the final output.
def compare(name, img, ref, ref_name):
    diff = cv2.absdiff(img, ref)
    print(f"  {name:8s} vs {ref_name:18s} "
          f"max={diff.max():3d}  mean={diff.mean():6.3f}  "
          f"within +/-1: {(diff <= 1).mean() * 100:5.1f}%")
    return diff

# Print image dimensions for reference
print(f"Image: {color_image.shape[1]} x {color_image.shape[0]}\n")
print("Showing the four required result images.")

# Build the list of images to display
# 1. Original color image
# 2. Grayscale image from OpenCV
# 3. Average method grayscale image
# 4. NTSC method grayscale image
panels = [
    (cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB), "Original", None),
    (builtin_image, "Grayscale", 'gray'),
    (average, "Average method", 'gray'),
    (ntsc, "NTSC method", 'gray'),
]

# Display the four images in a 2x2 grid
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for ax, (img, title, cmap) in zip(axes.ravel(), panels):
    ax.imshow(img, cmap=cmap, vmin=0 if cmap else None,
              vmax=255 if cmap else None)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()

# Older code kept for reference only
# cv2.imshow('Flowers', builtin_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Average Method formula: (B + G + R) / 3
# b,g,r = cv2.split(image)
# average = b+g+r/3

# average = b/3 + g/3 + r/3
