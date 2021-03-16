"""def my_gen():
    for i in range(100):
        yield i


g=my_gen()

for i in g:
    print(i,end=" ")
"""
a=iter([12,13,])
print(next(a))
print(next(a))
print(next(a))

