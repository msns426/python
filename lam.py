import functools
l= [21,32,45,65,76,87,98,80,90,55,66,78,45,35,25,15,24,95]
a = list(filter(lambda x:x%5==0, l))
print("filter.............",a)
b=list(map(lambda x:x**2,l))
print("map...............",b)
l1=[1,2,3,4,5,6,7,8,9,10]
c= functools.reduce(lambda a,b:a+b,l1)
print(c)