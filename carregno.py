import re
import urllib.request
s=input("enter car number")
num=re.fullmatch("AP[0-2][0-9][a-z]{2}[0-9]{4}",s)

if num !=None:
    print(" registration number is valid")
else:
    print("your entering wrong number, this in not a valid number")