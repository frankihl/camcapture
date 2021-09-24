import cv2
cap = cv2.VideoCapture('http://admin:hemligt1@192.168.1.180/video/mjpg.cgi')

while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  if cv2.waitKey(1) == 27:
    exit(0)
