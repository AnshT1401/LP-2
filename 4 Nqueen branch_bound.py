def is_safe(queen_positions, row, col):
    for r in range(row):
        c = queen_positions[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def branch_and_bound_n_queens(n):
    solutions = []
    queen_positions = [-1] * n  # queen_positions[row] = col

    def solve(row):
        if row == n:
            solutions.append(queen_positions.copy())
            return
        for col in range(n):
            if is_safe(queen_positions, row, col):
                queen_positions[row] = col
                solve(row + 1)
                queen_positions[row] = -1  # backtrack

    solve(0)
    return solutions

# Utility to display the solution
def print_solutions(solutions, n):
    for sol in solutions:
        for row in range(n):
            line = ""
            for col in range(n):
                if sol[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n" + "-" * (2 * n))

# Example usage
n = 4
solutions = branch_and_bound_n_queens(n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")
print_solutions(solutions[:1], n)  # Only show one solution for brevity
