import cv2

face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread('abb.jpg',1)

#img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face.detectMultiScale(img,scaleFactor=1.5,minNeighbors=2)

#print(img)
for x,y,w,h in faces:
#    print(x,y,w,h)
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

#print(img)

resize=cv2.resize(img,(900,600))

cv2.imshow('mami',resize)

cv2.waitKey(0)

cv2.destroyAllWindows()    