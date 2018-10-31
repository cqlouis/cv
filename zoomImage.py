import cv2
import math
import numpy as np 
import scipy.misc

img = cv2.imread("test.jpg",0)

cv2.imshow('original image',img)

ah = img.shape[0] 
aw = img.shape[1] 
bh = int(0.5 * ah)
bw = int(0.5 * aw)
 
b = np.zeros([bh,bw])

for i in range(bh):
	for j in range(bw):
		x = math.floor(j/bw * aw - 0.5)
		y = math.floor(i/bh * ah - 0.5)
		b[i,j] = img[y,x] 

scipy.misc.imsave('output.jpg', b)

b = cv2.imread("output.jpg",0)
cv2.imshow('yyyyy', b)
cv2.waitKey(0)
cv2.destroyAllWindows()