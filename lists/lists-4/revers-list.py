numbers = [int(x) for x in input().split()]

# Reversing a list using slicing
for x in reversed(numbers):
    print(x, end=' ')
print()


# Another way to reverse a list
numbers.reverse()
for x in numbers:
    print(x, end=' ')
print()
