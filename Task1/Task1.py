import os
import cv2 as cv
import numpy as np

def ImageDetail(path):
    try:
        os.getcwd
        img = cv.imread(path)
        if(img is None):
            raise FileNotFoundError
        #Gray scale equal intensities of R G B (Achromatic)
        if (round(np.mean(cv.split(img)[0]), 1) == round(np.mean(cv.split(img)[1]), 1)) and \
   (round(np.mean(cv.split(img)[0]), 1) == round(np.mean(cv.split(img)[2]), 1)) and \
   (round(np.mean(cv.split(img)[1]), 1) == round(np.mean(cv.split(img)[2]), 1)):

            
            height,width = img.shape[:2]
            print(f"{height} x {width} pixels")
            print(f"Colour Channel 1")
            fileSize = os.stat(path).st_size
            print(f"File Size {round(fileSize/1024)} KB")

            print(f"Mean Pixel Intensity Gray Scale {round(np.mean(img))}")

            print("Image Type Gray Scale")
        else:
            height,width,colourChannel = img.shape
            print(f"{height} x {width} pixels")
            print(f"Colour Channel {colourChannel}")
            fileSize = os.stat(path).st_size
            print(f"File Size {round(fileSize/1024)} KB")

            blue,green,red = cv.split(img)

            print(f"Mean Pixel Intensity (RGB) {round(np.mean(red)),round(np.mean(green)),round(np.mean(blue))}")

            print("Image Type Coloured")
    except FileNotFoundError:
        print(f"Exception occured File Not Found")


ImageDetail("bridge.jpg") 

