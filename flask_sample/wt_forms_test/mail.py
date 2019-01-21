import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = 'kosakaboat@gmail.com'
MY_PASSWORD = 'norionorio'

def create_message(to_addr, subject, body):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = FROM_ADDRESS
	msg['To'] = to_addr
	msg['Date'] = formatdate()
	return msg


def send(msg):
	smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpobj.ehlo()
	smtpobj.starttls()
	smtpobj.ehlo()
	smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
	smtpobj.sendmail(FROM_ADDRESS, msg['To'], msg.as_string())
	smtpobj.close()


if __name__ == '__main__':

	to_addr = 'kosakaboat@gmail.com'
	subject = 'test'
	body = 'test'

	msg = create_message(to_addr, subject, body)
	send(msg)