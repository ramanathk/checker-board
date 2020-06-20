import numpy as np

import cv2

n=int (25)
b = np.ones([200,200],dtype = 'uint8')*255
for i in range(n,200,n*2):
        for j in range (n,200,n*2):

           b[j-n:j,i-n:i] = 0
           b[j:j+n,i:i+n] = 0
cv2.imshow(' 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()  
