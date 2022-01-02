import numpy as np
#row first

class Gamefield:
    def __init__(self):
        self.field = np.zeros((16,16),dtype=object)
        self.fieldSize = self.field.size
        self.bombLocationList = None # define return of placeBombs (tuple list)
    
    def placeBombs(self):
        #TODO: create random generated list of tuple for x & y like [(1,3),(1,5),(1,4)]
        #TODO: - check lists for duplications
        #TODO:  -> if duplication found: replace duplication by create new number which is not in list
        #TODO: - place Bomb in gamefiled
        
        #~ create 
    
    def placeZeros(self):
        for x in range(0,np.size(self.field,0)):
            for y in range(0,np.size(self.field,1)):

                if  isinstance(self.field[x][y],Bomb) == True:
                    pass
                    #addValue(x,y)

                self.field[x][y] = Number(x,y)

    def addValue(self,x,y):
        pass

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
