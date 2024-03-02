import cv2
# print(cv2.__version__)

rows = int(input('Boss, how many rows do you want? '))
columns = int(input('And how many columns? '))
width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame = cv2.resize(frame, (int(width/columns), int(height/columns)))
    for i in range(rows):
        for j in range(columns):
            windowName = 'Window'+str(i)+' * '+str(j)
            cv2.imshow(windowName, frame)
            cv2.moveWindow(windowName,int(width/columns)*j, int(height/columns)*i)
    
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()