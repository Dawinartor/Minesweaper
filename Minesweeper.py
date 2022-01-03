import numpy as np
import random
from matplotlib import pyplot as plt
from itertools import product
from random import sample

class Gamefield:
    def __init__(self):
        self.__field = np.empty((16,16),dtype=object)
        self.__fieldSize = self.__field.size
        self.fieldSizeX = np.size(self.__field,0)
        self.fieldSizeY  = np.size(self.__field,1)
        self.__bombLocationList = [] # define return of placeBombs (tuple list)
        self.__bombCount = 40 # based on 40 bombs for 256 Tiles 
    
        self.placeZeros()
        self.placeBombs()
        self.addValue()
        
        self.test = np.zeros((16,16))
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):
                self.test[x][y] = self.__field[x][y].getNumber()

            
    def placeBombs(self):
        '''Create random generated list of tuples and place out of them Bombs in filed'''
        
        #TODO: check for a numpy alternative
        
        #~ create bombLocationList with unique locations
        def createBombLocationList():
            self.__bombLocationList = sample(list(product(range(self.fieldSizeX), range(self.fieldSizeY), repeat=1)), k=self.__bombCount)
                
        #~ place bombs in field
        def placeBombs():
            #* iterate through bombLocationList
            for mockupBomb in self.__bombLocationList:
                #* define x & y coordinates
                x = mockupBomb[0]
                y = mockupBomb[1]
                #* place the bomb in field               
                self.__field[x][y] = Bomb(x, y) 
        
        #~ use main created methods
        createBombLocationList()
        placeBombs()

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
            
            locationList = [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1)]

            for value in locationList:
                if not (value[0]<0 or value[1]<0 or value[0]>15 or value[1]>15): #cheking if x or y value is outside the field
                    try:
                        self.__field[value[0]][value[1]].increaseNumber()
                    except:
                        continue
                  
    # Getter & Setter
    def getFieldSize(self):
        return self.__fieldSize
    
    def getBombLocationList(self):
        return self.__bombLocationList
    
    def getBombCount(self):
        return self.__bombCount
    
    def getField(self):
        return self.__field
    
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
        
    # this is for testing purpose
    def getNumber(self):
        return
    

game = Gamefield()
plt.imshow(game.test)
plt.show()
