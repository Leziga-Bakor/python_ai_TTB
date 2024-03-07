import cv2
print(cv2.__version__)
width=640
height=360
circle_colour = (0,0,255)
circle_radius = 25
mythick = 2
mytext = 'JESUS is Lord'
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame[140:220,280:360]=(255,0,0)
    cv2.rectangle(frame,(280,140),(360,220),(0,255,0),2)
    cv2.circle(frame,(int(width/2),int(height/2)),circle_radius,circle_colour,mythick)
    cv2.putText(frame, mytext, (120,60), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()