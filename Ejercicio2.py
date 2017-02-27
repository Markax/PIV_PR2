import numpy as np
import cv2, sys

A=cv2.imread(sys.argv[1])

if (A==None):
	print (" Error al cargar imagen ")	
	sys.exit()

r=cv2.imshow('image',A)

info=A.shape
alto = info[1]
ancho = info[0]
bandas = info[2]
B=np.zeros((alto, ancho, bandas), np.uint8)

for i in range(0, alto, 1):
	for j in range(0, ancho, 1):
		B.itemset((i,-j,0),A.item(i,j,0))
		B.itemset((i,-j,1),A.item(i,j,1))
		B.itemset((i,-j,2),A.item(i,j,2))


s=cv2.imshow('rotada',B)
cv2.imwrite(sys.argv[2], B) 

cv2.waitKey(0)
cv2.destroyAllWindows()