import re
f=open("contacts.txt","r")
f1=open("phonelist.txt","w")
for line in f:
    list1 = re.findall("[7-9]\d{9}", line)
    for n in list1:
        f1.write(n+"\n")
print("data extracted successfully")
f.close()
f1.close()