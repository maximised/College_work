from bs4 import BeautifulSoup
import re
import urllib.request, urllib.parse, urllib.error
import ssl

url = input('enter url - ')

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()

print(html)

input()

