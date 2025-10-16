import math

def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

# Example usage
side_length = float(input("Enter the side length of the square: "))
result = square(side_length)
print(f"Perimeter: {result[0]}, Area: {result[1]}, Diagonal: {result[2]}")