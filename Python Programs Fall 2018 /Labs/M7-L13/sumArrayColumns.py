def sumColumn(matrix, col):
    s = 0
    for x in range(len(matrix)):
        s += matrix[x][col]
    return s

def main():
    print("Enter 3-by-4 array:")
    matrix = []
    for x in range(3):
        row = input()
        matrix.append([int(val) for val in row.split(" ")])
    print("The entered matrix:")
    for x in matrix:
        for y in x:
            print(y,end="\t")
        print()
    for x in range(len(matrix[0])):
        print("Sum of column",x,"is",sumColumn(matrix,x))
        
main()
