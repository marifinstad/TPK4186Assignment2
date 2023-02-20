#TASK 1

def newGame(event, opening):
    return [event, opening]

def getGameEvent(game):
    return game[0]

def setGameEvent(game, event):
    game[0] = event

def setGameOpening(game,opening):
    game[1] = opening

def getGameOpening(game):
    return game[1]