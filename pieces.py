
class Piece():    
    occupied_locations = {}
    opponent_locations = {}
    piece_types = {"pawn": 1, "rook": 1, "knight": 1,
                   "bischop": 1, "queen": 1, "king": 1}

    def __init__(self, name, location, is_white):
        self.name = name
        self.location = location
        df.iloc[location[0], location[1]] += 1
        self.is_white = is_white
        self.has_moved = False
        Piece.occupied_locations[name] = location
        if is_white == True:
            df_whites.iloc[location[0], location[1]] += 1
        if is_white == False:
            df_blacks.iloc[location[0], location[1]] += 1

    def hasMoved(self):
        return self.has_moved

    def moved(self):
        self.has_moved = True

    def isWhite(self):
        return self.is_white
    
    def showLocation(self):
        return self.location
    
    white_enpassant = False
    black_enpassant = False
    
    def setWhiteEnpassant(self, location):
        self.white_enpassant = location
        
    def removeWhiteEnpassant(self):
        self.white_enpassant = False
        
    def setBlackEnpassant(self, location):
        self.black_enpassant = location
        
    def removeBlackEnpassant(self):
        self.black_enpassant = False
        
    moves_up = {}
    moves_down = {}
    moves_left = {}
    moves_right = {}
    moves_ne = {}
    moves_se = {}
    moves_sw = {}
    moves_nw = {}
    
    def showMovesUp(self): return self.moves_up
    def showMovesNE(self): return self.moves_ne
    def showMovesRight(self): return self.moves_right
    def showMovesSE(self): return self.moves_se
    def showMovesdown(self): return self.moves_down
    def showMovesSW(self): return self.moves_sw
    def showMovesLeft(self): return self.moves_left
    def showMovesNW(self): return self.moves_nw
        
    def checkMovesUp(self): self.moves_up = moveChecker(self.location[0], -1, self.location[1], False, self.is_white)
    def checkMovesNE(self): self.moves_ne = moveChecker(self.location[0], -1, self.location[1], 1, self.is_white)
    def checkMovesRight(self): self.moves_right = moveChecker(self.location[0], False, self.location[1], 1, self.is_white)
    def checkMovesSE(self): self.moves_se = moveChecker(self.location[0], 1, self.location[1], 1, self.is_white)
    def checkMovesDown(self): self.moves_down = moveChecker(self.location[0], 1, self.location[1], False, self.is_white)
    def checkMovesSW(self): self.moves_sw = moveChecker(self.location[0], 1, self.location[1], -1, self.is_white)
    def checkMovesLeft(self): self.moves_left = moveChecker(self.location[0], False, self.location[1], -1, self.is_white)
    def checkMovesNW(self): self.moves_nw = moveChecker(self.location[0], -1, self.location[1], -1, self.is_white)
    
    def setMovesUp(self): 
        counter = 0 
        for move in self.moves_up: 
            addMovement(move[0], move[1], self.is_white, self.moves_up[move], counter) 
            counter = self.moves_up[move]
    def setMovesNE(self): 
        counter = 0 
        for move in self.moves_ne: 
            addMovement(move[0], move[1], self.is_white, self.moves_ne[move], counter) 
            counter = self.moves_ne[move]
    def setMovesRight(self): 
        counter = 0 
        for move in self.moves_right: 
            addMovement(move[0], move[1], self.is_white, self.moves_right[move], counter) 
            counter = self.moves_right[move]
    def setMovesSE(self): 
        counter = 0 
        for move in self.moves_se: 
            addMovement(move[0], move[1], self.is_white, self.moves_se[move], counter) 
            counter = self.moves_se[move]
    def setMovesDown(self): 
        counter = 0 
        for move in self.moves_down: 
            addMovement(move[0], move[1], self.is_white, self.moves_down[move], counter) 
            counter = self.moves_down[move]
    def setMovesSW(self): 
        counter = 0 
        for move in self.moves_sw: 
            addMovement(move[0], move[1], self.is_white, self.moves_sw[move], counter) 
            counter = self.moves_sw[move]
    def setMovesLeft(self): 
        counter = 0 
        for move in self.moves_left: 
            addMovement(move[0], move[1], self.is_white, self.moves_left[move], counter) 
            counter = self.moves_left[move]
    def setMovesNW(self): 
        counter = 0 
        for move in self.moves_nw: 
            addMovement(move[0], move[1], self.is_white, self.moves_nw[move], counter) 
            counter = self.moves_nw[move]
        
    def removeMovesUp(self): 
        counter = 0 
        for move in self.moves_up: 
            removeMovement(move[0], move[1], self.is_white, self.moves_up[move], counter) 
            counter = self.moves_up[move]
        self.moves_up = {}
    def removeMovesNE(self): 
        counter = 0 
        for move in self.moves_ne: 
            removeMovement(move[0], move[1], self.is_white, self.moves_ne[move], counter) 
            counter = self.moves_ne[move]
        self.moves_ne = {}
    def removeMovesRight(self): 
        counter = 0 
        for move in self.moves_right: 
            removeMovement(move[0], move[1], self.is_white, self.moves_right[move], counter) 
            counter = self.moves_right[move]
        self.moves_right = {}
    def removeMovesSE(self): 
        counter = 0 
        for move in self.moves_se: 
            removeMovement(move[0], move[1], self.is_white, self.moves_se[move], counter) 
            counter = self.moves_se[move]
        self.moves_se = {}
    def removeMovesDown(self): 
        counter = 0 
        for move in self.moves_down: 
            removeMovement(move[0], move[1], self.is_white, self.moves_down[move], counter) 
            counter = self.moves_down[move]
        self.moves_down
    def removeMovesSW(self): 
        counter = 0 
        for move in self.moves_sw: 
            removeMovement(move[0], move[1], self.is_white, self.moves_sw[move], counter) 
            counter = self.moves_sw[move]
        self.moves_sw = {}
    def removeMovesLeft(self): 
        counter = 0 
        for move in self.moves_left: 
            removeMovement(move[0], move[1], self.is_white, self.moves_left[move], counter) 
            counter = self.moves_left[move]
        self.moves_left = {}
    def removeMovesNW(self): 
        counter = 0 
        for move in self.moves_nw: 
            removeMovement(move[0], move[1], self.is_white, self.moves_nw[move], counter) 
            counter = self.moves_nw[move]
        self.moves_nw = {}
