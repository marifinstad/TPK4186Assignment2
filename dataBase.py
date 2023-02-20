
#TASK 4

def newDataBase(name):
    return [name, []]

def getDataBaseName(dataBase):
    return dataBase[0]

def setGameName(dataBase, name):
    dataBase[0] = name

def getDataBaseGames(dataBase):
    return dataBase[1]

def addGameToDataBase(dataBase,game):
    games = getDataBaseGames(dataBase)
    games.append(game)