import sys
import re
import chessGame
import chess
import chess.pgn



def importGameFromFile():
    try:
        with open("tpk4186_assignment2/game.pgn", "r") as fp:
            game = chess.pgn.read_game(fp)   
            white_username = game.headers['White']
            print(white_username)                 
            fp.read()
            fp.close()
    except:
        print("Could not read file") 
    

#Comment