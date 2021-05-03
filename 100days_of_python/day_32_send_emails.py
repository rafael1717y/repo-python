import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = 'smtp.gmail.com'
port = 587
user = 'rafael1717yy@gmail.com'
password = 'Insta1211@'

server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(user=user, password=password)

message = 'Olá'
email_msg = MIMEMultipart()
email_msg['From'] = "rafael.a.gomes@rfb.gov.br"
email_msg['To'] = 'rafael.a.gomes@rfb.gov.br'
email_msg['Subject'] = 'teste'
email_msg.attach(MIMEText(message, 'plain'))

server.sendmail(from_addr=email_msg['From'], to_addrs=email_msg['To'], msg='Teste automacao')
server.quit()


"""
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="rafaelufjf@gmail.com",
                    msg="Subject:Hello\n\nThis si the body of the email")
connection.close()
"""
