s = "AABABBA"
k = 1
count = {}
left = 0
max_freq = 0
result = 0
for right in range(len(s)):
    char = s[right]
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
    

    max_freq = max(max_freq, count[s[right]])
    
    
    while (right - left + 1) - max_freq > k:
        count[s[left]] -= 1
        left += 1
        
        
    result = max(result, right - left + 1)

    
print(max_freq)
print(count)
print(result)