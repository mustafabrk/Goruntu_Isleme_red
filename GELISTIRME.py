from calendar import c
import cv2 as cv
import numpy as np


video = cv.VideoCapture(0) 

def morphology(a, b):
    kernel = np.ones((a,a), np.uint8)
    opening = cv.morphologyEx(b, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(b, cv.MORPH_CLOSE, kernel)
    b = cv.bitwise_and(opening, closing)
    return b

def blurHSV(f, a, b):
    c = cv.GaussianBlur(f, (a,a), b)
    d = cv.cvtColor(c, cv.COLOR_BGR2HSV)
    return d

def renkAraligi():
    pass

while True: # her bir resmi tek tek okuyacak olan sonsuz döngüyü açıyoruz
    (grabbed, frame) = video.read()
    if not grabbed:
        break
    
    frame = cv.resize(frame, (960, 540)) # Ekranda fazla yer kaplamaması için görüntüyü küçültüyor.

    hsv = blurHSV(frame, 21, 0)

    altDeger = np.array([0, 200, 60], dtype = "uint8")  
    ustDeger = np.array([35, 255, 255], dtype = "uint8") # Değişiklikler diziye aktarıldı

    mask = cv.inRange(hsv, altDeger, ustDeger) # kırmızı içermeyen kısımlar maskeleniyor

    cikti = cv.bitwise_and(frame, hsv, mask = mask) # verilen iki görüntünün birleşmesinden yeni görüntü elde eden bir dizi döndürüyor
    cikti = morphology(5, cikti)

    cv.imshow("output", cikti) # Videonun son halinin her bir frame'ini gösteriyor

    if cv.waitKey(1) & 0xFF == ord('q'): # q tuşuna basınca döngüyü kırıp videoyu kapatıyor
        break

cv.destroyAllWindows()
video.release()