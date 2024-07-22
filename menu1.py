import os

def execute_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Execute the file
        exec(open(file_path).read())
    else:
        print(f"Error: File '{file_path}' does not exist.")

def main():
    while True:
    	
        print("\nChoose which file to execute:")
        print("1. SEND SMS to Phone Number")
        print("2. Ivr call")
        print("3. Send Whastapp Message")
        print("4. Send Mail")
        print("5. Google search")
        print("6. Live video")
        print("7. Insta post")
        print("8. Take your photo and crop it in grayscale with your name on it")
        print("9. Write a code in python to send g mail and ask receivers mail, subject, and body of the message")
        print("10. Convert Text to speech")
        print("11. Create a numpy array")
        print("12.  launch an aws instance with help of peace sign")
        print("13. Video stream through phone")
        print("14. Find purpose in life")
        print("15. launch an aws instance ")
        print("16. Find purpose in life")
        print("17. Find purpose in life")
        print("0. Exit")

        choice = input("Enter your choice (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14): ")

        if choice == '0':
            print("Exiting the menu.")
            break
        elif choice == '1':
            file_path = 'sms.py'  # Replace with the path to your first Python file
            execute_file(file_path)
        elif choice == '2':
            file_path = 'call.py'  # Replace with the path to your second Python file
            execute_file(file_path)
        elif choice == '3':
            file_path = 'whats.py'  # Replace with the path to your third Python file
            execute_file(file_path)
        elif choice == '4':
            file_path = 'mail.py'  # Replace with the path to your fourth Python file
            execute_file(file_path)
        elif choice == '5':
            file_path = 'google.py'  # Replace with the path to your fifth Python file
            execute_file(file_path)
        elif choice == '6':
            file_path = 'video.py'  # Replace with the path to your sixth Python file
            execute_file(file_path)
        elif choice == '7':
            file_path = 'insta.py'  # Replace with the path to your seventh Python file
            execute_file(file_path)
        elif choice == '8':
            file_path = 'gomail.py'  # Replace with the path to your eighth Python file
            execute_file(file_path)
        elif choice == '9':
            file_path = 'mail2.py'  # Replace with the path to your ninth Python file
            execute_file(file_path)
        elif choice == '10':
            file_path = 'ttos.py'  # Replace with the path to your tenth Python file
            execute_file(file_path)
        elif choice == '11':
            file_path = 'arry.py'  # Replace with the path to your eleventh Python file
            execute_file(file_path)
        elif choice == '12':
            file_path = 'aws_finger.py'  # Replace with the path to your twelfth Python file
            execute_file(file_path)
        elif choice == '13':
            file_path = 'ipcam.py'  # Replace with the path to your thirteenth Python file
            execute_file(file_path)
        elif choice == '14':
            file_path = 'aim.py'  # Replace with the path to your fourteenth Python file
            execute_file(file_path)
        elif choice == '15':
            file_path = 'aws.py'  # Replace with the path to your fourteenth Python file
            execute_file(file_path)
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()

