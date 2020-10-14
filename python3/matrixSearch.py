

# Matrix where both row and column are ascending
##  1  3  4 10
##  3  5  6 32
##  4  10  15 25
##  9 15 20 33  
matrix = [[1, 3, 4, 10], [3 ,5,6,32], [4, 10, 15, 25], [9,15,20,33]]
searchNum = 9

rowLimit = len(matrix)
colLimit= len(matrix[0])
row = 0
col = colLimit-1

foundMatch = False

while foundMatch is not True and row >= 0 and col >=0:
    print("Matrix eval=", matrix[row][col])
    if (matrix[row][col] == searchNum) :
        foundMatch = True
        break
    if matrix[row][col] > searchNum :
        col-=1
    elif matrix[row][col] < searchNum:
        row+=1
        

if foundMatch:
    print("FoundMatch row = " + str(row+1) + ", col = " + str(col+1))
else:
    print("No Match found")


