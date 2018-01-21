#!/usr/bin/env python
import imp
import sys
import os




def name():
    i=0
    mname=""
    for x in sys.argv:
        if i>0:
            with open('/Users/pyadhe/Documents/iTest/testBash/macBash/test.txt', 'a') as the_file:
                the_file.write(x+" ")
                mname=mname+x+" "
        i+=1
    return mname

def openBots(name):
    sys.path.append("/usr/local/lib/python2.7/site-packages")
    import mechanize
    from bs4 import BeautifulSoup
    name=name.strip().lower()
    name=name.split('.')
    name=name[0]
    br = mechanize.Browser()
    br.set_handle_robots(False)
    op=br.open("http://www.yifysubtitles.com")
    br.select_form(nr=0)
    br.form['q']=name
    sub = br.submit()
    soup = BeautifulSoup(sub.read(),"lxml")

    for div in soup.findAll('div',{'class':'col-sm-12'}):
        dd=div.find('div',{'class':'media-body'})
        di=dd.find('a')
        fnam = di.text.strip().lower().split("\n")
            #if fnam[0] == name:
        link=di['href']
        break

    op=br.open(link)
    soup = BeautifulSoup(op.read(),"lxml")
    row_count=0
    for table in soup.findAll('table',{'class':'table other-subs'}):
        for td in table.findAll('td',{'class':'flag-cell'}):
            row_count+=1
            if td.text.lower().strip() == "english":
                break

    for table in soup.findAll('table',{'class':'table other-subs'}):
        rc=0
        row_count= (row_count*3) - 3
        for a in table.findAll('a'):
            if rc==row_count:
                link1 = a['href']
                break
            else:
                rc+=1

    op=br.open(link1)
    soup = BeautifulSoup(op.read(),"lxml")

    row_count=0
    for div in soup.findAll('div',{'class':'col-xs-12'}):
        if row_count==2:
            x= div.text.split('\n')
            fnam = x[1].strip()+".srt"
        row_count+=1
    for a in soup.findAll('a',{'class':'btn-icon download-subtitle'}):
        down_link= a['href']
    br.retrieve(down_link,fnam)

mname=name()
openBots(mname)







#f, filename, description = imp.find_module('mechanize')
#mechanize = imp.load_module('mechanize.module', f, filename, description)
#f, filename, description = imp.find_module('bs4')
#BeautifulSoup = imp.load_module('bs4.BeautifulSoup', f, filename, description)


#    sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/mechanize")
#    from mechanize import _mechanize as mechanize
#    sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/bs4")
#    from bs4 import BeautifulSoup
#    f = "/usr/local/lib/python2.7/site-packages/mechanize"
#
#    mechanize = imp.load_source('mechanize.module', f)
#    f, filename, description = imp.find_module('bs4')
#BeautifulSoup = imp.load_source('bs4.BeautifulSoup', f, filename, description)
