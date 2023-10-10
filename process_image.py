import cv2
import numpy as np

# loads image
filename = "image.jpg"
img = cv2.imread(filename)

# convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY |
cv2.THRESH_OTSU)[1]
cv2.imshow('Image', thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()