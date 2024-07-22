import cv2

# Replace with the IP address provided by the IP Webcam app
ip_address = input("Enter the ip")

# Construct the video stream URL
stream_url = f"http://{ip_address}/video"

print(f"Attempting to open stream: {stream_url}")


# Open the video stream
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    print("Successfully opened video stream.")
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame.")
            break

        # Display the frame
        cv2.imshow("Mobile Cam Stream", frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the window
    cap.release()
    cv2.destroyAllWindows()

