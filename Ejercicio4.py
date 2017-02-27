import cv2 , numpy as np
import sys

cap = cv2.VideoCapture(sys.argv[1])

font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(cap,'Guillermo Martinez Lledo',(100, 100), font, escala, color,grueso ,cv2.LINE_AA)

while(cap.isOpened()):
	ret, frame = cap.read()
	
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
cap.release ()
cv2.waitKey(0)
cv2.destroyAllWindows ()