def second_largest(arr):
    arr.sort()
    seen=[]
    for i in arr:
        if i not in seen:
            seen.append(i)
    return seen[-2]
print(second_largest([1,3,2,4,5,5]))

#methord 2
x= sorted(set(arr))
print(x[-2])
