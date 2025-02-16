nums =[3,2,2,3]
val = 2
"""new=[]
for i in nums:
    if i == val:
        pass
    else:
        new.append(i)
    

print(nums)
print(new)
print(len(new))"""

k = 0  # Pointer for the new position
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

print(k)
