class Piece():
    occupied_locations = {}
    piece_types = {"pawn": 1, "rook": 1, "knight": 1, "bischop": 1, "queen": 1, "king": 1}
    
    def __init__(self, name, location, type):
        self.name = name
        self.location = location
        self.type = type
        self.has_moved = False
        Piece.occupied_locations[name] = location
        
    def hasMoved(self):
        return self.has_moved
    
    def moved(self):
        self.has_moved = True
        
def location_empty(location):
    pass
            
class Pawn(Piece):
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
    
    