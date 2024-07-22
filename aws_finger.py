import cv2
from cvzone.HandTrackingModule import HandDetector
import requests
import boto3
from flask import Flask, request

app = Flask(__name__)

@app.route('/ec2')
def launch_ec2_instance():
    # Create a session using boto3
    session = boto3.Session(
        aws_access_key_id='AKIA3FLD42IA55P3VPV5',
        aws_secret_access_key='b3Fbd8FzisIrkQDQsW8U8D4gac7k4gMNqnW8GtZv',
        region_name='ap-south-1'  # Replace with your desired region
    )   

    # Use the session to create an EC2 resource
    ec2 = session.resource('ec2')

    # Launch the EC2 instance
    instances = ec2.create_instances(
        ImageId='ami-0ec0e125bb6c6e8ec',  # Replace with a valid AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',  # Replace with the desired instance type
        SecurityGroupIds=['sg-0626809b2ee8efe6d'],  # Replace with your security group ID
    )

    # Print the ID of the new instance
    for instance in instances:
        return f"Instance ID: {instance.id}"

if __name__ == '__main__':
    import threading

    # Start the Flask app in a separate thread
    threading.Thread(target=lambda: app.run(host='0.0.0.0', port=80, debug=True, use_reloader=False)).start()

    # Initialize the webcam
    cap = cv2.VideoCapture(0)

    # Initialize the hand detector
    detector = HandDetector(maxHands=1)

    while True:
        # Capture the frame from the webcam
        success, img = cap.read()

        # Detect hands in the frame
        hands, img = detector.findHands(img)

        if hands:
            # Get the first hand detected
            hand = hands[0]

            # Check for a specific gesture (e.g., the "peace" sign)     
            fingers = detector.fingersUp(hand)
            if fingers == [0, 1, 1, 0, 0]:  # Index and middle fingers up, others down
                print("Peace gesture detected")
                
                # Send a request to the Flask API to launch EC2 instance
                response = requests.get('http://127.0.0.1:80/ec2')
                print(response.text)

        # Display the frame
        cv2.imshow("Image", img)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()
    