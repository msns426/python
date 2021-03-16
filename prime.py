"""a=int(input("Enter number: "))
k=0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")"""

for i in range(1,100):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i ,end=" ")
