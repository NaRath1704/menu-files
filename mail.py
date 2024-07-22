import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login('parv23155@gmail.com','dckg ueoc wmsz vidg')

server.sendmail('parv23155@gmail.com','parvagarwal73@gmail.com', 'hello friend')

print('mail sent')

