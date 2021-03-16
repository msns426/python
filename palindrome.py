n = int(input("enter a number"))
n1 = n
s = 0
while n > 0:
    d = n % 10
    n = n//10
    s = s*10+d

if n1 == s:
    print(" given number {} is palindrome".format(s))
else:
    print(" given number {} is not palindrome".format(s))