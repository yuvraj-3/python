"""swiss"""
def non_repeat(s):
    for i in s:
        if s.count(i)==1:
            return i
    return None
print(non_repeat("swiss"))

