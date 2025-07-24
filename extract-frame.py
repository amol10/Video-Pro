import cv2
from skimage.metrics import structural_similarity as stsi
import numpy as np

def load_ref_image():
    rimg = cv2.imread("r.jpg")
    cv2.imwrite("rc.jpg", rimg)
    return rimg

def extract_frames():
    path = "pyin.mp4"
    count = 5000
    v = cv2.VideoCapture(path)
    rimg = load_ref_image()

    for i in range(0, count, 500):
        s, img = v.read()
        compare(rimg, img)
        #cv2.imwrite("%i.jpg"%i, img)

#load_ref_image()

def compare(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, diff =stsi(gray1, gray2, full=True)
    print(str(score * 100))

extract_frames()