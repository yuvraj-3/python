'''Input:
[0, 1, 0, 3, 12]
Output:
[1, 3, 12, 0, 0]'''

def sift(arr):
    count=0
    anew=[]
    for i in arr:
        if i ==0:
            count+=1
        else:
            anew.append(i)
    for i in range(0,count):
        anew.append(0)
    return anew
print(sift([0,1,0,3,0,12]))
