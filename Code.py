import numpy as np 
import argparse
import time
import cv2


count=1

blueLower = np.array([10, 67, 0], dtype = "uint8")
blueUpper = np.array([255, 210, 50], dtype = "uint8")
camera = cv2.VideoCapture("/home/chetan/Documents/object/object.mov")
while True:

  (grabbed, frame) = camera.read()
  if not grabbed:
    break
  blue = cv2.inRange(frame, blueLower, blueUpper)
  blue = cv2.GaussianBlur(blue, (3, 3), 0)
  (_, cnts, _) = cv2.findContours(blue.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  if len(cnts) > 0:
    cnt = sorted(cnts, key = cv2.contourArea, reverse = True) [0]
    rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
    cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
  cv2.imshow("Tracking", frame)
  if count>50:

      cv2.imwrite("frame%d.jpg" % count, frame)
  cv2.imshow("Binary", blue)
  if count>50:

      cv2.imwrite("blue%d.jpg" % count, blue)
  time.sleep(0.025)
  count=count+1
  if cv2.waitKey(1) & 0xFF == ord("q"):
    break
camera.release()
cv2.destroyAllWindows() 

