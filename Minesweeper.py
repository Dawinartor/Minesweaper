import numpy as np
import random

class Gamefield:
    def __init__(self):
        self.__field = np.zeros((16,16),dtype=object)
        self.__bombCount = 40 # based on 40 bombs for 256 Tiles 
        self.__fieldSize = self.__field.size
        self.__bombLocationList = [] # define return of placeBombs (tuple list)
    
    def placeBombs(self):
        '''  '''
        
        #TODO: create random generated list of tuple for x & y like [(1,3),(1,5),(1,4)] 40x bombs
        #TODO: - check lists for duplications
        #TODO:  -> if duplication found: replace duplication by create new number which is not in list
        #TODO: - place Bomb in gamefiled
        
        #~ create random int generator
        def generateRandomInt():
            randi = random.randint(0, 15) # 16 in total
            return randi
        
        #~ create touple with using random int generator
        def createTuple():
            # generate x and y random integers
            x = generateRandomInt()
            y = generateRandomInt()
            bombCoordinates = (x, y)
            return bombCoordinates
        
        #~ assign bomb to locationList
        def createBombLocations():
            for bomb in range(0, 40):
                newBombLocation = createTuple()
                self.__bombLocationList.append(newBombLocation)
                
        createBombLocations()
        
        
    
    def placeZeros(self):
        for x in range(0,np.size(self.field,0)):
            for y in range(0,np.size(self.field,1)):

                if  isinstance(self.field[x][y],Bomb) == True:
                    pass
                    #addValue(x,y)

                self.field[x][y] = Number(x,y)

    def addValue(self,x,y):
        pass
    
    # Getter & Setter
    def getFieldSize(self):
        return self.__fieldSize
    
    def getBombLocationList(self):
        return self.__bombLocationList
    

class Tile:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        self.width = 16
        self.height = 16

    def getLocation(self):
        return self.__x,self.__y

class Number(Tile):
    def __init__(self, x, y,number = 0):
        self.__number = number
        super().__init__(x, y)

    def getNumber(self):
        return self.__number

    def increaseNumber(self):
        self.__number += 1


class Bomb(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)


# test method
gameBoard = Gamefield()
gameBoard.placeBombs()
print(gameBoard.getBombLocationList())