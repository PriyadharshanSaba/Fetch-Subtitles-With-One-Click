#!/usr/bin/env python
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import mechanize
import sys

def fetchAndInsert(mnam):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.open("https://subscene.com")
    br.select_form(nr=0)
    br.form['q']=mnam

def name():


