import numpy
import matplotlib.pyplot as plt
import cv2 as cv

def show_image(img):
    try:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    except:
        img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
    plt.figure(figsize=(10,10))
    plt.imshow(img);