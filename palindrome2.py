def palindrome(n):
    a=0
    x=n
    while x>0:
        y=x%10
        
        a=a*10+y
        x=x//10
    return a==n
print(palindrome(121))