class PawnWhite(Piece):
    moves_up = []
    attack_NE = []
    attacl_NW = []
    enpassant_NE = False
    enpassant_NW = False
        
    def setMoves(self):
        self.moves_up = moveUp(self.location[0], self.location[1], self.is_white, True)
        if self.moves_up[0] == 0 and self.has_moved == False:
            self.moves_up.append(moveUp(self.location[0] - 1, self.location[1], self.is_white, True))
    def removeMoves(self):
        if self.moves_up[0] == 0 and self.has_moved == False:
            removeUp(self.location[0] - 1, self.location[1], self.is_white, True)
        removeUp(self.location[0], self.location[1], self.is_white, True)
    
    def moveAttackNE(self):
        self.attack_NE = moveNE(self.location[0], self.location[1], self.is_white, True)
    def removeAttackNE(self):
        removeNE(self.location[0], self.location[1], self.is_white, True)
        self.attack_NE = []
        
    def moveAttackNW(self):
        self.attack_NW = moveNW(self.location[0], self.location[1], self.is_white, True)
    def removeAttackNW(self):
        removeNW(self.location[0], self.location[1], self.is_white, True)
        self.attack_NW = []
        
    def moveEnpassantNE(self):
        self.enpassant_NE = True
        df_whites_movement.iloc[self.location[0] -1, self.location[1] + 1] += 1
        df_pinned_by_whites.iloc[self.location[0] -1, self.location[1] + 1] += 1
    def removeEnpassantNE(self):
        self.enpassant_NE = False
        df_whites_movement.iloc[self.location[0] -1, self.location[1] + 1] -= 1
        df_pinned_by_whites.iloc[self.location[0] -1, self.location[1] + 1] -= 1
        
    def moveEnpassantNW(self):
        self.enpassant_NW = True
        df_whites_movement.iloc[self.location[0] -1, self.location[1] - 1] += 1
        df_pinned_by_whites.iloc[self.location[0] -1, self.location[1] - 1] += 1
    def removeEnpassantNW(self):
        self.enpassant_NW = False        
        df_whites_movement.iloc[self.location[0] -1, self.location[1] - 1] -= 1
        df_pinned_by_whites.iloc[self.location[0] -1, self.location[1] - 1] -= 1
