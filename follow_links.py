#IMPORT MODULES

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#PROMPT USER FOR URL, COUNT AND POSITION
url = input('Enter a url - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count_ = input('Enter Count - ')
Position = input('Enter Position - ')

#COUNTING LOOP...
count = int(count_)
while count > 0:

    count = count - 1
    tags = soup('a')
    print(tags.get('href', None))
