import numpy as np
import cv2, sys

X=int(sys.argv[1])
Y=int(sys.argv[2])
N=sys.argv[3]

"linea"
Img=np.zeros((X, Y, 3), np.uint8)

"Polilinea"
cv2.line(Img, (0, 100), (255, 100), (255,0,0), 3)
pts = np.array([[10,5], [20,30], [70,20], [50,10]],
np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(Img, [pts], True, (0,0,255), 4)

"Circulo"
cv2.circle(Img, (100, 100), 100, (100,50,100), 10)

"Circunferencia"
cv2.circle(Img, (200, 100), 0, (100,250,60), 100)

r=cv2.imshow('image',Img)

cv2.imwrite(N, Img) 
cv2.waitKey(0)
cv2.destroyAllWindows()