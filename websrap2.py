import re
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
num=re.findall("[+91][0-9]{6,11}",str(text))
for i in num:
    print(i)

