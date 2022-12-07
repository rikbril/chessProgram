from curses.ascii import isupper
import pandas as pd
from pieces import *
from selfStudie.moves import *

df = pd.DataFrame(index=range(8), columns=range(8))
df_white = pd.DataFrame(index=range(8), columns=range(8))
df_black = pd.DataFrame(index=range(8), columns=range(9))

def createBoard():
    class_dictionary = {"R": Rook, "N": Knight, "B": Bischop, "Q": Queen, "K":King, "P": Pawn}
    class_single_move = {"R": False, "N": True, "B": False, "Q": False, "K":True, "P": True}
    class_spelled_out = {"R": "Rook", "N": "Knight", "B": "Bischop", "Q": "Queen", "K":"King", "P": "Pawn"}
    chess_pieces = {}
    start_fen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"
    numberString = "123456789"

    ## there must be a better way for this
    chess_piece_counter = {"R": 0, "r": 0, "B": 0, "b": 0, "Q": 0, "q": 0, "K": 0, "k": 0, "N": 0, "n": 0, "P": 0, "p": 0}

    count = 0
    for x in range(len(start_fen)):
        if start_fen[x] in numberString:
            count += int(start_fen[x])
        elif start_fen[x] == "/":
            pass
        else:        
            fen_letter  = start_fen[x].capitalize()
            class_spelled_out[fen_letter]
            chess_piece_counter[start_fen[x]] += 1
            location = [count//8, count%8]
            
            is_white = False
            if isupper(start_fen[x]):
                piece_name = class_spelled_out[fen_letter] + "White:"
                is_white = True
            else:
                piece_name = class_spelled_out[fen_letter] +"Black:"
            piece_name += (f"{chess_piece_counter[start_fen[x]]}")
        
            chess_pieces[piece_name] = class_dictionary[fen_letter](piece_name, location, is_white, class_single_move[fen_letter])
            count += 1
            
    return chess_pieces


def movePiece(self, new_location):
    removePinnedMoves()
    piece_on_new_location = self.dictNameFromLocation(new_location)
    if piece_on_new_location:
        chess[piece_on_new_location].removePinnedMoves()
        chess.pop(piece_on_new_location)
        self.location_occupied.pop(piece_on_new_location)
    
    encounters_old_location = self.updateLocation()
    self.location = new_location
    self.location_occupied[self.name] = new_location
    self.setMoves()
    encounters_new_location = self.updateLocation()
    encounters = {**encounters_old_location, **encounters_new_location}
    
    for encounter in encounters:  
        chess[encounter].removePinnedMoves()
        chess[encounter].setMoves()   

def dictKeyFromValue(value):
    for key in chess:
        if chess[key] == value:
            return key

if __name__ == "__main__":
    print("doing something")
    chess = createBoard()
    name = "RookWhite:2"
    chess[name].showLocation()   
    for piece in chess:
        print(piece)
    for piece in chess:
        print(piece)
    chess[name].movePiece([7,7])
    chess[name].showLocation()