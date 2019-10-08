def locateLargest(m):
    x, y = 0, 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > m[x][y]:
                x, y = i, j
    return x, y


def printMatrix(m):
    for lst in m:
        for num in lst:
            print("  " + str(num), end='')
        print()


def main():
    m = []
    print("Enter first 3-by-4 matrix")
    for i in range(3):
        m.append([int(x.strip()) for x in input().split()])
    print("The entered matrix:")
    printMatrix(m)
    x, y = locateLargest(m)
    print("\nFirst largest value is located at row " + str(x) + " and column " + str(y))


main()
