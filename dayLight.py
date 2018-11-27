#works better in daylight videos and for smoothening effect

import numpy as np
import cv2
import time


(r_avg, g_avg, b_avg) = (None, None, None)
selected_frames = 0

cap = cv2.VideoCapture(0) #replace 0 with location of video
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (800,600))

ret,previous = cap.read()
#ret = True
while (ret):
      ret,image_np = cap.read()
      if(not ret):
          continue   
      
      
      image_np=cv2.resize((image_np),(800,600))
   
      (B, G, R) = cv2.split(image_np.astype("float"))
      
      if r_avg is None:
                    r_avg = R
                    b_avg = B
                    g_avg = G
      else:
                    r_avg = ((selected_frames * r_avg) + (1 * R)) / (selected_frames + 1.0)
                    g_avg = ((selected_frames * g_avg) + (1 * G)) / (selected_frames + 1.0)
                    b_avg = ((selected_frames * b_avg) + (1 * B)) / (selected_frames + 1.0)
      
      selected_frames += 1
      
      avg = cv2.merge([b_avg, g_avg, r_avg]).astype("uint8")
      out.write(avg)
      cv2.imshow('image',avg)
      
      if cv2.waitKey(1) & 0xFF == ord('q'):
             
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break
        
cv2.destroyAllWindows()
cap.release()
out.release()
      
                 