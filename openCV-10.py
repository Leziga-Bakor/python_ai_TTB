import cv2
print(cv2.__version__)
def mouseClick(event, xPos,yPos,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was: ',event)
        print('at Position', xPos, yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event was: ', event)
        print('at Position',xPos,yPos)
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
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()