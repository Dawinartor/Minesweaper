import numpy as np
#row first

array = np.zeros((16,16),dtype=object)

class GameField:
    def __init__(self):
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




def placeZeros():
    for x in range(0,np.size(array,0)):
        for y in range(0,np.size(array,1)):

            if  isinstance(array[x][y],Bomb) == True:
                addValue(x,y)

            array[x][y] = Number(x,y)

def addValue(x,y):
    pass


placeZeros()

array[1][1].increaseNumber()

print(array[1][1].getNumber())