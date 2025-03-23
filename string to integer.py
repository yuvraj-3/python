# A string to a 32-bit signed integer

def str_to_int( s):
        a=''
        sign=1
        s=s.strip()
        if s[0] == '-':
            sign = -1
            s = s[1:]
        for i in s:
            if i.isdigit():
                a=a+i
            else:
                break
        return sign * int(a) if a else 0
print(str_to_int("-42"))