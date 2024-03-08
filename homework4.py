import cv2
import time
print(cv2.__version__)
width=640
height=360
myRadius=30
myColor=(0,0,0)
myThick=2
fontH=2
fontT=2
myText='Jesus is Boss'
myFont=cv2.FONT_HERSHEY_DUPLEX
upperLeft=(250,140)
lowerRight=(390,220)
lineW=4
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

tLast = time.time()
time.sleep(.1)
while True:
    dt = time.time() - tLast
    fps = 1/dt
    print(fps)
    tLast = time.time()
    ignore,  frame = cam.read()
    frame[140:220,250:390]=(255,0,0)
    cv2.rectangle(frame,upperLeft,lowerRight,(0,255,0),lineW)
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    cv2.putText(frame,myText,(120,60),myFont,fontH,(0,0,255),fontT)
    cv2.rectangle(frame,(0,0),(120,40),(255,0,255),-1)
    cv2.putText(frame,str(int(fps))+' fps', (5,30), myFont,1,(0,255,255), 2 )    
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()