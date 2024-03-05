import cv2
print(cv2.__version__)
import numpy as np

boardSize = int(input('What size is your board? '))
numSquares=int(input('How many squares? '))
squareSize = boardSize/numSquares
while True:

    frame = np.zeros([250,250,3],dtype=np.uint8)
    frame[:,:] = (0,0,255)
    for i in range(0,250,50):
        for j in range(0,250,50):
            frame[i:i+25,j:j+25]=(0,0,0)
            frame[i+25:i+50,j+25:j+50]=(0,0,0)
    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break