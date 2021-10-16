#iterate through the puzzle looking for an empty space
    #iterate through possible values for the space
        #if value is not in current row
        #current column
        #current house
            #insert the value into the puzzle
            #if puzzle is full or recursive solve call returns true return true
            #else set space back to empty and return false
        #else try next value

def check_complete(puzzle):
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                return False
    return True

def solve(puzzle):
    #look for empty space
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == 0:
                for value in range(1,10):
                    #check the row
                    if value in puzzle[row]:
                        return False
                    #check the column
                    for col_row in range(9):
                        if puzzle[col_row][column] == value:
                            return False
                    #check the house
                    for house_row in house_neighbors(row): 
                        for house_column in house_neighbors(column):
                            if puzzle[house_row][house_column] == value:
                                return False
                    #if we got here the current value is valid at this time
                    puzzle[row][column] = value
                    #check if puzzle is full and solve downstream
                    if check_complete(puzzle) or solve(puzzle):
                        print("Puzzle solved!")
                        return True
                    #if we get here no valid puzzle downstream, so revert the current cell and try next value
                    puzzle[row][column] = 0
                #no valid values for this space
                return False
    #if we get here there were no empty spaces
    #this shouldn't happen, but I should treat it as if the puzzle is solved and return True
    return True

#returns range function of other cells in the same house as provided cell's row or column
def house_neighbors(address):
    return range(((address//3) * 3), (((address//3)*3)+3))

def validity_check(puzzle): #returns true if puzzle is valid sudoku
        rows = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]} 
        columns = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        houses = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        #these could just as easily be lists instead of dicts, but I think it's easier to read like this

        for row in range(9):
            for column in range(9):
                num = puzzle[row][column]
                
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
