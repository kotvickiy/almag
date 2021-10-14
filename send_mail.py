import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(list_text,
              # recipients=['tasha1234@mail.ru', 'kotvickiy@inbox.ru'],
              recipients=['kotvickiy@inbox.ru'],
              subject = '',
              server='smtp.mail.ru',
              user='test-70@internet.ru',
              password='6sBPYzGrhLRZmVy1xnJi'):
    
    sender = user

    text = ''
    for i in list_text:
        for j in i.values():
            text += str(j) + '\n'
        text += '\n\n'


    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender

    part_text = MIMEText(text, 'plain')

    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()
