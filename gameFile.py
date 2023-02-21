import sys
import re
import chessGame
import chess
import chess.pgn
#import matplotlib.pyplot as plt

#Task 2
def importGameFromFile():
    try:
        with open("game.pgn", "r") as fp:
            game = chess.pgn.read_game(fp) 
            black_username = game.headers['Black']
            print(black_username)    
            fp.read()
            fp.close()
            return game
    except:
        print("Could not read file") 
    
importGameFromFile()

#TASK 7
def readChessWins(counter):
    try:
        with open("Stockfish_15_64-bit.commented.[2600].pgn" ,"r") as fp:
            for line in fp: 
                line = line.rstrip()
                if re.search("Result", line):
                    if re.search("1-0", line):
                        counter[0] = counter[0] + 1
                    elif re.search("0-1", line):
                        counter[1] = counter[1] + 1
                    else:
                        counter[2] = counter[2] + 1
            fp.close()
    except:
        print("Could not read file") 
        
#TEST 7
# couts = [0,0,0]
# readChessWins(couts)
# print(couts)

#TASK 8
def readNumberOfMovesGames():
    try:
        with open("Stockfish_15_64-bit.commented.[2600].pgn" ,"r") as fp:
            movesList = [] 
            while True: 
                counter = 0
                currentGame = chess.pgn.read_game(fp)
                if currentGame is None: 
                    break
                for el in currentGame.mainline_moves():
                    counter += 1
                movesList.append(counter)
            fp.close()
            return movesList
    except:
        print("Could not read file")  

#TEST TASK 8
#print(readNumberOfMovesGames())

#Creates plot with number of moves

# x = 2600
# y = readNumberOfMovesGames()

# plt.plot(x, y)
# plt.xlabel("Number of games")
# plt.ylabel("Number of moves")
# plt.title("Number of moves in games")
# plt.show()