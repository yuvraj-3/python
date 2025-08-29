# Valid Anagram Check
s = "rat"
t = "car"

for i in s:
    if i in t:
        print("yes it is")
    else:
        print(f"{i} not in {t}")
#--------------------------------------------------------------------------------------------
def isAnagram(s, t):
    if sorted(s)==sorted(t):
        return "Anagram"
    else:
        return "Not An Anagram"

print(isAnagram("cat","rat"))