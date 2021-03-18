import re
import urllib.request
s= input("enter your mail id:")

res=re.fullmatch("\w[a-z0-9_.]*@[a-z0-9]+[.][a-z]+",s)
if res !=None:
    print("mail id is valid")
else:
    print("mail id is not valid")