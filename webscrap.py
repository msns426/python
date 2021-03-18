import re, urllib
import urllib.request
sites = ["https://www.google.co.in/"]
for s in sites:
    print("printing sites ....",s)
    u=urllib.request.urlopen(s)
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)
    print(title[0])