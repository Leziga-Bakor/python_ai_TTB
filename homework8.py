import cv2
import numpy as np
x=np.zeros([256,180,3],dtype=np.uint8)
while True:
    cv2.imshow('my HSV',x)
    cv2.moveWindow('my HSV', 0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cv2.destroyAllWindows()