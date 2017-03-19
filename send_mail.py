import smtplib
import random
import string

#random string generation
def send_mail():
    code=''
    for i in range(8):
        send=random.choice(string.ascii_letters)
        code=code+send
    print(code)


    #gmail connection
    mail=smtplib.SMTP('smtp.gmail.com:587')
    mail.ehlo()
    mail.starttls()
    mail.login('iamnotsparsha@gmail.com', 'fantasy.101')
    content = "Please use this code to log into your account: "
    content = 'Subject: %s\n\n%s' % ("Password Reset", content)
    content=content+ code
    print(content)
    mail.sendmail('iamnotsparsha@gmail.com','iamnotsparsha@gmail.com',content)
    mail.close()
