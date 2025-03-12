#Longest Substring Without Repeating Characters
def lengthOfLongestSubstring(s):
    left=0
    arr=[]
    max_len = 0
    for right in range(len(s)):
        while s[right] in arr:
            arr.remove(s[left])
            left +=1
        arr.append(s[right])
        max_len = max(max_len,right-left+1)
    return max_len


print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
