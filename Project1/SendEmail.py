import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'sandygharal'
email['to'] = 'sandygharal27@gmail.com'
email['subject'] = 'My love'
email.set_content('I love you so much :)')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sandygharal27@gmail.com', 'Sandyjet4327$')
    smtp.send_message(email)
    print('All done!!!')
