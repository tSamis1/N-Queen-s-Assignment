import random
import time


def nqueens(n):
    size = n
    solution = None
    while solution is None:
        solution = min_conflict_repair(build_board(size),size)
    print('done')


#This method builds the initial board. I tried the method they talked about in the NASA paper, as well as a random initialization
#the placing with minimumconflicts really slowed the initializing on large N's, so I don't use it for anyting N>100.
def build_board(size):
    initial_positions = []
    for i in range(size):
        initial_positions.append(0)
    if size <= 100:
        initial_positions[0] = random.randint(1, size)
    for row in range(2, size+1):
        if size > 100:
            # This places queens randomly
            initial_positions[row-1] = random.randint(1, size)
        else:
            # This is the method where each queen is placed initially to cause minimum conflicts
            conflicts = []
            options = []
            for col in range(1, size+1):
                conflicts.append(number_of_conflicts(row, row, col, initial_positions))
            for i in range(size):
                if conflicts[i] == min(conflicts):
                    options.append(i+1)
            initial_positions[row-1] = random.choice(options)

    return initial_positions

#This is the main repair function, it checks to see if there are still conflicts on the board, and if so, finds the queen with the most
#conflicts and moves it to the column with the least conflicts. This function seems to work up to about N= 100 but starts to fail after
#that
def min_conflict_repair(board, size):
    iterations = 0
    while iterations < 100:
        most_conflicts = 0
        #print(iterations)
        iterations += 1
        num_conflicts = 0
        for row in range(1, size+1):
            conflict_per_row = number_of_conflicts(size, row, board[row-1], board)
            if conflict_per_row > most_conflicts:
                most_conflicts = row
            num_conflicts += conflict_per_row
        if num_conflicts == 0:
            return board
        print(most_conflicts)

        queen = most_conflicts
        board[queen-1] = move_to_lowest_conflict_col(size, queen, board)
        #print(queen)
        #print(board)

    return None

#This function returns the column on a row with the fewest conflicts, and a random minimum if there is a tie
def move_to_lowest_conflict_col(size, row, board):
    conflicts = []
    options = []
    for col in range(1, size + 1):
        conflicts.append(number_of_conflicts(size, row, col, board))
    for i in range(size):
        if conflicts[i] == min(conflicts):
            options.append(i + 1)
    return random.choice(options)

#This function finds the number of conflicts on a specific square
def number_of_conflicts(size, row, col, positions):
    total = 0
    for i in range(1, size+1):
        if i == row:
            continue
        if positions[i-1] == col or abs(i - row) == abs(positions[i-1]-col):
            total += 1
    return total



start_time = time.time()
nqueens(1000)
elapsed_time = time.time() - start_time
print(elapsed_time)
