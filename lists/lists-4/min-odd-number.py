numbers = [int(x) for x in input().split()]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(min(odd_numbers) if odd_numbers else 0)
