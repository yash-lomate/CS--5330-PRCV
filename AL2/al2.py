import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# Path to the flower image in Lab1
image = cv2.imread('flowers.jpg', cv2.IMREAD_COLOR)

if image is None:
    raise FileNotFoundError(f'Could not load image: {image}')

# Convert to grayscale for reference
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_equalized = cv2.equalizeHist(gray_image)

# Equalize each color channel separately
b, g, r = cv2.split(image)
b_eq = cv2.equalizeHist(b)
g_eq = cv2.equalizeHist(g)
r_eq = cv2.equalizeHist(r)
color_equalized = cv2.merge([b_eq, g_eq, r_eq])

# Plot results
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axes[0].set_title('Original Color Image')
axes[0].axis('off')

axes[1].imshow(gray_equalized, cmap='gray')
axes[1].set_title('Grayscale Histogram Equalization')
axes[1].axis('off')

axes[2].imshow(cv2.cvtColor(color_equalized, cv2.COLOR_BGR2RGB))
axes[2].set_title('Equalized per RGB Channel')
axes[2].axis('off')

plt.tight_layout()
plt.show()

print('Histogram equalization applied to each RGB channel of flowers.jpg')
print(f'Image size: {image.shape[1]} x {image.shape[0]}')
