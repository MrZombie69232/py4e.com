from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# ignore the ssl certificate error
ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode = ssl.CERT_NONE

url= input('Enter Url :')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum =0
num=0
count = 0
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    num = int(tag.contents[0])
    sum= sum+num
    count = count+1
print('Count',count)
print('Sum',sum)