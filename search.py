nums = [1,3,5,6]
target = 2
i=0
if target in nums:
    i=nums.index(target)
    
else:
    for j in nums:
        if nums[i] < target:
            i += 1
    
print(i)
