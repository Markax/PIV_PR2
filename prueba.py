import numpy as np
import cv2, sys

A=cv2.imread(sys.argv[1])

if (A==None):
	print (" Error al cargar imagen ")	
	sys.exit()

r=cv2.imshow('image',A)

B=cv2.imwrite(sys.argv[2])

cv2.waitKey(0)
cv2.destroyAllWindows()