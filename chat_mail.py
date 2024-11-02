import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
import time
from time import asctime

fromaddr = 'email1'
toaddr = 'email2'
subject = 'Automatic mail'
body = 'This is a test mail'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)  # Port 587 for TLS connection
server.starttls()  # Initiating TLS encryption
server.login(fromaddr, 'password')

text = msg.as_string()
for i in range(0,5):
    server.sendmail(fromaddr, toaddr, text)
    print('mail %d send successfully',i)

server.quit()

print('All Mails sent successfully!')
