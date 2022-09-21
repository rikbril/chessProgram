"""This file contains all the code regarding the placement of all the pieces, df_blacks/whites and the tracking of those pieces in the corresponding dataframes: 
df_black/white_movement and df_pinned_by_black/white 

these values are generated after an move is made

for the tracking of the movement of a singular piece in a singular direction an dictionary is used. This dictionary has as key the location and as value an cummulative counter 
with the value of 0,1 or 2. 
0: if the value is 0 the piece has free movement in that direction 
1: if the value is 1 it has encountered an singular opponent, the piece can move to this location and kill this opponent. by the next turn this route may be clear therefor
this is regared an pinned piece in order to keep track of low value blocking pieces which protect high value pieces.
2: once 2 opponents have been reached or an friencly piece is in the way it is not possible to attack these by the next turn therefore they are not tracked

the sequences in which the paths are checked is clockwise, starting with 'north' up and ending with 'north-west' these are abriviated

## TODO: knight movement, casteling and enpassant
"""
##
moves_n = {}
moves_ne = {}
moves_e = {}
moves_se = {}
moves_s = {}
moves_sw = {}
moves_w = {}
moves_nw = {}

# showing all the directions in which an part can move, only being used in the final code
def showMoves(self):
    def showMovesN(self): return self.moves_n
    def showMovesNE(self): return self.moves_ne
    def showMovesE(self): return self.moves_e
    def showMovesSE(self): return self.moves_se
    def showMovesS(self): return self.moves_s
    def showMovesSW(self): return self.moves_sw
    def showMovesW(self): return self.moves_w
    def showMovesNW(self): return self.moves_nw
    
## generating the dictionaries of each direction and copying it to the individual piece
def moveChecker(row, rowAdjuster, column, columnAdjuster, is_white, single_move=False):
    """looks at the starting position of an piece and checks all the position in one singular path.

    Args:
        row (int): row position of the piece.
        rowAdjuster (False or +1/-1): If False then it does nothing. -1 it loops through lower row positions, +1 it loops through all higher row positions. 
        column (int): column position of the piece.
        columnAdjuster (False or +1/-1): If False then it does nothing. -1 it loops through lower row positions, +1 it loops through all higher row positions. 
        is_white (bool): checks if the piece is white or black.
        single_move (bool, optional): breaks loop is the piece can only move once. Defaults to False.

    Returns:
        {location: int}: returns the location and a value between 0 and 2. 0 for free movement. 1 if it encounters an opponent or when it can move to that position after a single 
        move of the opposite player and 2 when it encountered a friendly piece or more than 1 opponent 
    """
    result = {}
    loop_counter = 10
    incrementing_rows = False
    incrementing_columns = False
    decrementing_rows = False
    decrementing_columns = False
    
    if rowAdjuster == 1:
        incrementing_rows = True
        loop_counter = 8 - row
    if rowAdjuster == -1:
        decrementing_rows = True
        loop_counter = row + 1
    if columnAdjuster == 1:
        incrementing_columns = True
        if 8 - column < loop_counter:
            loop_counter = 8 - column
    if columnAdjuster == -1:
        decrementing_columns = True
        if column + 1 < loop_counter:
            loop_counter = column + 1
    
    counter = 0
    for x in range(1, loop_counter):
        adjustedRow = row
        adjustedColumn = column
        if incrementing_rows == True:
            adjustedRow += x 
        if decrementing_rows == True:
            adjustedRow -= x
        if incrementing_columns == True:
            adjustedColumn += x 
        if decrementing_columns == True:
            adjustedColumn -= x
        
        counter = counter + addingLocation(adjustedRow, rowAdjuster, adjustedColumn, columnAdjuster, is_white)
        if counter > 2:
            counter = 2  
        result[adjustedRow, adjustedColumn] = counter
        if single_move == True:
            return result
    return result
