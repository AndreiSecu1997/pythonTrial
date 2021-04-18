import sys
import requests
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

from formatting import format_msg
from send_mail import send_mail

sender = 'people2andreisecu@gmail.com'
receivers = ['people2andreisecu@gmail.com', 'people2andreisecu@gmail.com']
body_of_email = 'Text to be displayed in the email'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'Subject line'
msg['From'] = sender
msg['To'] = ','.join(receivers)

def attachFile(fileRoute):
    s = "s"

def send(host, username, password):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login('people2andreisecu@gmail.com', 'c2007020022908')
    msg = MIMEMultipart()
    # file2 = open(r"D:\Text\MyFile2.txt", "w+")
    msg.attach(MIMEText(open("text.txt").read()))
    try:
        s.sendmail(sender, receivers, msg.as_string())
        sent = True
    except:
        sent = False
    finally:
        s.quit()
    return sent


if __name__ == "__main__":
    print(sys.argv)
    name = "people2andreisecu@gmail.com"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, email, True)
    print(response)