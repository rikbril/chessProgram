## This file contains all the instruction for the general movement of the chess pieces (including castleing & enpassant (still to be included)). 
## It returns an array with 3 values; 0, 1 and 2. The first item in an array corresponds to the first step in a direction. 
## if the piece does not encounter an other piece it is clear to move and this is represented by a 0 in the array. 
## If it encounters an piece of the opponent it returns a 1. This is done to keep track of the pinned pieces which are there to protect more important pieces.
## If a friendly piece is in the way or it has encounter a second piece of the opponent it will return an 2 
##
## there is an option to limit the amount of spaces a piece can move to 1 by setting the single_move variable to True

## for the horizontal and vertical directions the current coordinates are given. the code will loop from 0 to 7 replaces the row or column values depending on the direction
def moveLeft(row, i, single_move=False):
    counter = 0
    array = []
    for column in df.columns:
        if column < i:
            occupied = locationEmpty(row, (i - column) - 1)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveRight(row, i, single_move=False):
    counter = 0
    array = []
    for column in df.columns:
        if column > i:
            occupied = locationEmpty(row, column)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveUp(i, column, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row < i:
            occupied = locationEmpty((i - row) - 1, column)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveDown(i, column, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row > i:
            occupied = locationEmpty(row, column)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array

## for the diagonal directions an loop is started from 1 to 7. this value is either added or subtracted depending the direction, furthermore checks are placed to ensure that
## the add/subtracted values are within the 0 to 7 range.
def moveNE(row, column, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column + i < 8:
                occupied = locationEmpty(row - i, column + i)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveSE(row, column, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column + i < 8:
                occupied = locationEmpty(row + i, column + i)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveSW(row, column, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column - i >= 0:
                occupied = locationEmpty(row + i, column - i)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveNW(row, column, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column - i >= 0:
                occupied = locationEmpty(row - i, column - i)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array

def locationEmpty(row, column):
    if df_whites.iloc[row, column] == 1:
        return 2
    elif df.iloc[row, column] == 1:
        return 1
    else:
        return 0
