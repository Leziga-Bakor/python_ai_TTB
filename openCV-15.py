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
cv2.namedWindom('my Webcam')
cv2.setMouseCallback('my Webcam', mouseClick)
while True:
    ignore,  frame = cam.read()
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()