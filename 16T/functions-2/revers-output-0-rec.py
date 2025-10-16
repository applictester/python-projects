def reverse_sequence():
    # Read the next integer from input
    num = int(input())
    if num != 0:
        # Recursive call
        reverse_sequence()
        # Print the number after the recursive call
        print(num)

# Start the function
reverse_sequence()