def addingLocation(row, rowAdjuster, column, columnAdjuster, is_white):
    """adds the values to the moveChecker function

    Args:
        row (int): row position on board
        rowAdjuster (False or +1/-1): If False then it does nothing. -1 it loops through lower row positions, +1 it loops through all higher row positions. 
        column (int): column position on board
        columnAdjuster (False or +1/-1): If False then it does nothing. -1 it loops through lower row positions, +1 it loops through all higher row positions. 
        is_white (bool): checks if the piece is white or black.

    Returns:
        int: 0 if the location is empty, 1 if the location occupied by an opponent, 2 if the location is occupied by a friendly piece.
    """
    if  (df_whites.iloc[row, column] == 1 and is_white == True) or (df_blacks.iloc[row, column] == 1 and is_white == False):
        return 2 
    elif df.iloc[row, column] == 1:
        return 1
    else:
        return 0
 
def checkMovesN(self): self.moves_n = moveChecker(self.location[0], -1, self.location[1], False, self.is_white)
def checkMovesNE(self): self.moves_ne = moveChecker(self.location[0], -1, self.location[1], 1, self.is_white)
def checkMovesE(self): self.moves_e = moveChecker(self.location[0], False, self.location[1], 1, self.is_white)
def checkMovesSE(self): self.moves_se = moveChecker(self.location[0], 1, self.location[1], 1, self.is_white)
def checkMovesS(self): self.moves_s = moveChecker(self.location[0], 1, self.location[1], False, self.is_white)
def checkMovesSW(self): self.moves_sw = moveChecker(self.location[0], 1, self.location[1], -1, self.is_white)
def checkMovesW(self): self.moves_w = moveChecker(self.location[0], False, self.location[1], -1, self.is_white)
def checkMovesNW(self): self.moves_nw = moveChecker(self.location[0], -1, self.location[1], -1, self.is_white)

## adding the values of the dictionaries to the corresponding dataframes
def setMovesN(self): 
    counter = 0 
    for move in self.moves_n: 
        addMovement(move[0], move[1], self.is_white, self.moves_n[move], counter) 
        counter = self.moves_n[move]
def setMovesNE(self): 
    counter = 0 
    for move in self.moves_ne: 
        addMovement(move[0], move[1], self.is_white, self.moves_ne[move], counter) 
        counter = self.moves_ne[move]
def setMovesE(self): 
    counter = 0 
    for move in self.moves_e: 
        addMovement(move[0], move[1], self.is_white, self.moves_e[move], counter) 
        counter = self.moves_e[move]
def setMovesSE(self): 
    counter = 0 
    for move in self.moves_se: 
        addMovement(move[0], move[1], self.is_white, self.moves_se[move], counter) 
        counter = self.moves_se[move]
def setMovesS(self): 
    counter = 0 
    for move in self.moves_s: 
        addMovement(move[0], move[1], self.is_white, self.moves_s[move], counter) 
        counter = self.moves_s[move]
def setMovesSW(self): 
    counter = 0 
    for move in self.moves_sw: 
        addMovement(move[0], move[1], self.is_white, self.moves_sw[move], counter) 
        counter = self.moves_sw[move]
def setMovesW(self): 
    counter = 0 
    for move in self.moves_w: 
        addMovement(move[0], move[1], self.is_white, self.moves_w[move], counter) 
        counter = self.moves_w[move]
def setMovesNW(self): 
    counter = 0 
    for move in self.moves_nw: 
        addMovement(move[0], move[1], self.is_white, self.moves_nw[move], counter) 
        counter = self.moves_nw[move]
    
def addMovement(row, column, is_white, added_counter, previous_counter):
    """takes the values from moveChecker function and adds it to the correct dataframes: white/black_movement and pinned_by_white/black

    Args:
        row (int): row position on board
        column (_type_): column position on board
        is_white (bool): if the piece is white or black
        added_counter (int): cummulative value counter of the current direction 
        previous_counter (int): cummulative value counter of the latest direction, when lower it means that it is possible to attack/keep the piece pinned
    """
    ## checking if the piece is white
    if is_white == True:
        if added_counter == 0:
            df_whites_movement.iloc[row, column] += 1
            df_pinned_by_whites.iloc[row, column] += 1
        elif added_counter == 1:
            df_pinned_by_whites.iloc[row, column] += 1
            if previous_counter == 0:
                df_whites_movement.iloc[row, column] += 1
        else:
            if previous_counter < 2:
                df_pinned_by_whites.iloc[row, column] += 1
    
    ## checking if the piece is black
    if is_white == False:
        if added_counter == 0:
            df_blacks_movement.iloc[row, column] += 1
            df_pinned_by_blacks.iloc[row, column] += 1
        elif added_counter == 1:
            df_pinned_by_blacks.iloc[row, column] += 1
            if previous_counter == 0:
                df_blacks_movement.iloc[row, column] += 1
        else:
            if previous_counter < 2:
                df_pinned_by_blacks.iloc[row, column] += 1

