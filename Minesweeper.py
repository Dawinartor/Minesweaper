import numpy as np
#row first

class Gamefield:
    def __init__(self):
        self.__field = np.empty((16,16),dtype=object)
        self.__fieldSize = self.__field.size
        self.fieldSizeX = np.size(self.__field,0)
        self.fieldSizeY  = np.size(self.__field,1)
        self.__bombLocationList = None # define return of placeBombs (tuple list)
    
        self.placeZeros()
        #self.addValue()
            
    def placeBombs(self):
        #TODO: create random generated list of tuple for x & y like [(1,3),(1,5),(1,4)]
        #TODO: - check lists for duplications
        #TODO:  -> if duplication found: replace duplication by create new number which is not in list
        #TODO: - place Bomb in gamefiled
        
        pass
    
    def placeZeros(self):
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):

                if  isinstance(self.__field[x][y],Bomb) == True:
                    continue

                self.__field[x][y] = Number(x,y)

    def addValue(self):
        '''Iterates bombLocationList and calls increaseNumber() method of each surrounding Number objects'''
        for location in self.__bombLocationList:
            x = location[0]
            y = location[1]

            self.__field[x+1][y].increaseNumber()
            self.__field[x][y+1].increaseNumber()
            self.__field[x-1][y].increaseNumber()
            self.__field[x][y-1].increaseNumber()
            self.__field[x+1][y+1].increaseNumber()
            self.__field[x-1][y-1].increaseNumber()
            self.__field[x+1][y-1].increaseNumber()
            self.__field[x-1][y+1].increaseNumber()


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

game = Gamefield()

