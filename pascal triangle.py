n=5

for i in range(n):
    num=1
    print(' '*(n-i), end="")

    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print()

'''def generate(numRows: int):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle''' 