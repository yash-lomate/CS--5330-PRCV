#Yash Lomate
#09/21/2026
import cv2
import numpy as np
import matplotlib.pyplot as plt

image = 'flowers.jpg'

# Load the original color image
color_image = cv2.imread(image, cv2.IMREAD_COLOR)
if color_image is None:
    raise FileNotFoundError(f'Could not load {image}')

# Convert to grayscale for reference / comparison
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

def show_channel_histogram(title, img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title(title)
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    plt.plot(hist, color='black')
    plt.xlim([0, 256])
    plt.show()

# Histogram equalization on grayscale image (baseline)
gray_equalized = cv2.equalizeHist(gray_image)

# Histogram equalization applied to each BGR color channel independently
b, g, r = cv2.split(color_image)
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)
color_equalized = cv2.merge([b_eq, g_eq, r_eq])

# Show the original and equalized output
panels = [
    (cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB), 'Original color image', None),
    (gray_image, 'Original grayscale', 'gray'),
    (gray_equalized, 'Equalized grayscale', 'gray'),
    (cv2.cvtColor(color_equalized, cv2.COLOR_BGR2RGB), 'Equalized color image (per channel)', None),
]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
for ax, (img, title, cmap) in zip(axes.ravel(), panels):
    ax.imshow(img, cmap=cmap, vmin=0 if cmap else None, vmax=255 if cmap else None)
    ax.set_title(title)
    ax.axis('off')

plt.tight_layout()
plt.show()

# Optional: display histograms for the channels before and after equalization
show_channel_histogram('B channel histogram before equalization', b)
show_channel_histogram('B channel histogram after equalization', b_eq)
show_channel_histogram('G channel histogram before equalization', g)
show_channel_histogram('G channel histogram after equalization', g_eq)
show_channel_histogram('R channel histogram before equalization', r)
show_channel_histogram('R channel histogram after equalization', r_eq)

print('Histogram equalization applied to each RGB channel of flowers.jpg')
print('Color image size:', color_image.shape[1], 'x', color_image.shape[0])
