import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('D:/log.jpg',0)

#apply log transformation method
c=255 / np.log(1 + np.max(image))
log_image =  c * (np.log(image + 1))

#specify the data type so that float value will be converted into int
log_image = np.array(log_image, dtype = np.uint8)

plt.imshow(image, cmap='gray')
plt.show

plt.imshow(log_image, cmap='gray')
plt.show
