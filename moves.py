## This file contains all the instruction for the general movement of the chess pieces (including castleing & enpassant (still to be included)). 
## It returns an array with 3 values; 0, 1 and 2. The first item in an array corresponds to the first step in a direction. 
## if the piece does not encounter an other piece it is clear to move and this is represented by a 0 in the array. 
## If it encounters an piece of the opponent it returns a 1. This is done to keep track of the pinned pieces which are there to protect more important pieces.
## If a friendly piece is in the way or it has encounter a second piece of the opponent it will return an 2 
##
## there is an option to limit the amount of spaces a piece can move to 1 by setting the single_move variable to True

## for the horizontal and vertical directions the current coordinates are given. the code will loop from 0 to 7 replaces the row or column values depending on the direction
def moveLeft(row, i, is_white, single_move=False):
    counter = 0
    array = []
    for column in df.columns:
        if column < i:
            occupied = addingLocation(row, (i - column) - 1, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveRight(row, i, is_white, single_move=False):
    counter = 0
    array = []
    for column in df.columns:
        if column > i:
            occupied = addingLocation(row, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveUp(i, column, is_white, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row < i:
            occupied = addingLocation((i - row) - 1, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def moveDown(i, column, is_white, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row > i:
            occupied = addingLocation(row, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array

def removeLeft(row, i, is_white, single_move=False ):
    counter = 0
    array = []
    for column in df.columns:
        if column < i:
            occupied = removeLocation(row, (i - column) - 1, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def removeRight(row, i, is_white, single_move=False):
    counter = 0
    array = []
    for column in df.columns:
        if column > i:
            occupied = removeLocation(row, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def removeUp(i, column, is_white, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row < i:
            occupied = removeLocation((i - row) - 1, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
def removeDown(i, column, is_white, single_move=False):
    counter = 0
    array = []
    for row in range(0, len(df.index)):
        if row > i:
            occupied = removeLocation(row, column, is_white, counter)
            counter = counter + occupied
            if counter > 2:
                counter = 2
            array.append(counter)
            if single_move == True:
                return array
    return array
    
## for the diagonal directions an loop is started from 1 to 7. this value is either added or subtracted depending the direction, furthermore checks are placed to ensure that
## the add/subtracted values are within the 0 to 7 range.
def moveNE(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column + i < 8:
                occupied = addingLocation(
                    row - i, column + i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveSE(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column + i < 8:
                occupied = addingLocation(
                    row + i, column + i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveSW(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column - i >= 0:
                occupied = addingLocation(
                    row + i, column - i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def moveNW(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column - i >= 0:
                occupied = addingLocation(
                    row - i, column - i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array

def removeNE(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column + i < 8:
                occupied = removeLocation(row - i, column + i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def removeSE(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column + i < 8:
                occupied = removeLocation(row + i, column + i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def removeSW(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row + i < 8:
            if column - i >= 0:
                occupied = removeLocation(row + i, column - i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array
def removeNW(row, column, is_white, single_move=False):
    counter = 0
    array = []
    for i in range(1, 8):
        if row - i >= 0:
            if column - i >= 0:
                occupied = removeLocation(row - i, column - i, is_white, counter)
                counter = counter + occupied
                if counter > 2:
                    counter = 2
                array.append(counter)
                if single_move == True:
                    return array
    return array

## looking if a piece can move to/ attack a certain spot and which places is pressures. this function is called by an other loop function
def addingLocation(row, column, is_white, counter):
    ## this function is called by a loop an is supplied with an counter, between 0 and 2. if the counter is 0 the piece has not encounter an other piece on its path. 
    ## if it already has encountered a singular opponent it recieves an 1. which means that it can not move any further but still pressures the piece behind.
    ## once it encounters an 2nd opponent or a friendly piece it gets a 2. as a result it cannot reach that spot under any circumstance by the next round
    
    #it passes this value on to the next function and once more but it adds the value for the spot it is checking right now, 0 for unoccupied, 1 for opponent and 2 for friendly  
    if  (df_whites.iloc[row, column] == 1 and is_white == True) or (df_blacks.iloc[row, column] == 1 and is_white == False):
        addMovement(row, column, is_white, counter, counter + 2)
        return 2 
    elif df.iloc[row, column] == 1:
        addMovement(row, column, is_white, counter, counter + 1)
        return 1
    else:
        addMovement(row, column, is_white, counter, counter + 0)
        return 0

## this function is an continuation of the addingLocation function, but it is split up for cleanliness
def addMovement(row, column, is_white, previous_counter, added_counter):
    ## checking if the piece is white
    if is_white == True:
        if added_counter == 0:
            df_whites_movement.iloc[row, column] += 1
            df_pinned_by_whites.iloc[row, column] += 1
        elif added_counter == 1:
            if previous_counter == 0:
                df_whites_movement.iloc[row, column] += 1
            df_pinned_by_whites.iloc[row, column] += 1
        else:
            if previous_counter == 1:
                df_pinned_by_whites.iloc[row, column] += 1
    
    ## checking if the piece is black
    if is_white == False:
        if added_counter == 0:
            df_blacks_movement.iloc[row, column] += 1
            df_pinned_by_blacks.iloc[row, column] += 1
        elif added_counter == 1:
            if previous_counter == 0:
                df_blacks_movement.iloc[row, column] += 1
        else:
            if previous_counter == 1:
                df_pinned_by_blacks.iloc[row, column] += 1

## this function is almost the same as the addingLocation function but here it removes the tracking function in preparation for an move/attack or after a piece is destroyed
def removeLocation(row, column, is_white, counter):
    ## this function is called by a loop an is supplied with an counter, between 0 and 2. if the counter is 0 the piece has not encounter an other piece on its path.
    ## if it already has encountered a singular opponent it recieves an 1. which means that it can not move any further but still pressures the piece behind.
    ## once it encounters an 2nd opponent or a friendly piece it gets a 2. as a result it cannot reach that spot under any circumstance by the next round

    #it passes this value on to the next function and once more but it adds the value for the spot it is checking right now, 0 for unoccupied, 1 for opponent and 2 for friendly
    if (df_whites.iloc[row, column] == 1 and is_white == True) or (df_blacks.iloc[row, column] == 1 and is_white == False):
        removeMovement(row, column, is_white, counter, counter + 2)
        return 2
    elif df.iloc[row, column] == 1:
        removeMovement(row, column, is_white, counter, counter + 1)
        return 1
    else:
        removeMovement(row, column, is_white, counter, counter + 0)
        return 0

def removeMovement(row, column, is_white, previous_counter, added_counter):
    ## checking if the piece is white
    if is_white == True:
        if added_counter == 0:
            df_whites_movement.iloc[row, column] -= 1
            df_pinned_by_whites.iloc[row, column] -= 1
        elif added_counter == 1:
            if previous_counter == 0:
                df_whites_movement.iloc[row, column] -= 1
            df_pinned_by_whites.iloc[row, column] -= 1
        else:
            if previous_counter == 1:
                df_pinned_by_whites.iloc[row, column] -= 1

    ## checking if the piece is black
    if is_white == False:
        if added_counter == 0:
            df_blacks_movement.iloc[row, column] -= 1
            df_pinned_by_blacks.iloc[row, column] -= 1
        elif added_counter == 1:
            if previous_counter == 0:
                df_blacks_movement.iloc[row, column] -= 1
        else:
            if previous_counter == 1:
                df_pinned_by_blacks.iloc[row, column] -= 1
