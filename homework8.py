import cv2
import numpy as np
x=np.zeros([256,720,3],dtype=np.uint8)
for row in range(0,256):
    for column in range(0,720):
        x[row,column]=(int(column/4),row,255)
x = cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow('my HSV',x)
    cv2.moveWindow('my HSV', 0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cv2.destroyAllWindows()