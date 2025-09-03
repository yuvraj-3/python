arr = [10, 5,10, 10]
arr.sort()
max_ele=max(arr)
for i in range(len(arr)-1,-1,-1):
    if arr[i]==max_ele:
        continue
    else:
        print(arr[i])

#methord 2
x= sorted(set(arr))
print(x[-2])
