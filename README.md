# Problems_Solved
#Matrix:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
print()
matrix1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix1)):
        c[i][j]=(matrix[i][j]+matrix1[i][j])
for i in c:
    print(*i)

                       

