import smtplib
from email.message import EmailMessage
import os
sender_email = 'parv23155@gmail.com'
sender_password = "dckg ueoc wmsz vidg "
recipient_email = input("Please enter mail to send")
subject = input("Enter the subject: ")
body = input("Enter the body: ")
msg = EmailMessage()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject
msg.set_content(body)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
server.send_message(msg)
server.quit()
print("Email sent successfully")
