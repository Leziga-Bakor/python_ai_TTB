import cv2
# print(cv2.__version__)
cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    
    cv2.imshow('colour 1',frame)
    cv2.moveWindow('colour 1',0,0)

    cv2.imshow('colour 2',frame)
    cv2.moveWindow('colour 2',650,520)

    cv2.imshow('my Webcam',grayFrame)
    cv2.moveWindow('my Webcam',650,0)

    cv2.imshow('my Webcam 2',grayFrame)
    cv2.moveWindow('my Webcam 2',0,520)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()