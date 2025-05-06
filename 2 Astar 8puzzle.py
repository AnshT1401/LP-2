g = 0

def solvable(start):
    inv = 0  #inversions
    for i in range(9):
        if start[i] == -1:
            continue
        for j in range(i+1, 9):
            if start[j] == -1:
                continue
            if start[i] > start[j]:
                inv += 1
    return inv % 2 == 0

def heuristic(start, goal):
    global g
    h = 0
    for i in range(9):
        for j in range(9):
            if start[i] == goal[j] and start[i] != -1:
                h += abs(j // 3 - i // 3) + abs(j % 3 - i % 3)
    return h + g

def moveleft(start, position):
    start[position], start[position-1] = start[position-1], start[position]

def moveright(start, position):
    start[position], start[position+1] = start[position+1], start[position]

def moveup(start, position):
    start[position], start[position-3] = start[position-3], start[position]

def movedown(start, position):
    start[position], start[position+3] = start[position+3], start[position]

def movetiles(start, goal):
    emptyat = start.index(-1)
    row = emptyat // 3
    col = emptyat % 3

    t1, t2, t3, t4 = start[:], start[:], start[:], start[:]
    f1 = f2 = f3 = f4 = 100

    if col - 1 >= 0:
        moveleft(t1, emptyat)
        f1 = heuristic(t1, goal)
    if col + 1 < 3:
        moveright(t2, emptyat)
        f2 = heuristic(t2, goal)
    if row + 1 < 3:
        movedown(t3, emptyat)
        f3 = heuristic(t3, goal)
    if row - 1 >= 0:
        moveup(t4, emptyat)
        f4 = heuristic(t4, goal)

    min_heu = min(f1, f2, f3, f4)

    if f1 == min_heu:
        moveleft(start, emptyat)
    elif f2 == min_heu:
        moveright(start, emptyat)
    elif f3 == min_heu:
        movedown(start, emptyat)
    elif f4 == min_heu:
        moveup(start, emptyat)

def print_board(elements):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if elements[i] == -1 else elements[i], end=" ")
    print()

def solveEight(start, goal):
    global g
    g += 1
    movetiles(start, goal)
    print_board(start)
    f = heuristic(start, goal)
    if f == g:
        print(f"Solved in {g} moves")
        return
    solveEight(start, goal)

def main():
    global g
    start = []
    goal = []

    print("Enter the start state (use -1 for blank):")
    for _ in range(9):
        start.append(int(input()))
    print("Enter the goal state (use -1 for blank):")
    for _ in range(9):
        goal.append(int(input()))

    print("Initial Board:")
    print_board(start)

    if solvable(start):
        solveEight(start, goal)
    else:
        print("Not solvable")

if __name__ == "__main__":
    main()
