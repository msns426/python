"""str=["hello","srinivas"]
s=str
print(str == s)
print((str is s))
str1=["hello","srinivas"]
print(str == str1)
print(str is str1)

print("Hello hai".istitle())
print(max("sAtya"))"""


"""a=int(input("enter  a value"))
b=int(input("enter b value"))
i=1
while i<=a and i<=b:
    if a%i ==0 and b%i==0:
       gcd=i
    i+=1

print("gcd of  {} and {} is  {}".format(a,b,gcd))"""


a=int(input("enter  a value"))
b=int(input("enter b value"))
if a > b:
    max = a
else:
    max = b

while True:
    if max%a==0 and max%b==0:
        lcm=max
        break
    max+=1

print("lcm of  {} and {} is  {}".format(a,b,lcm))