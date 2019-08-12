import cv2,time,glob

def resizeImage(width, height, img):    #select the area of an image
    img = img[0:width, 0:height]
    return img


def cropImage(CROP_W_SIZE, CROP_H_SIZE, img):   #crop image into given number of pieces
    img = resizeImage(3000, 3000, img)
    img2 = img

    height, width, channels = img.shape

    for ih in range(CROP_H_SIZE):
        for iw in range(CROP_W_SIZE ):

            x = width//CROP_W_SIZE * iw
            y = height//CROP_H_SIZE * ih
            h = (height // CROP_H_SIZE)
            w = (width // CROP_W_SIZE )
            #print(x,y,h,w)
            img = img[y:y+h, x:x+w]

            NAME = str(time.time())
            cv2.imwrite("CROP/" + str(time.time()) +  ".jpg",img)
            img = img2



images = [cv2.imread(file) for file in glob.glob("/home/sanju/Desktop/UCSC 4/SE Project/OpenCV/Test_Project/*.JPG")]

for img in images:
    cropImage(4, 4, img)
