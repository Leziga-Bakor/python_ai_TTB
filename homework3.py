import cv2
print(cv2.__version__)
import numpy as np

boardSize = int(input('What size is your board? '))
numSquares=int(input('How many squares? '))
squareSize = int(boardSize/numSquares)

lightColor = (0,0,255)
darkColor = (0,0,0)
nowColor = darkColor


'''
while True:

    frame = np.zeros([boardSize,boardSize,3],dtype=np.uint8)
    frame[:,:] = lightColor
    for i in range(0,boardSize,squareSize*2):
        for j in range(0,boardSize,squareSize*2):
            frame[i:i+squareSize,j:j+squareSize]=darkColor
            frame[i+squareSize:i+squareSize*2,j+squareSize:j+squareSize*2]=darkColor
    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
'''

#Top tech boy solution
while True:
    frame =np.zeros([boardSize,boardSize,3],dtype=np.uint8)

    for row in range(numSquares):
        for col in range(numSquares):
            frame[squareSize*row:squareSize*(row+1),squareSize*col:squareSize*(col+1)] = nowColor
            if nowColor == darkColor:
                nowColor = lightColor
            else:
                nowColor=darkColor
        if nowColor == darkColor:
            nowColor = lightColor
        else:
            nowColor=darkColor

    cv2.imshow('my window',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break