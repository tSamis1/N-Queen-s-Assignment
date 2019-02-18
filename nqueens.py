import random
import time

class nQueens:

    def __init__(self, n):
        self.board = [None] * n
        self.emptyRows = [i for i in range(n)]
        random.shuffle(self.emptyRows)
        self.occRows = [0] * n
        self.occLeftDiag = [0] * (2 * n - 1)
        self.occRightDiag = [0] * (2 * n - 1)
        self.totalConflicts = 0
        self.max_iterations = n * 2
        self.num_restarts = 0
        self.initialize(n)
        self.solve(n)

    #Creates the board before iterative repair
    def initialize(self, n):
        for col in range(n):
            if col == 0:
                rowVal = random.randint(0, n - 1)
                self.board[col] = rowVal + 1
                self.updateConflicts(rowVal, col, n)
            else:
                x = self.colConflicts(col, n)
                self.totalConflicts += x
    
    def colConflicts(self, col, n):
        oneConflict = []
        twoConflict = []
        #Determine number of conflicts for a row
        for row in self.emptyRows:
            numConflicts = self.calcConflicts(row, col, n)
            
            if numConflicts == 0:
                self.board[col] = row + 1
                self.updateConflicts(row, col, n)
                return 0
            
            if numConflicts == 1:
                oneConflict.append(row)
           
            if numConflicts == 2:
                twoConflict.append(row)

        if len(oneConflict) == 0:
            rowVal = random.choice(twoConflict)
            self.board[col] = rowVal + 1
            self.updateConflicts(rowVal, col, n)
            return 2

        rowVal = random.choice(oneConflict)
        self.board[col] = rowVal + 1
        self.updateConflicts(rowVal, col, n)
        return 1
    
    #Checks square for number of conflicts
    def calcConflicts(self, row, col, n):
        if (row - col) >= 0:
            leftDiag = row - col
        else:
            leftDiag = (row - col) + (2*n - 1)        #Avoids negative values that would give the incorrect index
        rightDiag = row + col
        numConflicts = self.occRows[row] + self.occLeftDiag[leftDiag] + self.occRightDiag[rightDiag]
        return numConflicts

    def updateConflicts(self, row, col, n):
        if (row - col) >= 0:
            leftDiag = row - col
        else:
            leftDiag = (row - col) + (2*n - 1)   #Avoids negative values that would give the incorrect index
        self.occLeftDiag[leftDiag] += 1
        self.occRows[row] += 1
        self.occRightDiag[row + col] += 1
        self.emptyRows.remove(row)
    
    
    def solve(self, n):
        for i in range(self.max_iterations):
            if self.totalConflicts == 0:    #REMEMBER TO KEEP TRACK OF TOTAL CONFLICTS
                print("solution")
                return
            else:
                #Generates random column with at least 1 conflict
                randCol = random.randint(0, n - 1)
                oldRow = self.board[randCol]
                oldRow -= 1
                numConflicts = self.calcConflicts(oldRow, randCol, n)
                while numConflicts < 1:
                    randCol = random.randint(0, n - 1)
                    oldRow = self.board[randCol]
                    oldRow -= 1
                    numConflicts = self.calcConflicts(oldRow, randCol, n)

                noConflictUpdate = False
                for newRow in self.emptyRows:
                    numConflicts = self.calcConflicts(newRow, randCol, n)
                    if numConflicts == 0:
                        self.board[randCol] = newRow + 1
                        self.totalConflicts -= (self.calcConflicts(oldRow, randCol, n))
                        self.updateConflicts(newRow, randCol, n)
                        self.removeQueen(oldRow, randCol, n)
                        noConflictUpdate = True
                        break

                if noConflictUpdate == False:
                    randRow = random.randint(0, n - 1)
                    numConflicts = self.calcConflicts(randRow, randCol, n)
                    counter = 0
                    while numConflicts >= self.calcConflicts(oldRow, randCol, n) and counter < 10:
                        randRow = random.randint(0, n - 1)
                        numConflicts = self.calcConflicts(randRow, randCol, n)
                        counter += 1

                    if numConflicts < self.calcConflicts(oldRow, randCol, n):           #One conflict row
                        self.board[randCol] = randRow + 1
                        self.totalConflicts -= (self.calcConflicts(oldRow, randCol, n) - numConflicts)
                        self.updateSolveConflicts(randRow, randCol, n)
                        self.removeQueen(oldRow, randCol, n)

                    elif counter ==  10:
                        randRow = random.randint(0, n - 1)
                        numConflicts = self.calcConflicts(randRow, randCol, n)
                        while numConflicts > self.calcConflicts(oldRow, randCol, n):
                            randRow = random.randint(0, n - 1)
                            numConflicts = self.calcConflicts(randRow, randCol, n)
                        self.board[randCol] = randRow + 1
                        self.updateSolveConflicts(randRow, randCol, n)
                        self.removeQueen(oldRow, randCol, n)

        self.num_restarts += 1
        print("restarting")
        self.restart(n)
    
    #Remove queen from initial location
    def removeQueen(self, oldRow, col, n):
        if (oldRow - col) >= 0:
            leftDiag = oldRow - col
        else:
            leftDiag = (oldRow - col) + (2*n - 1)   #Avoids negative values that would give the incorrect index
        self.occLeftDiag[leftDiag] -= 1
        self.occRows[oldRow] -= 1
        self.occRightDiag[oldRow + col] -= 1

        if self.occRows[oldRow] == 0:
            self.emptyRows.append(oldRow)

    #This function is to avoid the emptyRows.remove() in the other updateConflicts method
    def updateSolveConflicts(self, newRow, col, n):
        if (newRow - col) >= 0:
            leftDiag = newRow - col
        else:
            leftDiag = (newRow - col) + (2*n - 1)   #Avoids negative values that would give the incorrect index
        self.occRows[newRow] += 1
        self.occLeftDiag[leftDiag] += 1
        self.occRightDiag[newRow + col] += 1
    
    #Full reset
    def restart(self, n):
        self.board = [None] * n
        self.emptyRows = [i for i in range(n)]
        random.shuffle(self.emptyRows)
        self.occRows = [0] * n
        self.occLeftDiag = [0] * (2 * n - 1)
        self.occRightDiag = [0] * (2 * n - 1)
        self.totalConflicts = 0
        self.max_iterations = n*2
        self.initialize(n)
        self.solve(n)

def main():
    begin = time.time()
    input = open("nqueens.txt")
    output = open("nqueens_out.txt", "w")
    lines = input.readlines()
    lines = [x.strip() for x in lines]
    lines = [int(i) for i in lines]
    for n in lines:
        initial_board = nQueens(n)
        output.write(str(initial_board.board) + "\n")
        #print(initial_board.board)
        #print(initial_board.totalConflicts)
        #print(initial_board.num_restarts)
    end = time.time()
    length = end - begin
    print(str(length))

main()
