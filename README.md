# sudoku

I want to write a program that will be able to generate a random, unsolved sudoku puzzle written in python. 
This could either be in the form of an interactive GUI application (pygame/pysimpleGUI), or some form of printable file (png/pdf).


Initial thoughts for solution:
1: write the logic to solve and unsolved sudoku. 
2: generate a random board that is completely filled.
3: test that is is a valid soduku puzzle.
4: remove some of the filled spaces until satisfied.
5: deliver solvable puzzle to user. (delivery method tbd)

Predicted challenges:
1: I imagine there are far more invalid boards than valid ones by several orders of magnitude.
    generating random boards and hoping they are solvable might not be the best solution.
    consider using the solving logic with a little randomness to generate the boards.
2: removing filled spaces at random may lead to a board that can only be solved with guess work,
    or that has multiple valid solutions, which is not ideal.
    additional logic will be needed to intelligently remove spaces so the puzzle is more fairly solvable.
    this logic would also make it easier to categorize the difficulty of a puzzle.

