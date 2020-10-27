# 把输入图像缩小一半
# import cv2
# import math
# import numpy as np 
# import scipy.misc

# img = cv2.imread("test.jpg",0)

# cv2.imshow('original image',img)

# ah = img.shape[0] 
# aw = img.shape[1] 
# bh = int(0.5 * ah)
# bw = int(0.5 * aw)
 
# b = np.zeros([bh,bw])

# for i in range(bh):
# 	for j in range(bw):
# 		x = math.floor(j/bw * aw - 0.5)
# 		y = math.floor(i/bh * ah - 0.5)
# 		b[i,j] = img[y,x] 

# scipy.misc.imsave('output.jpg', b)

# b = cv2.imread("output.jpg",0)
# cv2.imshow('yyyyy', b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 任意比例缩放输入图像
import cv2
import numpy as np

def nearest_neighbor_resize(img, new_w, new_h):
    # height and width of the input img
    h, w = img.shape[0], img.shape[1]
    # new image with rgb channel
    ret_img = np.zeros(shape=(new_h, new_w, 3), dtype='uint8')
    # scale factor
    s_h, s_c = (h * 1.0) / new_h, (w * 1.0) / new_w

    # insert pixel to the new img
    for i in range(new_h):
        for j in range(new_w):
            p_x = int(j * s_c)
            p_y = int(i * s_h)

            ret_img[i, j] = img[p_y, p_x]

    return ret_img

def test( w, h, img = 'F:/rafa.jpg'):
    img = cv2.imread(img)
    ret_img = nearest_neighbor_resize(img, w, h)
    cv2.imshow("source image", img)
    cv2.imshow("after bilinear image", ret_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

test(1950, 1008)


