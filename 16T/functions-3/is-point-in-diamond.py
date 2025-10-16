def IsPointInDiamond(x, y):
    return abs(x) + abs(y) <= 1


x = float(input("Enter x: "))
y = float(input("Enter y: "))
print("YES" if IsPointInDiamond(x, y) else "NO")