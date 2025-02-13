def palindrome(x):
    return str(x) == str(x)[::-1]

print(palindrome(121))