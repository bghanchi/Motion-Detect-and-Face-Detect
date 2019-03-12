import cv2,time


video=cv2.VideoCapture(0)

f_images=None


while 1:
    bool,frame=video.read()

    images = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    images=cv2.GaussianBlur(images,(21,21),0)
 
    if f_images is None:
        f_images=images
        continue


    delta_image=cv2.absdiff(f_images,images)

    thresh_delta=cv2.threshold(delta_image,30,255,cv2.THRESH_BINARY)[1]

    thresh_delta=cv2.dilate(thresh_delta,None,iterations=0)

#     (_,cnts,_)=cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    (cnts,_) = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for a in cnts:

       if cv2.contourArea(a)<1000:
           continue

       (x,y,w,h)=cv2.boundingRect(a)
       images=cv2.rectangle(images,(x,y),(x+w,y+h),(0,0,255),3) 


#    cv2.imshow("frame",frame)
    cv2.imshow("image",images)
#    cv2.imshow("Delta_image",delta_image)
#    cv2.imshow("thresh_delta",thresh_delta)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    

video.release()
cv2.destroyAllWindows()

