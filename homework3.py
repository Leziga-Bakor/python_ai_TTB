import cv2
print(cv2.__version__)
import numpy as np

boardSize = int(input('What size is your board? '))
numSquares=int(input('How many squares? '))
squareSize = int(boardSize/numSquares)
while True:

    frame = np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    frame[:,:] = (0,0,255)
    for i in range(0,boardSize,squareSize*2):
        for j in range(0,boardSize,squareSize*2):
            frame[i:i+squareSize,j:j+squareSize]=(0,0,0)
            frame[i+squareSize:i+squareSize*2,j+squareSize:j+squareSize*2]=(0,0,0)
    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break