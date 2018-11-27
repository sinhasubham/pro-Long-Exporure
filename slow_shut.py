import numpy as np
import cv2
import time


def blender(curr , prev):
    height, width,depth = curr.shape
    x=0.5  #change value of x to change the weights of previous and current frame
    for i in range(0, height):
         for j in range(0, width):
             for k in range(0,depth):
                 curr[i,j,k]=(x*curr[i,j,k]) + ((1-x)* prev[i,j,k])
    return curr
                 


def longex(curr , prev):
    height, width,depth = curr.shape
    for i in range(0, height):
         for j in range(0, width):
             for k in range(0,depth):
                 if curr[i,j,k]< prev[i,j,k]:
                     curr[i,j,k]=prev[i,j,k]
    return curr
           
      
cap = cv2.VideoCapture(0) #replace 0 with location of video

ret,previous = cap.read()
previous=cv2.resize((previous),(800,600))
image_np=previous
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (800,600))

while (ret):
      ret,image_np = cap.read()
      if(not ret):
          continue
      
      
      image_np=cv2.resize((image_np),(800,600))
      
      image_np=longex(image_np,previous)   #change longex to blender for blending effect
      #image_np=cv2.medianBlur(image_np,1)
      
      previous=image_np
      out.write(image_np)
      cv2.imshow('image',image_np)
      if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('img.PNG',image_np)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
        
cv2.destroyAllWindows()
cv2.imwrite('img.PNG',image_np)
out.release()
cap.release()
      
      
                 