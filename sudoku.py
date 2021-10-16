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
                print("puzzle not yet full")
                return False
    print("puzzle full")
    return True

def solve(puzzle):
    #look for empty space
    for row in range(9):
        print("row is " + str(row))
        for column in range(9):
            print("column is " + str(column))
            if puzzle[row][column] == 0:
                print("empty space found")
                for value in range(1,10):
                    print("trying " + str(value))
                    #check the row
                    if value in puzzle[row]:
                        print("Failed row check")
                        continue
                    print("passed row check")
                    #check the column
                    for col_row in range(9):
                        if puzzle[col_row][column] == value:
                            print("Failed column check")
                            continue
                    print("passed column check")
                    #check the house
                    for house_row in house_neighbors(row): 
                        for house_column in house_neighbors(column):
                            if puzzle[house_row][house_column] == value:
                                print("Failed house check")
                                continue
                    print("passed house check")
                    #if we got here the current value is valid
                    puzzle[row][column] = value
                    #check if puzzle is full and solve downstream
                    if check_complete(puzzle) or solve(puzzle):
                        print("Puzzle solved!")
                        return True
                    #if we get here no valid puzzle downstream, so backtrack and try next value
                    else:
                        print("downstream fail. Next value")
                        puzzle[row][column] = 0
                        continue
                #no valid values for this space. Backtrack.
                print("No valid nums in this space. Backtrack")
                return False
    #if we get here there were no empty spaces
    #this shouldn't happen, but I should treat it as if the puzzle is solved and return True
    print("Puzzle already completed")
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
            print("row is " + str(row))
            for column in range(9):
                print("column is " + str(column))
                num = puzzle[row][column]
                print("num is " + str(num))
                house = row // 3 + (column // 3) * 3    #houses are the 3x3 sub-grids from left to right, top to bottom in ascending order
                print("house is " + str(house))
                if num in rows[row] or num in columns[column] or num in houses[house]:  #if current num already seen in the row, column or house the puzzle is invalid
                    print("num already there")
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
print(validity_check(sudoku))