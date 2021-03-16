n = int(input("enter n value"))
s=0
for i in range(1,n):
    if n % i ==0:
        s= s+i
if s == n:
    print("given number is perfect number")
else:
    print("given number is not a perfect number")