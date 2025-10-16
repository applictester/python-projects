numbers = [int(x) for x in input().split()]
min_positive = min(x for x in numbers if x > 0)
print(min_positive)
