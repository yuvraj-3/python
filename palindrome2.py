def palindrome(n):
    a=0
    x=n
    while x>0:
        y=x%10
        
        a=a*10+y
        x=x//10
    return a==n
print(palindrome(121))

# reverse intiger
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1  
        x = abs(x)  
        a = int(str(x)[::-1]) * sign  

        return a 