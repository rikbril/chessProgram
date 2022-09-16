class Piece():
    occupied_locations = {}
    piece_types = {"pawn": 1, "rook": 1, "knight": 1, "bischop": 1, "queen": 1, "king": 1}
    
    def __init__(self, name, location, is_white):
        self.name = name
        self.location = location
        self.is_white = is_white
        self.has_moved = False
        Piece.occupied_locations[name] = location
    
    def showLocation(self):
        return self.location
    
    def setLocation(self, x, y):
        self.location = [x, y]
        
    def hasMoved(self):
        return self.has_moved
    
    def moved(self):
        self.has_moved = True
        
    def isWhite(self):
        return self.is_white
        
def location_empty(location):
    pass
            
class PawnWhite(Piece):
    possible_moves = []
    
class PawnBlack(Piece):
    possible_moves = []
    
class Rook(Piece):
    possible_moves = []
    
class Knight(Piece):
    possible_moves = []
    
class Bischop(Piece):
    possible_moves = []

class Queen(Piece):
    possible_moves = []

class King(Piece):
    possible_moves = []
    
    