# removing the values of the dictionaries and the corresponding dataframes and clearing the dictionaries of the individual piece
def removeMovesN(self): 
    counter = 0 
    for move in self.moves_n: 
        removeMovement(move[0], move[1], self.is_white, self.moves_n[move], counter) 
        counter = self.moves_n[move]
    self.moves_n = {}
def removeMovesNE(self): 
    counter = 0 
    for move in self.moves_ne: 
        removeMovement(move[0], move[1], self.is_white, self.moves_ne[move], counter) 
        counter = self.moves_ne[move]
    self.moves_ne = {}
def removeMovesE(self): 
    counter = 0 
    for move in self.moves_e: 
        removeMovement(move[0], move[1], self.is_white, self.moves_e[move], counter) 
        counter = self.moves_e[move]
    self.moves_e = {}
def removeMovesSE(self): 
    counter = 0 
    for move in self.moves_se: 
        removeMovement(move[0], move[1], self.is_white, self.moves_se[move], counter) 
        counter = self.moves_se[move]
    self.moves_se = {}
def removeMovesS(self): 
    counter = 0 
    for move in self.moves_s: 
        removeMovement(move[0], move[1], self.is_white, self.moves_s[move], counter) 
        counter = self.moves_s[move]
    self.moves_s
def removeMovesSW(self): 
    counter = 0 
    for move in self.moves_sw: 
        removeMovement(move[0], move[1], self.is_white, self.moves_sw[move], counter) 
        counter = self.moves_sw[move]
    self.moves_sw = {}
def removeMovesW(self): 
    counter = 0 
    for move in self.moves_W: 
        removeMovement(move[0], move[1], self.is_white, self.moves_W[move], counter) 
        counter = self.moves_W[move]
    self.moves_W = {}
def removeMovesNW(self): 
    counter = 0 
    for move in self.moves_nw: 
        removeMovement(move[0], move[1], self.is_white, self.moves_nw[move], counter) 
        counter = self.moves_nw[move]
    self.moves_nw = {}

def removeMovement(row, column, is_white, added_counter, previous_counter):
    """takes the values from moveChecker function and removes it from the correct dataframes: white/black_movement and pinned_by_white/black

    Args:
        row (int): row position on board
        column (_type_): column position on board
        is_white (bool): if the piece is white or black
        added_counter (int): cummulative value counter of the current direction 
        previous_counter (int): cummulative value counter of the latest direction, when lower it means that it is possible to attack/keep the piece pinned
    """
    ## checking if the piece is white
    if is_white == True:
        if added_counter == 0:
            df_whites_movement.iloc[row, column] -= 1
            df_pinned_by_whites.iloc[row, column] -= 1
        elif added_counter == 1:
            df_pinned_by_whites.iloc[row, column] -= 1
            if previous_counter == 0:
                df_whites_movement.iloc[row, column] -= 1
        else:
            if previous_counter < 2:
                df_pinned_by_whites.iloc[row, column] -= 1

    ## checking if the piece is black
    if is_white == False:
        if added_counter == 0:
            df_blacks_movement.iloc[row, column] -= 1
            df_pinned_by_blacks.iloc[row, column] -= 1
        elif added_counter == 1:
            df_pinned_by_blacks.iloc[row, column] -= 1
            if previous_counter == 0:
                df_blacks_movement.iloc[row, column] -= 1
        else:
            if previous_counter < 2:
                df_pinned_by_blacks.iloc[row, column] -= 1
  
