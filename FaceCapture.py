import cv2

cap=cv2.VideoCapture(0)
i=0
while cap.isOpened():
    ret, frame= cap.read()
    if ret:
        frame= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('capturing', frame)
        cv2.imwrite('samee'+str(i)+'.jpg', frame)
        i+=1

        if i==50 or cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()
