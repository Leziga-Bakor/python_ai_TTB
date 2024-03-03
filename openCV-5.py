import cv2
print(cv2.__version__)
import numpy as np
while True:

    frame = np.zeros([250,250],dtype=np.uint8)
    frame[:,:] = 125
    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break