class Rook(Piece):
    piece_moves_up = True
    piece_moves_ne = False
    piece_moves_right = True
    piece_moves_se = False
    piece_moves_down = True
    piece_moves_sw = False
    piece_moves_left = True
    piece_moves_nw = False
    
    def showMoves(self):
        if self.piece_moves_up == True: 
            return self.moves_up 
        if self.piece_moves_ne == True: 
            return self.moves_ne 
        if self.piece_moves_right == True: 
            return self.moves_right 
        if self.piece_moves_se == True: 
            return self.moves_se 
        if self.piece_moves_down == True: 
            return self.moves_down 
        if self.piece_moves_sw == True: 
            return self.moves_sw 
        if self.piece_moves_left == True: 
            return self.moves_left 
        if self.piece_moves_nw == True: 
            return self.moves_nw 
    
    def checkMoves(self):
        if self.piece_moves_up == True: 
            self.checkMovesUp()
        if self.piece_moves_ne == True: 
            self.checkMovesNE()
        if self.piece_moves_right == True: 
            self.checkMovesRight()
        if self.piece_moves_se == True: 
            self.checkMovesSE()
        if self.piece_moves_down == True: 
            self.checkMovesDown()
        if self.piece_moves_sw == True: 
            self.checkMovesSW()
        if self.piece_moves_left == True: 
            self.checkMovesLeft()
        if self.piece_moves_nw == True: 
            self.checkMovesNW()
            
    def setMoves(self):
        if self.piece_moves_up == True: 
            self.setMovesUp()
        if self.piece_moves_ne == True: 
            self.setMovesNE()
        if self.piece_moves_right == True: 
            self.setMovesRight()
        if self.piece_moves_se == True: 
            self.setMovesSE()
        if self.piece_moves_down == True: 
            self.setMovesDown()
        if self.piece_moves_sw == True: 
            self.setMovesSW()
        if self.piece_moves_left == True: 
            self.setMovesLeft()
        if self.piece_moves_nw == True: 
            self.setMovesNW()
            
    def removeMoves(self):
        if self.piece_moves_up == True: 
            self.removeMovesUp()
        if self.piece_moves_ne == True: 
            self.removeMovesNE()
        if self.piece_moves_right == True: 
            self.removeMovesRight()
        if self.piece_moves_se == True: 
            self.removeMovesSE()
        if self.piece_moves_down == True: 
            self.removeMovesDown()
        if self.piece_moves_sw == True: 
            self.removeMovesSW()
        if self.piece_moves_left == True: 
            self.removeMovesLeft()
        if self.piece_moves_nw == True: 
            self.removeMovesNW()
        
    def temp():
        def pieceMoveUp(self):
            self.moves_up = moveUp(self.location[0], self.location[1], self.is_white)
        def pieceReMoveUp(self):
            removeUp(self.location[0], self.location[1], self.is_white)

        def pieceMoveDown(self):
            self.moves_down = moveDown(self.location[0], self.location[1], self.is_white)
        def pieceReMoveDown(self):
            self.moves_down = removeDown(self.location[0], self.location[1], self.is_white)
        
        def pieceMoveLeft(self):
            self.moves_left = moveLeft(self.location[0], self.location[1], self.is_white)
        def pieceReMoveLeft(self):
            self.moves_left = removeLeft(self.location[0], self.location[1], self.is_white)

        def pieceMoveRight(self):
            self.moves_right = moveRight(self.location[0], self.location[1], self.is_white)
        def pieceReMoveRight(self):
            self.moves_right = removeRight(self.location[0], self.location[1], self.is_white)
