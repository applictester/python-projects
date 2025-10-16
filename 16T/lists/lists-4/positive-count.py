numbers = [int(x) for x in input().split()]
positive_count = sum(1 for num in numbers if num > 0)
print(positive_count)