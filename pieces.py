class Piece():
    location_occupied = {}
    pressured_by_white = {}
    pressured_by_black = {}
    
    def __init__(self, name, location, is_white, single_move):
        self.name = name
        self.location = location
        self.location_occupied[name] = location
        self.is_white = is_white
        self.single_move = single_move
        self.movement = []
        self.pinned = []
        self.directions = self.setDirections()
        
    def setDirections(self, directions=False):
        result = []
        if directions:
            for direction in directions:
                adjusting_directions = direction.split("-")
                result.append(self.locationAdjuster(adjusting_directions))            
        else:
            for direction in self.movement_directions:
                adjusting_directions = direction.split("-")
                result.append(self.locationAdjuster(adjusting_directions))
        return result
    
    def setPressuredLists(self):
        for x in range(0,64):
            self.pressured_by_white[(f"{x//8, x%8}")] = 0
            self.pressured_by_black[(f"{x//8, x%8}")] = 0
    def showName(self):
        print(self.name)
    def showLocation(self):
        print(self.location)
    def showOccupiedLocations(self):
        print(self.location_occupied)
    def locationColor(self):
        return self.is_white
    def showMovement(self):
        print(self.movement)
    def showPinned(self):
        print(self.pinned)
    def showMovementDirections(self):
        print(self.movement_directions)
     
    def dictNameFromLocation(self, location):
        for key in self.location_occupied:
            if self.location_occupied[key] == location:
                return key
    
    def locationAdjuster(self, directions):
        row_adjustment = 0
        column_adjustment = 0
        for direction in directions:
            if direction == "north":
                row_adjustment -= 1
            if direction == "south":
                row_adjustment += 1
            if direction == "west":
                column_adjustment -= 1
            if direction == "east":
                column_adjustment += 1
        return [row_adjustment, column_adjustment]   
    def locationChecker(self, row_adjustment, column_adjustment):
        result = []
        counter = 0
        looping = True
        adjusted_row = self.location[0] + row_adjustment
        adjusted_column = self.location[1] + column_adjustment
        while looping:   
            if adjusted_row < 0 or adjusted_row > 7:
                break
            if adjusted_column < 0 or adjusted_column > 7:
                break
            
            for value in self.location_occupied:
                if self.location_occupied[value] == [adjusted_row, adjusted_column]:
                    is_white = chess_pieces[value].locationColor()
                    if is_white:
                        counter += 2
                    else:
                        counter += 1
            
            if counter > 2:
                counter = 2
                        
            result.append(counter)
            adjusted_row += row_adjustment
            adjusted_column += column_adjustment

            if self.single_move:
                break
        return result
    def locationName(self, row_adjustment, column_adjustment, single_move):
        encounters = {}
        looping = True
        adjusted_row = self.location[0] + row_adjustment
        adjusted_column = self.location[1] + column_adjustment
        while looping:   
            if adjusted_row < 0 or adjusted_row > 7:
                break
            if adjusted_column < 0 or adjusted_column > 7:
                break
        
            name = self.dictNameFromLocation([adjusted_row, adjusted_column])
            if name:
                encounters[name] = [adjusted_row, adjusted_column]
                
            adjusted_row += row_adjustment
            adjusted_column += column_adjustment
            
            if single_move:
                break
        return encounters
    
    def setMoves(self):
        self.movement = []
        self.pinned = []
        for direction in self.directions:
            self.movement.append(self.locationChecker(direction[0], direction[1]))
            
        for x in range(len(self.movement)):
            previous_counter = 0
            self.pinned.append([])
            for y in range(len(self.movement[x])):
                if self.movement[x][y] < 2 or previous_counter < 2:
                    self.pinned[x].append(1)
                previous_counter = self.movement[x][y]
        self.addPinnedMoves()
    def addPinnedMoves(self):
        for movement_direction in range(len(self.pinned)):
            if self.pinned[movement_direction] != None:
                adjusted_row = self.location[0] + self.directions[movement_direction][0]
                adjusted_column = self.location[1] + self.directions[movement_direction][1]
                for move in self.pinned[movement_direction]:
                    if self.is_white:
                        self.pressured_by_white[(f"{adjusted_row, adjusted_column}")] += 1
                    else:
                        self.pressured_by_black[(f"{adjusted_row, adjusted_column}")] += 1
                    adjusted_row += self.directions[movement_direction][0]
                    adjusted_column += self.directions[movement_direction][1] 
    def removePinnedMoves(self):
        for movement_direction in range(len(self.pinned)):
            if self.pinned[movement_direction] != None:
                adjusted_row = self.location[0] + self.directions[movement_direction][0]
                adjusted_column = self.location[1] + self.directions[movement_direction][1]
                for move in self.pinned[movement_direction]:
                    if self.is_white:
                        self.pressured_by_white[(f"{adjusted_row, adjusted_column}")] -= 1
                    else:
                        self.pressured_by_black[(f"{adjusted_row, adjusted_column}")] -= 1
                    adjusted_row += self.directions[movement_direction][0]
                    adjusted_column += self.directions[movement_direction][1] 
        self.pinned = []            
    
    def movePiece(self, new_location):
        self.removePinnedMoves()
        piece_on_new_location = self.dictNameFromLocation(new_location)
        if piece_on_new_location:
            # chess_pieces[piece_on_new_location].removePinnedMoves()
            # chess_pieces.pop(piece_on_new_location)
            self.location_occupied.pop(piece_on_new_location)
        
        encounters_old_location = self.updateLocation()
        self.location = new_location
        self.location_occupied[self.name] = new_location
        self.setMoves()
        encounters_new_location = self.updateLocation()
        encounters = {**encounters_old_location, **encounters_new_location}
        
        for encounter in encounters:  
            chess_pieces[encounter].removePinnedMoves()
            chess_pieces[encounter].setMoves()        
    def updateLocation(self):
        update_movement = []
        encounters= {}
        update_directions = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west",
                            "north-north-east", "east-east-north", "east-east-south", "south-south-east", 
                            "south-south-west", "west-west-south", "west-west-north", "north-north-west"]
        directions = self.setDirections(update_directions)
        for direction in directions:
            update_movement.append([direction[0], direction[1]])
        
        for direction in update_movement:
            if direction[0] == 2 or direction[0] == -2 or direction[1] == 2 or direction[1] == -2:
                lst = self.locationName(direction[0], direction[1], True)
                for encounter in lst:
                    encounters[encounter] = lst[encounter]
            else:
                lst = self.locationName(direction[0], direction[1], False)
                for encounter in lst:
                    encounters[encounter] = lst[encounter]
        return encounters

