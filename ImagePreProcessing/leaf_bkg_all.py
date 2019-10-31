import glob
import cv2
import numpy as np

images = [cv2.imread(file) for file in glob.glob("/home/hashan/PycharmProjects/TeaLeafClassifier/ImagePreProcessing/InputImages/*.jpg")]

for i in images:
    img = i

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, (36, 0, 0), (255, 255,255))

    imask = mask > 0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    # print(i)
    itemindex = np.where(images==i)
    #filename = 'IMG_'+ str(itemindex)+'.JPG'
    #print(filename + '\n' + itemindex)

    #cv2.imwrite(filename, green)
    green = cv2.resize(green, (1080, 720))
    cv2.imshow('Green', green)
    cv2.waitKey(0)
    cv2.destroyAllWindows()