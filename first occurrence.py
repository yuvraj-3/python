haystack = "sadbutsad"
needle = "sad"

#methord 1
'''if needle in haystack:
    i=haystack.index(needle)
    print(i)
else:
    print("-1")'''

#methord 2
'''print(haystack.find(needle))'''

#methord 3
haystack = "sadbutsad"
needle = "sad"

m, n = len(haystack), len(needle)
result = -1

for i in range(m - n + 1): # Loop till needle can still fit
    if haystack[i:i+n] == needle:
        result = i
        break

print(result)
