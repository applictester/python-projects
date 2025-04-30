def IsPointInArea(x, y):
    # The function checks if a point (x, y) satisfies one of the following conditions:
    return (
        # Condition 1:
        # The point lies below the line y = -x
        # AND the point lies below the line y = 2(x + 1)
        # AND the point is outside the circle with center (-1, 1) and radius 2
        # AND the point lies above the line y = 3.5
        ((y <= -x) and (y <= 2 * (x + 1)) and ((x + 1)**2 + (y - 1)**2 >= 4) and (y >= 3.5)) or
        # Condition 2:
        # The point lies inside the circle with center (-1, 1) and radius 2
        # AND the point lies above the line y = -x
        # AND the point lies above the line y = 2(x + 1)
        (((x + 1)**2 + (y - 1)**2 <= 4) and (y >= -x) and (y >= 2 * (x + 1)))
    )

# Input coordinates from the user
x = float(input("Введіть координату x: "))  # Enter x-coordinate
y = float(input("Введіть координату y: "))  # Enter y-coordinate

# Check if the point is in the area and print the result
print("YES" if IsPointInArea(x, y) else "NO")
