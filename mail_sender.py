import os
import smtplib
import sys


def send_mail(eligible_persons):
    user = os.environ['sendermail']  # from email
    passwd = os.environ['senderpassword']

    to = os.environ['receiveremail']  # to address
    body = eligible_persons

    smtp_server = 'smtp.yandex.com'
    port = '465'  # change this depending upon the smtp server

    try:
        server = smtplib.SMTP_SSL(smtp_server, port)
        print(sys.version)
        server.ehlo()
        server.login(user, passwd)
        subject = 'Reminder List'
        msg = 'From: {0}\r\nTo: {1}\r\nSubject:{2}\r\n\r\n'.format(user, to, subject) + body
        server.sendmail(user, to, msg)
        print("Sending Email")
        sys.stdout.flush()
        server.quit()
        print('\n Done emailing!')
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPHeloError, smtplib.SMTPSenderRefused, smtplib.SMTPDataError) as e:
        print('\n Error other than authentication!')
        return 0
    except smtplib.SMTPAuthenticationError:
        print('\n The username or password you entered is incorrect.')
        return 0
    return 1
