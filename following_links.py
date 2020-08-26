
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
href = soup('a')

#Taking input
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
    link = href[position].get('href', None)
    print(link)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, "html.parser")
    href = soup('a')
   # print(tag.get('href', None))