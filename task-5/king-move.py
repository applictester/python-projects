# Input: four integers from 1 to 8
x1 = int(input("Enter the column of the first cell: "))
y1 = int(input("Enter the row of the first cell: "))
x2 = int(input("Enter the column of the second cell: "))
y2 = int(input("Enter the row of the second cell: "))

# Check if the king can move from (x1, y1) to (x2, y2) in one move
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")