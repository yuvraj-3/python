def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome found
    
    longest = ""
    
    for i in range(len(s)):
        # Check for odd-length palindrome
        odd_pal = expand(i, i)
        # Check for even-length palindrome
        even_pal = expand(i, i + 1)
        
        # Update longest palindrome if a longer one is found
        longest = max(longest, odd_pal, even_pal, key=len)
    
    return longest


print(longestPalindrome("babad"))
