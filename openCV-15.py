import cv2
import numpy as np
print(cv2.__version__)

evt = 0
xVal = 0
yVal = 0
def mouseClick(event, xPos, yPos, flags, params):
    global evt
    global xVal
    global yVal
    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        xVal = xPos
        yVal = yPos
        evt = event
    if event == cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)

width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam', mouseClick)
while True:
    ignore,  frame = cam.read()
    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        clr = frame[yVal][xVal]
        x[:,:] = clr
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
        cv2.imshow('color picker',x)
        cv2.moveWindow('color picker', width,0)
        evt=0
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()