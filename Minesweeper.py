import numpy as np
from matplotlib import pyplot as plt
from itertools import product
from random import sample
from Number import Number
from Bomb import Bomb

class Gamefield:
    """
    A class to represent a person.
    ...

    Attributes
    ----------
    __field : ndarray
        empty numpy array that represents game field
    __fieldSize : int
        size of the field
    fieldSizeX : int
        size of the array in x axis
    fieldSizeY : int
        size of the array in y axis
    __bombLocationList : list
        contains locations of genereted bombs
    __bombCount: int
        amount of bomb in the field

    Methods
    -------
    placeBombs():
        Places bomb objects into the field.
    placeZeros():
        Fills field array with number objects.
    addValue():
        Manipulates number objects around bombs.
    getFieldSize():
        returns __fieldSize
    getBombLocationList():
        returns __bombLocationList
    getField():
        returns __field
    """
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
        
        def createBombLocationList():
            #TODO: descripe one line code
            self.__bombLocationList = sample(list(product(range(self.fieldSizeX), range(self.fieldSizeY), repeat=1)), k=self.__bombCount)
                
        def placeBombs():
            '''Itarets through __bombLocationList and creates bomb objects at that coordinate
            '''
            for mockupBomb in self.__bombLocationList:
                #* define x & y coordinates
                x = mockupBomb[0]
                y = mockupBomb[1]
          
                self.__field[x][y] = Bomb(x, y) 
        
        #~ use main created methods
        createBombLocationList()
        placeBombs()

    def placeZeros(self):
        '''Fills field array with number objects
        '''
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):

                if isinstance(self.__field[x][y],Bomb) == True:
                    continue

                self.__field[x][y] = Number(x,y)

    def addValue(self):
        '''Manipulates number objects around bombs.

        Iterates bombLocationList and calls increaseNumber() method of each surrounding Number objects'''

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
                  
    def getFieldSize(self):
        '''returns __fieldSize'''
        return self.__fieldSize
    
    def getBombLocationList(self):
        '''returns __bombLocationList'''
        return self.__bombLocationList
    
    def getBombCount(self):
        return self.__bombCount
    
    def getField(self):
        '''returns __field'''
        return self.__field
    
    
game = Gamefield()
plt.imshow(game.test)
plt.show()
