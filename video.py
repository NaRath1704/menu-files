import cv2
cap = cv2.VideoCapture(0)
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # If a frame was successfully read, display it
    if ret:
        cv2.imshow('parv', frame)
    
    # Break the loop if the Enter key (key code 13) is pressed
    if cv2.waitKey(100) == 13:
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()

