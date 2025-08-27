'''Input: arr[] = [1, 2, 3, 4, 5]
Output: 3 2
Explanation: There are 3 odd elements (1, 3, 5) and 2 even elements (2 and 4).'''
arr = [1, 2, 3, 4, 5]
odd_count=0
even_count=0
for i in arr:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(odd_count,even_count)
'''
odd_count  = sum(1 for x in arr if x % 2 != 0)
even_count = sum(1 for x in arr if x % 2 == 0)'''