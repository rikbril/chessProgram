import pandas as pd

## creates 3 DataFrames, df is for all the pieces on the board, df_movement is for all the places which can be attacked and
## df_pinned is for all the places which can be attacked if the opponent moves a single piece
df = pd.DataFrame(index=range(8), columns=range(8))
df_movement = pd.DataFrame(index=range(8), columns=range(8))
df_pinned = pd.DataFrame(index=range(8), columns=range(8))


def createBoard():
    numberString = "0123456789"
    startFen = "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr"

    for row in range(0, 8):
        for column in range(0, 8):
            df.iloc[row, column] = 0
            df_movement.iloc[row, column] = 0
            df_pinned.iloc[row, column] = 0

    count = 0
    for i in range(len(startFen)):
        if startFen[i] in numberString:
            count = count + int(startFen[i])
        elif startFen[i] != "/":
            df.iloc[(count//8), (count % 8)] = startFen[i]
            count += 1


createBoard()


def moveChecker(location, x, y, is_white, counter=0):
    row = location[0] + x
    column = location[1] + y