class Knight(Piece):
    possible_moves = []
class Bischop(Piece):
    moves_ne = {}
    moves_se = {}
    moves_sw = {}
    moves_nw = {}
    
    def showMoves(self):
        return [self.moves_ne, self.moves_se, self.moves_sw, self.moves_nw]
    
    def checkMoves(self):
        self.moves_ne = moveChecker(self.location[0], -1, self.location[1], 1, self.is_white)
        self.moves_se = moveChecker(self.location[0], 1, self.location[1], 1, self.is_white)
        self.moves_sw = moveChecker(self.location[0], 1, self.location[1], -1, self.is_white)
        self.moves_nw = moveChecker(self.location[0], -1, self.location[1], -1, self.is_white)
    
    def setMoves(self):
        counter = 0
        for move in self.moves_ne:
            addMovement(move[0], -1, move[1], 1, self.is_white, self.moves_ne[move], counter)
            counter = self.moves_ne[move]
        counter = 0
        for move in self.moves_se:
            addMovement(move[0], 1, move[1], 1, self.is_white, self.moves_se[move], counter)
            counter = self.moves_se[move]
        counter = 0
        for move in self.moves_sw:
            addMovement(move[0], 1, move[1], -1, self.is_white, self.moves_sw[move], counter)
            counter = self.moves_sw[move]
        counter = 0
        for move in self.moves_nw:
            addMovement(move[0], -1, move[1], -1, self.is_white, self.moves_nw[move], counter)
            counter = self.moves_nw[move]
    
    def removeMoves(self):
        counter = 0
        for move in self.moves_ne:
            removeMovement(move[0], -1, move[1], 1, self.is_white, self.moves_ne[move], counter)
            counter = self.moves_ne[move]
        counter = 0
        for move in self.moves_se:
            removeMovement(move[0], 1, move[1], 1, self.is_white, self.moves_se[move], counter)
            counter = self.moves_se[move]
        counter = 0
        for move in self.moves_sw:
            removeMovement(move[0], 1, move[1], -1, self.is_white, self.moves_sw[move], counter)
            counter = self.moves_sw[move]
        counter = 0
        for move in self.moves_nw:
            removeMovement(move[0], -1, move[1], -1, self.is_white, self.moves_nw[move], counter)
            counter = self.moves_nw[move]
        moves_ne = {}
        moves_se = {}
        moves_sw = {}
        moves_nw = {}
