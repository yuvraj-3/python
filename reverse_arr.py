'''arr=[1,2,4,5,6]

print(arr[::-1])'''

def reversearr(arr):
    return arr.reverse()
arr=[1,2,3,4]
print(reversearr(arr=[1,2,4,5,6]))

def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1, 2, 3, 4]
reverseArray(arr)
print(arr)  