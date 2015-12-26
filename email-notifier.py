import sys
import argparse
import smtplib

parser = argparse.ArgumentParser(prog='email-notifier')
parser.add_argument('-u', '--user', required=True, help='user from')
parser.add_argument('-t', '--to', required=True, help='user to')
parser.add_argument('-m', '--message', required=True, help='message text')
parser.add_argument('-c', '--check', action="store_true", help='check login')
parser.add_argument('-p', '--password', required=True, help='user password')
parser.add_argument('-s', '--subject', default='unotify', 
                    help='subject (default = "unotify")')
parser.add_argument('-d', '--host', default='smtp.gmail.com', 
                    help='smtp domain (default = "smtp.gmail.com")')
parser.add_argument('-r', '--port', default='587', 
                    help='smtp port ((default = 587))')
args = parser.parse_args()

def send_email(user, pwd, recipient, subject, body, check, host, port):

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body
    
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP(host, int(port))
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        if not check:
            server.sendmail(FROM, TO, message)
        server.close()
    except Exception as e:
        sys.stderr.write('Error: ' + str(e) + '\n')
        exit(1)

send_email(args.user, args.password, args.to, args.subject, args.message, 
           args.check, args.host, args.port)
