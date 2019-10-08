print("Enter First 3 *3 Matrix")
X = []
#Read First Matrix
for i in range(3):
    X.append([])
    for j in range(3):
        b=int(input("Enter element for First Matrix at "''+ str(i)+str(j)))
X[i].append(b)

print("Enter Second 3 *3 Matrix")
#Read Second Matrix
Y = []
for i in range(3):
    Y.append([])
    for j in range(3):
        c=int(input("Enter element for First Matrix at "''+ str(i)+str(j)))
Y[i].append(c)
#Matrix for String the result
result = [[0,0,0],
[0,0,0],
[0,0,0]]
#Addition of two Matrices
def Addition(X,Y):
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j]
            return result
# Printing first Matrix in the form of array
p1=[]
for r in range(0,3):
    for t in range(0,3):
        p1.append(X[r][t])
        print("Matrix A")
        print(p1)
p2=[]
for r in range(0,3):
    for t in range(0,3):
        p2.append(X[r][t])
        print("Matrix B")
        print(p2)
k=Addition(X,Y)
p=[]
for r in range(0,3):
    for t in range(0,3):
        p.append(k[r][t])
        print("A+B")
        print(p)
