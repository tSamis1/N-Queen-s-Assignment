import random

class nQueens:

    def __init__(self, n):
        self.board = [None] * n
        self.queens = { "rows" : {}, "leftDiag" : {}, "rightDiag" : {} }
        self.emptyRows = [i for i in range(n)]
        random.shuffle(self.emptyRows)
        self.occRows = [0] * n
        self.occLeftDiag = [0] * (2 * n - 1)
        self.occRightDiag = [0] * (2 * n - 1)
        self.totalConflicts = 0
        self.max_iterations = 100
        self.initialize(n)
        #self.solve(n)


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

        self.queens["rows"][row] = [col]
        self.queens["leftDiag"][leftDiag] = [col]
        self.queens["rightDiag"][(row + col)] = [col]
