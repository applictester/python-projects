def place_pins(n, leftmost=1, moves=None):
    if moves is None:
        moves = []
    if n == 0:
        return moves
    # Place a pin on the leftmost available cell
    moves.append(leftmost)
    # Recursively place the remaining pins
    place_pins(n - 1, leftmost + 1, moves)
    # Remove the pin from the current cell
    moves.append(-leftmost)
    return moves

def generate_moves(n):
    moves = []
    for i in range(1, n + 1):
        place_pins(i, moves=moves)
    return moves

# Input
N = int(input("Enter the number of cells (1 <= N <= 10): "))
if 1 <= N <= 10:
    result = generate_moves(N)
    # Output the moves
    print(" ".join(map(str, result)))
else:
    print("Invalid input. N must be between 1 and 10.")