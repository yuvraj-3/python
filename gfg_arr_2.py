'''n = len(arr)
nonZeroIndex = 0

for i in range(n):
    if arr[i] != 0:
        arr[nonZeroIndex], arr[i] = arr[i], arr[nonZeroIndex]
        nonZeroIndex += 1
'''
#2
class Solution:
    def pushZerosToEnd(self, arr):
        # Get all non-zero elements
        new = [num for num in arr if num != 0]
        
        # Calculate how many zeros to add
        zeros = len(arr) - len(new)
        
        # modify the original array
        arr[:] = new + [0] * zeros  

