#!/usr/bin/env python
import smtplib
import random

def verfMail():
    otp=generateKey()
    fromaddr = 'studentportal.info7@gmail.com'
    pasw='dbmsproject@2017'
    toaddrs = 'priyadharshan.97@gmail.com'
    content="Your code is : "+otp
    msg = "\r\n".join(["From:" + fromaddr,"To:" + toaddrs,"Subject: Verification Code","",content])
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(fromaddr,pasw)
    mail.sendmail(fromaddr,toaddrs,msg)
    mail.close()
    print "Hey"

def generateKey():
    xo = random.randint(1000,9999)
    ran = str(xo)
    return ran


verfMail()




#https://myaccount.google.com/u/1/lesssecureapps?pli=1
