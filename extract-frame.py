import cv2
from skimage.metrics import structural_similarity as stsi
import numpy as np
from PIL import Image
import pytesseract as pt
pt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


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

def read_frames():
    path = "C:\\Users\\amole\\Videos\\cs.mp4"
    v = cv2.VideoCapture(path)
    for i in range(0, 1000):
        s, im = v.read()
        if i%10 == 0:
            s = pt.image_to_string(im)
            print(s)

#load_ref_image()

def extract_frame(t):
    path = "C:\\Users\\amole\\Videos\\cs.mp4"
    count = 5000
    v = cv2.VideoCapture(path)
    fr = v.get(cv2.CAP_PROP_FPS)
    print(fr)
    fi = int(fr * t - 1)

    for i in range(0, fi - 1):
        v.read()
    s, i = v.read()
    cv2.imwrite("t.png", i)

def ocr():
    i = Image.open("t.png")
    s = pt.image_to_string(i)
    print(s)



def compare(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    score, diff =stsi(gray1, gray2, full=True)
    print(str(score * 100))

#extract_frames()
#extract_frame(12)
#ocr()
read_frames()
