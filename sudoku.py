class Sudoku:
    def __init__(self, data):
        self.board = data
        return

    def validity_check(self): #returns true if this instance is valid in it's current configuration
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]} 
        columns = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        houses = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        #these could just as easily be lists instead of dicts, but I think it's easier to read like this

        for row in range(9):
            for column in range(9):
                num = self.board[row][column]
                
                house = row // 3 + (column // 3) * 3    #houses are the 3x3 sub-grids from left to right, top to bottom in ascending order
                
                if num in rows[row] or num in columns[column] or num in houses[house]:  #if current num already seen in the row, column or house the puzzle is invalid
                    return False
                else:
                    rows[row].append(num)
                    columns[column].append(num)
                    houses[houses].append(num)
                    continue
        
        #if we get here the puzzle is valid
        return True