class Queen(Piece):
    piece_moves_up = True
    piece_moves_ne = True
    piece_moves_right = True
    piece_moves_se = True
    piece_moves_down = True
    piece_moves_sw = True
    piece_moves_left = True
    piece_moves_nw = True
    
    def showMoves(self):
        if self.piece_moves_up == True: 
            return self.moves_up 
        if self.piece_moves_ne == True: 
            return self.moves_ne 
        if self.piece_moves_right == True: 
            return self.moves_right 
        if self.piece_moves_se == True: 
            return self.moves_se 
        if self.piece_moves_down == True: 
            return self.moves_down 
        if self.piece_moves_sw == True: 
            return self.moves_sw 
        if self.piece_moves_left == True: 
            return self.moves_left 
        if self.piece_moves_nw == True: 
            return self.moves_nw 
    
    def checkMoves(self):
        if self.piece_moves_up == True: 
            self.checkMovesUp()
        if self.piece_moves_ne == True: 
            self.checkMovesNE()
        if self.piece_moves_right == True: 
            self.checkMovesRight()
        if self.piece_moves_se == True: 
            self.checkMovesSE()
        if self.piece_moves_down == True: 
            self.checkMovesDown()
        if self.piece_moves_sw == True: 
            self.checkMovesSW()
        if self.piece_moves_left == True: 
            self.checkMovesLeft()
        if self.piece_moves_nw == True: 
            self.checkMovesNW()
            
    def setMoves(self):
        if self.piece_moves_up == True: 
            self.setMovesUp()
        if self.piece_moves_ne == True: 
            self.setMovesNE()
        if self.piece_moves_right == True: 
            self.setMovesRight()
        if self.piece_moves_se == True: 
            self.setMovesSE()
        if self.piece_moves_down == True: 
            self.setMovesDown()
        if self.piece_moves_sw == True: 
            self.setMovesSW()
        if self.piece_moves_left == True: 
            self.setMovesLeft()
        if self.piece_moves_nw == True: 
            self.setMovesNW()
            
    def removeMoves(self):
        if self.piece_moves_up == True: 
            self.removeMovesUp()
        if self.piece_moves_ne == True: 
            self.removeMovesNE()
        if self.piece_moves_right == True: 
            self.removeMovesRight()
        if self.piece_moves_se == True: 
            self.removeMovesSE()
        if self.piece_moves_down == True: 
            self.removeMovesDown()
        if self.piece_moves_sw == True: 
            self.removeMovesSW()
        if self.piece_moves_left == True: 
            self.removeMovesLeft()
        if self.piece_moves_nw == True: 
            self.removeMovesNW()
class King(Piece):
    #directions:   n    ne    e     se    s     sw    w     nw
    direction = [True, True, True, True, True, True, True, True]
    
    
    def showMoves(self):
        if self.piece_moves_up == True: 
            return self.moves_up 
        if self.piece_moves_ne == True: 
            return self.moves_ne 
        if self.piece_moves_right == True: 
            return self.moves_right 
        if self.piece_moves_se == True: 
            return self.moves_se 
        if self.piece_moves_down == True: 
            return self.moves_down 
        if self.piece_moves_sw == True: 
            return self.moves_sw 
        if self.piece_moves_left == True: 
            return self.moves_left 
        if self.piece_moves_nw == True: 
            return self.moves_nw 
    
    def checkMoves(self):
        if self.piece_moves_up == True: 
            self.checkMovesUp()
        if self.piece_moves_ne == True: 
            self.checkMovesNE()
        if self.piece_moves_right == True: 
            self.checkMovesRight()
        if self.piece_moves_se == True: 
            self.checkMovesSE()
        if self.piece_moves_down == True: 
            self.checkMovesDown()
        if self.piece_moves_sw == True: 
            self.checkMovesSW()
        if self.piece_moves_left == True: 
            self.checkMovesLeft()
        if self.piece_moves_nw == True: 
            self.checkMovesNW()
            
    def setMoves(self):
        if self.piece_moves_up == True: 
            self.setMovesUp()
        if self.piece_moves_ne == True: 
            self.setMovesNE()
        if self.piece_moves_right == True: 
            self.setMovesRight()
        if self.piece_moves_se == True: 
            self.setMovesSE()
        if self.piece_moves_down == True: 
            self.setMovesDown()
        if self.piece_moves_sw == True: 
            self.setMovesSW()
        if self.piece_moves_left == True: 
            self.setMovesLeft()
        if self.piece_moves_nw == True: 
            self.setMovesNW()
            
    def removeMoves(self):
        if self.piece_moves_up == True: 
            self.removeMovesUp()
        if self.piece_moves_ne == True: 
            self.removeMovesNE()
        if self.piece_moves_right == True: 
            self.removeMovesRight()
        if self.piece_moves_se == True: 
            self.removeMovesSE()
        if self.piece_moves_down == True: 
            self.removeMovesDown()
        if self.piece_moves_sw == True: 
            self.removeMovesSW()
        if self.piece_moves_left == True: 
            self.removeMovesLeft()
        if self.piece_moves_nw == True: 
            self.removeMovesNW()
    