class Rook(Piece):
    movement_directions = ["north", "east", "south", "west"]

class Bischop(Piece):
    movement_directions = ["north-east", "south-east", "south-west", "north-west"]    

class King(Piece):
    movement_directions = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]

class Queen(Piece):
    movement_directions = ["north", "north-east", "east", "south-east", "south", "south-west", "west", "north-west"]

class Knight(Piece):
    movement_directions = ["north-north-east", "east-east-north", "east-east-south", "south-south-east", 
                           "south-south-west", "west-west-south", "west-west-north", "north-north-west"]

class Pawn(Piece):
    ## directions for pawns are vertical, enpassant east, enpassant west, dubble vertical.
    ## the vertical movement for white is south and for black it is north
    movement_directions = []
    
    def __init__(self, name, location, is_white, single_move):
        super().__init__(name, location, is_white, single_move)
        if self.is_white:
            self.movement_directions = ["south", "south-east", "south-west", "south-south"]
        else:
            self.movement_directions = ["north", "north-east", "north-west", "north-north"]
        self.directions = self.setDirections()
    
    def setMoves(self):
        self.movement = []
        self.pinned = []
        for x in range(len(self.directions)):
            self.pinned.append([])
            location_score = self.locationChecker(self.directions[x][0], self.directions[x][1])
            if location_score:
                if x == 0:
                    if location_score == 0:
                        self.movement.append(0)
                    else:
                        self.movement.append(2)
                elif x == 3:
                    if (location_score[0] + self.movement[0]) == 0:
                        self.movement.append(0)
                    else:
                        self.movement.append(2)
                else:
                    if location_score == 1:
                        self.movement.append(1)
                    else:
                        self.movement.append(2)
                    self.pinned[x].append(1)
        self.addPinnedMoves()
    
    def addPinnedMoves(self):
        for x in range(len(self.pinned)):
            if x == 1 or x == 2:
                for y in range(len(self.pinned[x])):
                    if y:
                        if self.is_white:
                            self.pressured_by_white[(f"{(self.location[0]+1), (self.location[1]+self.directions[x][1])}")] += 1
                        else:
                            self.pressured_by_black[(f"{(self.location[0]-1), (self.location[1]+self.directions[x][1])}")] += 1
        
    def removePinnedMoves(self):
        for x in range(len(self.pinned)):
            if x == 1 or x == 2:
                for y in range(len(self.pinned[x])):
                    if y:
                        if self.is_white:
                            self.pressured_by_white[(f"{(self.location[0]+1), (self.location[1]+self.directions[x][1])}")] -= 1
                        else:
                            self.pressured_by_black[(f"{(self.location[0]-1), (self.location[1]+self.directions[x][1])}")] -= 1
