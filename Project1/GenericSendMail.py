import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('MailBody.html').read_text())
email = EmailMessage()
email['from'] = 'sandygharal'
email['to'] = 'sandygharal27@gmail.com'
email['subject'] = 'My love'
email.set_content(html.substitute({'name': 'Tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sandygharal27@gmail.com', 'Sandyjet4327$')
    smtp.send_message(email)
    print('All done!!!')
