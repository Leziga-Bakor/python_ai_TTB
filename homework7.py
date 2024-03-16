import cv2
print(cv2.__version__)
def myCallBack1(val):
    global xPos
    print('xPos: ',val)
    xPos = val
    # if val == 0:
    #     val = 1
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH, width/val)
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height/val)
    
def myCallBack2(val):
    global yPos
    print('yPos: ', val)
    yPos = val
    
# def myCallBack3(val):
#     global myRad
#     print('Radius: ', val)
#     myRad = val
# def myCallBack4(val):
#     global myThick
#     print('thickness: ', val)
#     myThick = val
width=1280
height=720
xPos = 0
yPos = 0
myRad = 25
myThick = 1
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,150)
cv2.moveWindow('myTrackbars', width, 0)
cv2.createTrackbar('xPos', 'myTrackbars', 0,2000, myCallBack1)
cv2.createTrackbar('yPos', 'myTrackbars', 0,1000, myCallBack2)
# cv2.createTrackbar('radius', 'myTrackbars', myRad ,int(height/2), myCallBack3)
# cv2.createTrackbar('thickness', 'myTrackbars', myThick ,7, myCallBack4)

while True:
    ignore,  frame = cam.read()
    # if myThick == 0:
    #     myThick = (-1)
    # cv2.circle(frame, (xPos,yPos),myRad,(255,0,0),myThick)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',xPos,yPos)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()