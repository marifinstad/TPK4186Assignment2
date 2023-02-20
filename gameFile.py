import sys
import re
import chessGame
import chess
import chess.pgn

#Task 2
def importGameFromFile():
    try:
        with open("game.pgn", "r") as fp:
            game = chess.pgn.read_game(fp)                   
            fp.read()
            fp.close()
            return game
    except:
        print("Could not read file") 
    
importGameFromFile()