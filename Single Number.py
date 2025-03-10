def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num  # XOR operation
    return result

nums = [1, 2, 2]
print(singleNumber(nums))  # Output: 1

def singleNumber(nums):
    for num in nums:
        if nums.count(num) == 1:  
            return num

nums = [1, 2, 2]
print(singleNumber(nums))  

