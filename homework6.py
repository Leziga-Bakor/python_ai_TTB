import cv2
print(cv2.__version__)
evt = 0
evt2 = 0
pnt1 = (100,200)
pnt2 = (120,240)
def mouseClick(event, xPos,yPos,flags,params):
    global evt, evt1, evt2
    global pnt, pnt1a, pnt2a
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Mouse Event was: ',event)
        print('at Position', xPos, yPos)
        pnt1a =(xPos, yPos)
        evt1 = event
    if event==cv2.EVENT_LBUTTONUP:
        print('Mouse Event was: ', event)
        print('at Position',xPos,yPos)
        evt2=event
        pnt2a =(xPos, yPos)
    if event==cv2.EVENT_RBUTTONDOWN:
        print('Right button up ', event)
        evt = event
        pnt=(xPos,yPos)
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
    if  evt2 == 4:
        # print(pnt1[0],pnt2[0])
        # frameROI = frame[pnt1[0]:pnt2[0],pnt1[1]:pnt2[1]]
        pnt1 = pnt1a
        pnt2 = pnt2a
     
    frameROI = frame[pnt1[0]:pnt2[0],pnt1[1]:pnt2[1]]

    cv2.imshow('my ROI', frameROI)
    cv2.moveWindow('my ROI', 1280,0)        
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()