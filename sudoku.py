import random

def check_complete(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                print("puzzle not yet full")
                return False
    print("puzzle full")
    return True

def solve(puzzle):

    #look for empty space
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                #introduce randomness
                values = [x for x in range(1,10)]
                random.shuffle(values)
                for value in values:
                    #check the row
                    row_failed = False
                    if value in puzzle[row]:
                        row_failed = True
                    if row_failed:
                        continue
                    #check the column
                    col_failed = False
                    for col_row in range(9):
                        if puzzle[col_row][column] == value:
                            col_failed = True
                    if col_failed:
                        continue
                    #check the house
                    house_failed = False
                    for house_row in house_neighbors(row): 
                        for house_column in house_neighbors(column):
                            if puzzle[house_row][house_column] == value:
                                house_failed = True
                    if house_failed:
                        continue
                    #if we got here the current value is valid
                    puzzle[row][column] = value
                    #check if puzzle is full and solve downstream
                    if check_complete(puzzle) or solve(puzzle):
                        print("Puzzle solved!")
                        return True
                    #if we get here no valid puzzle downstream, so backtrack and try next value
                    else:
                        puzzle[row][column] = 0
                        continue
                #no valid values for this space. Backtrack.
                return False
    #if we get here there were no empty spaces
    #this shouldn't happen, but I should treat it as if the puzzle is solved and return True
    print("Puzzle already completed")
    return True

#returns range function of other cells in the same house as provided cell's row or column
def house_neighbors(address):
    return range(((address//3) * 3), (((address//3)*3)+3))

def validity_check(puzzle): #returns true if completed puzzle is valid sudoku for testing/debugging
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]} 
        columns = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        houses = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        #these could just as easily be lists instead of dicts, but I think it's easier to read like this

        for row in range(9):
            for column in range(9):
                num = puzzle[row][column]
                house = ((row // 3) * 3) + (column // 3)    #houses are the 3x3 sub-grids from left to right, top to bottom in ascending order
                if num in rows[row] or num in columns[column] or num in houses[house]:  #if current num already seen in the row, column or house the puzzle is invalid
                    return False
                else:
                    rows[row].append(num)
                    columns[column].append(num)
                    houses[house].append(num)
                    continue
        #if we get here the puzzle is valid
        return True


sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0], [0, 8, 7, 0, 0, 0, 0, 3, 1], [0, 0, 3, 0, 1, 0, 0, 8, 0], [9, 0, 0, 8, 6, 3, 0, 0, 5], [0, 5, 0, 0, 9, 0, 6, 0, 0], [1, 3, 0, 0, 0, 0, 2, 5, 0], [0, 0, 0, 0, 0, 0, 0, 7, 4], [0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(solve(sudoku))
for line in sudoku:
    print(line)
print(validity_check(sudoku))