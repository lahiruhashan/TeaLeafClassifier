import cv2
import numpy as np

im = cv2.imread('bunch.jpg')
kernel = np.array([[-1,-1,-1,-1,-1],[-1,2,2,2,-1],[-1,2,8,2,-1],[-1,2,2,2,-1],[-1,-1,-1,-1,-1]]) * (1/8)
im_sharpened = cv2.filter2D(im, -1, kernel)

cv2.imwrite('bunch_sharp.jpg', im_sharpened)
cv2.imshow('SHRP', im_sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
