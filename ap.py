#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib3
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
        r = requests.get(url, headers = headers)
        return r.text
    except RequestException as e:
            log_error('Error during requests to {0} : {1}'.format(url, str(e)))
            return None

def log_error(e):
    f=open("error.txt", "a+")
    f.write(e)
    f.close()

f=open("tid.txt", "a+")
url1 = 'https://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&sortall=1&filter=sortall&sortall=1&page=2'
raw_html = get_html(url1)
soup = BeautifulSoup(raw_html, 'html.parser')
for tag in soup.find_all("tbody"):
    id = re.findall(r'\d+',tag["id"])
    if id != []:
        s = id[0] +" "
        f.write(s)
f.close()
