import smtplib
import sys
import email.utils
import mailconfig
import getpass


mailserver = mailconfig.smtpservername
mailuser = mailconfig.popusername

From = input('From? ').strip()
To = input('To?   ').strip()
Tos = To.split(';')
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()


text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    text += line

print('Connecting...')
server = smtplib.SMTP_SSL(mailserver, port=465)
mailpasswd = getpass.getpass('Password for %s?' % mailserver)
server.login(mailuser, mailpasswd)
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
    print('Failed recipients:', failed)
else:
    print('No errors.')
print('Bye.')
