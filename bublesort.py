l = [10,12,15,16,21,4,3,6,7,14]
print("before sorting the list")

for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]

print("after sorting list is",l)