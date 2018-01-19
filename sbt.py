#!/usr/bin/env python
import imp
import sys
import os

global pat
pat = "/Users/pyadhe/miniconda2/lib/python2.7/site-packages"




#try:
#    import sys
#    start = sys.version.index('|') # Do we have a modified sys.version?
#    end = sys.version.index('|', start + 1)
#    version_bak = sys.version # Backup modified sys.version
#    sys.version = sys.version.replace(sys.version[start:end+1], '') # Make it legible for platform module
#    import platform
#    platform.python_implementation() # Ignore result, we just need cache populated
#    platform._sys_version_cache[version_bak] = platform._sys_version_cache[sys.version] # Duplicate cache
#    sys.version = version_bak # Restore modified version string
#    import mechanize
#    from bs4 import BeautifulSoup
#except ValueError: # Catch .index() method not finding a pipe
#    pass

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
        if fnam[0] == name:
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



os.chdir("/Users/pyadhe/miniconda2/lib/python2.7")
print os.path.abspath('')
from sitepackages import mechanize
from bs4 import BeautifulSoup
mname=name()
#openBots(mname)



#sys.executable
#/Users/pyadhe/miniconda2/bin/python
