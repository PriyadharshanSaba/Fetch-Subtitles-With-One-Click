#!/usr/bin/env python
import smtplib
import random
import sys

def verfMail():
    fromaddr = 'studentportal.info7@gmail.com'
    pasw='dbmsproject@2017'
    toaddrs = 'priyadharshan.97@gmail.com'
    content="Here: "+str(sys.argv[1])
    msg = "\r\n".join(["From:" + fromaddr,"To:" + toaddrs,"Subject: Verification Code","",content])
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(fromaddr,pasw)
    mail.sendmail(fromaddr,toaddrs,msg)
    mail.close()
    print "Hey"

verfMail()




#https://myaccount.google.com/u/1/lesssecureapps?pli=1
