# Input: Four integers representing the column and row of two chessboard cells
x1 = int(input("Enter column of first cell: "))
y1 = int(input("Enter row of first cell: "))
x2 = int(input("Enter column of second cell: "))
y2 = int(input("Enter row of second cell: "))

# Determine the color (0 or 1) of the cells
cell1_color = (x1 + y1) % 2
cell2_color = (x2 + y2) % 2

# Compare the colors and output the result
if cell1_color == cell2_color:
    print("YES")
else:
    print("NO")