n = int(input("enter  no of elements"))
a=[]
for i in range(n):
    v=int(input("enter value"))
    a.append(v)

avg = sum(a)/n
print("average of given list of elements is:",avg)
