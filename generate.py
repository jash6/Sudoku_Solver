import random
import solver
import copy

class Generate:
    selected = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self):
        self.select_indices()
        self.initialise()
    
    def select_box_indices(self,boxno):
        count=0
        start_row=(boxno//3)*3
        start_col=(boxno%3)*3
        while count<4:
            row=random.randint(start_row,start_row+2)
            col=random.randint(start_col,start_col+2)
            if self.selected[row][col]!=0:
                continue
            else:
                count+=1
                self.selected[row][col]=1
    
    def select_indices(self):
        for boxno in range(0,9):
            self.select_box_indices(boxno)

    def find_next(self):
        for i in range(len(self.selected)):
            for j in range(len(self.selected[0])):
                if self.selected[i][j] == 1:
                    return (i, j)  # row, col

        return None

    def initialise(self):
        find = self.find_next()
        if not find:
            return True
        else:
            row, col = find
        
        for i in range(1,10):
            if solver.valid(self.board, i, (row, col)):
                self.board[row][col] = i
                self.selected[row][col]=0
                if solver.solve(copy.deepcopy(self.board)):
                    if self.initialise():
                        return True

                    self.board[row][col] = 0
                    self.selected[row][col]=1
        return False
        