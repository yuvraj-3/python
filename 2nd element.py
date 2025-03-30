#methord 1 with sorting
arr = [12, 35, 1, 10, 34,34, 1]

arr= list(set(arr))
arr.sort(reverse=True)
print(arr[1])

#methord 2 without sorting
def second_largest(arr):
    first = second = float('-inf')#negative infinity
    
    for num in arr:
        if num > first:  
            second = first  
            first = num  
        elif num > second and num != first:
            second = num  
    
    return second if second != float('-inf') else None  

arr = [10, 5, 10]
print(second_largest(arr))  

