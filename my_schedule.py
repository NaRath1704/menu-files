import smtplib
import schedule
import time

def send_email():
    from_address = 'parv23155@gmail.com'
    to_address = 'parvagarwal73@gmail.com'
    subject = 'Scheduled Email'
    body = 'This email was sent at a scheduled time.'

    email_message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_address, 'dckg ueoc wmsz vidg')
        server.sendmail(from_address, to_address, email_message)
        server.quit()
        print(f"Successfully sent email message to {to_address}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def schedule_email(time_str):
    schedule.every().day.at(time_str).do(send_email)
    print(f"Email scheduled at {time_str} every day.")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Set the time to send email here
    time_str = "10:44"
    schedule_email(time_str)

    run_scheduler()

