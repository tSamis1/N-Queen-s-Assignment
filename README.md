# N-Queen-s-Assignment
CISC 352 - Assignment 1: nQueens Problem

nQueens Problem:

The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the more general n queens problem of placing n non-attacking queens on an n×n chessboard


Developed a program written in Python that efficiently solves the nQueens problem up to 1 million queens.

Requirements:
Python 3+

Note:
Program sometimes incurs an extremely infrequent index error when attempting to select from the twoConflicts list in the function colConflicts. We decided to keep this error as the trade off in efficiency to compensate for this error is too great, especially when the error occurs so infrequently due to the incredibly low statistical chance of the scenario.

Note:
Efficiency with large values of "n" is somewhat ambigious as it is almost entirely determined by the number of restarts necessary to find a solution. For example, with n = 1,000,000, the initialization time of the board is 4 and a half minutes. The min-conflict heuristic solves the board extremely quickly. If the board does not need to restart, it is solved in about 4.5 mins, with 1 restart, it is solved in about 9 minutes, and with 2 restarts it is solved in just under 12 minutes. Large values of "n" roughly average 1 restart, with fairly even values of 0-2 restarts.
