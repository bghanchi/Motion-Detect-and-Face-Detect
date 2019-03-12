import cv2,time

face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)

a=0
while 1:
    a+=1
    bool,images=video.read()

    #print(bool,images)

    faces=face.detectMultiScale(images,scaleFactor=1.5,minNeighbors=2)

    #print(img)
    for x,y,w,h in faces:
    #    print(x,y,w,h)
        images=cv2.rectangle(images,(x,y),(x+w,y+h),(255,0,255),3)


    resize=cv2.resize(images,(900,600))
    cv2.imshow("capturing",resize)
    key=cv2.waitKey(1)

#time.sleep(3)

video.release()

cv2.destroyAllWindows()