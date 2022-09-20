import pandas as pd

## creates 4 DataFrames, df is for all the pieces on the board. df_whites is for all the white pieces on the board. df_movement is for all the places 
## which can be attacked and df_pinned is for all the places which can be attacked if the opponent moves a single piece
df = pd.DataFrame(index=range(8), columns=range(8))
df_whites = pd.DataFrame(index=range(8), columns=range(8))
df_blacks = pd.DataFrame(index=range(8), columns=range(8))
df_whites_movement = pd.DataFrame(index=range(8), columns=range(8))
df_blacks_movement = pd.DataFrame(index=range(8), columns=range(8))
df_pinned_by_whites = pd.DataFrame(index=range(8), columns=range(8))
df_pinned_by_blacks = pd.DataFrame(index=range(8), columns=range(8))

## places the pieces of both sides on the board
def createBoard():
    ## the startFen starts at df location [0,0]. from here it moves one piece to the side in the same column and jumps to the next row after the last column.
    ## whenever there is a number in the Fen an amount equal to that number will be skipped in the dataframe following the simple logic stated above.
    ## The capitalized numbers are for white and the lowercase numbers are for black 
    numberString = "0123456789"
    startFen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"

    for row in range(0, 8):
        for column in range(0, 8):
            df.iloc[row, column] = 0
            df_whites.iloc[row, column] = 0
            df_whites_movement.iloc[row, column] = 0
            df_pinned_by_whites.iloc[row, column] = 0
            df_blacks.iloc[row, column] = 0
            df_blacks_movement.iloc[row, column] = 0
            df_pinned_by_blacks.iloc[row, column] = 0

    count = 0
    for i in range(len(startFen)):
        if startFen[i] in numberString:
            count = count + int(startFen[i])
        elif startFen[i] != "/":
            df.iloc[(count//8), (count % 8)] = startFen[i]
            if startFen[i] == startFen[i].capitalize():
                print(count)
                ## just in case reserved for later
            count += 1

createBoard()

def moveChecker(location, x, y, counter=0):
    row = location[0] + x
    column = location[1] + y

def locationEmptyWhite(row, column):
    if df_whites.iloc[row, column] == 1:
        return [True, True]
    elif df.iloc[row, column] == 1:
        return [True, False]
    else:
        return [False]
