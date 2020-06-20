import numpy as np
import cv2
b = np.ones([200,200],dtype = 'uint8')*255
for i in range(25,200,25*2):
        for j in range (25,200,25*2):

           b[j-25:j,i-25:i] = 0
           b[j:j+25,i:i+25] = 0
cv2.imshow(' 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()  
