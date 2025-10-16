# Input: Four integers from 1 to 8 representing the column and row of two chessboard cells
x1 = int(input("Enter the column of the first cell: "))
y1 = int(input("Enter the row of the first cell: "))
x2 = int(input("Enter the column of the second cell: "))
y2 = int(input("Enter the row of the second cell: "))

# Check if the rook can move from the first cell to the second in one move
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")