import numpy as np
#row first

class GameField:
    def __init__(self):
        self.field = np.zeros((16,16),dtype=object)
        self.fieldSize = self.field.size
        self.fieldSizeX = np.size(self.field,0)
        self.fieldSizeY  = np.size(self.field,1)


    def placeZeros(self):
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):

                if  isinstance(self.field[x][y],Bomb) == True:
                    continue

                self.field[x][y] = Number(x,y)

    def addValue(self,x,y):

        # for x in range(0,self.fieldSizeX):
        #     for y in range(0,self.fieldSizeY):
        #         if  isinstance(self.field[x][y],Bomb) == True:
        #             self.field[x+1][y].increaseNumber()
        #             self.field[x][y+1].increaseNumber()
        #             self.field[x-1][y].increaseNumber()
        #             self.field[x][y-1].increaseNumber()
        #             self.field[x+1][y+1].increaseNumber()
        #             self.field[x-1][y-1].increaseNumber()
        #             self.field[x+1][y-1].increaseNumber()
        #             self.field[x-1][y+1].increaseNumber()

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
