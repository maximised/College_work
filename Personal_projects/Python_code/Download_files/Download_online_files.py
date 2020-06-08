from bs4 import BeautifulSoup
import requests
import re

import urllib.request
import urllib

url = "http://osullivan.ucc.ie/teaching/cs1113/lectures.html"
username = "cs1"
password = "cs1"
values = { 'Username': username,'Password': password }
data_credentials = urllib.parse.urlencode(values).encode("utf-8")

def download_cs1113_files( url ):
    r = requests.get( url )
    data = r.text;
    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all( "a" ):
        link = link.get("href")
        print( link )

        if link[-4:] == ".pdf":
            p = urllib.request.HTTPPasswordMgrWithDefaultRealm()

            p.add_password(None, link, username, password)

            handler = urllib.request.HTTPBasicAuthHandler(p)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)

            page = urllib.request.urlopen(url).read()

            file_name = "C:\College_work\Year_1\CS1113\Lectures\\" + link[link.find("/L"):]

            urllib.request.urlretrieve(link, file_name)


download_cs1113_files( url )