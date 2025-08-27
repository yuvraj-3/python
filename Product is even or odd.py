'''Product is even or odd?
Difficulty: BasicAccuracy: 36.94%Submissions: 21K+Points: 1Average Time: 10m
You are given two long numbers N1 and N2 in a string. You need to find out if the product of these numbers generate an even number or an odd number, If it is an even number print 1 else print 0.

Example 1:

Input: 
N1 = "12"
N2 = "15"
Output: 1
Explanation: 12 * 15 = 180 which is an 
even number.'''

N1 = "12"
N2 = "15"

x=int(N2)*int(N1)
if x%2==0:
    print("1")
else:
    print("0")