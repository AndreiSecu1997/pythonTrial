import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from pathlib import Path

sender = 'people2andreisecu@gmail.com'
to = 'people2andreisecu@gmail.com, altcineva@gmail.com'
subject = 'subject topic'
message = 'bla bla bla content'
files = ['text.txt','template.pptx','test.jpg']
server = 'smtp.gmail.com'
port = 465
username = 'people2andreisecu@gmail.com'
passsword = 'c2007020022908'
use_tls = True


def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
              use_tls=True):
    """Compose and send email with provided info and attachments.

    Args:
        send_from (str): from name
        send_to (list[str]): to name(s)
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
    """
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(True)
    msg['Subject'] = subject

    msg.attach(MIMEText(message))

    for path in files:
        print(Path(path).stat().st_size)
        if Path(path).stat().st_size > 2097152: continue
        print(Path(path).stat().st_size)
        part = MIMEBase('application', "octet-stream")
        with open(path, 'rb') as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(Path(path).name))
        msg.attach(part)

    smtp = smtplib.SMTP_SSL(server, port)
    smtp.login(username, password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.quit()

if __name__ == "__main__":
    send_mail(sender, to, subject, message, files, server, port, username, passsword, use_tls)
