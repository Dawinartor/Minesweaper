'''
    File name: Gamefield.py #TODO: Rename the file to Gamefield
    Author: Mehmet Şahin Üçeş & David Melamed
    Mehmet's GitHub: https://github.com/memo1918 
    David's GitHub: https://github.com/Dawinartor
    Date created: 4/01/2022
    Date last modified: 18/01/2022
    Python Version: 3.8.10
'''

# required packages to use this package
import numpy as np
import json
from itertools import product
from random import sample
# self developed classes
from Number import Number
from Bomb import Bomb


class Gamefield:
    """
    The main class that represent the Gamefield
    ...

    Attributes
    ----------
    __field: numpy.ndarray
        empty numpy array with objects that represents field
    __fieldSize: int
        size of the field
    __fieldSizeX: int
        size of the array in x axis
    __fieldSizeY: int
        size of the array in y axis
    __bombLocationList : list
        contains locations of genereted bombs
    __bombCount: int
        amount of bomb in the field
    __openedTileCount: int
        amount of opened tiles

    Methods
    -------
    placeBombs(): 
        Places bomb objects into the field.
    placeTiles(): 
        Fills field array with number objects.
    addValue(): 
        Manipulates number objects around bombs.
    isLightUpChanger(x,y): 
        Checks and changes isLightup of a given tile
    blankOpener(x,y): 
        Check the surrounding of the given tile for isLightUp and calls back isLightUpChanger()
    toJSON(): str
        Gets data from GameField and GameFiled.field and returns as a JSON formatted string
    getFieldSize(): int
        Returns size of field
    getFieldSizeX(): int
        Return size of X-axe from field
    getFieldSizeY(): int
        Return size of Y-axe from field
    getBombLocationList(): list
        Returns list with bombs inside
    getBombCount(): int
        Returns total amount of bombs inside field
    getField(): numPy.array
        Returns the field
    """
    def __init__(self): #TODO: Check constructor docstring best-practice
        self.__field = np.empty((16,16), dtype=object)
        self.__fieldSize = self.__field.size
        self.__fieldSizeX = np.size(self.__field, 0) # starts from 0
        self.__fieldSizeY = np.size(self.__field, 1)
        self.__bombLocationList = [] # define return of placeBombs (tuple list)
        self.__bombCount = 40 # based on 40 bombs for 256 Tiles 
        self.__openedTileCount = 0
        
        self.placeTiles()
        self.placeBombs()
        self.addValue()
    
    def placeBombs(self):
        '''Adds Bomb objects in __field '''
        
        def createBombLocationList(): #TODO: Explain what happens here
            '''Creates unique tuples (int, int) and adds them into __bombLocationList'''
            rangeX = range(self.__fieldSizeX)
            rangeY = range(self.__fieldSizeY)
            GamefieldTotalSize = product(rangeX, rangeY, repeat=1)
            gamefieldList = list(GamefieldTotalSize)
            self.__bombLocationList = sample(gamefieldList, k=self.__bombCount)
            
                
        def placeBombs():
            '''Iterates through __bombLocationList and creates bomb objects based on containing tuples'''
            for mockupBomb in self.__bombLocationList:
                #* define x & y coordinates
                x = mockupBomb[0]
                y = mockupBomb[1]

                index = y+((x)* self.__fieldSizeY)
                self.__field[x][y] = Bomb(x, y,index) 
        
        createBombLocationList()
        placeBombs()

    def placeTiles(self):
        '''Adds Number objects in each empty space of __field'''
        for x in range(0,self.__fieldSizeX):
            for y in range(0,self.__fieldSizeY):

                if isinstance(self.__field[x][y],Bomb) == True:
                    continue
                index = y+((x)* self.__fieldSizeY) #FIX: What is going on here?
                self.__field[x][y] = Number(x,y,index)

    def addValue(self):
        '''Increases number attribute in each number object around bombs'''

        for location in self.__bombLocationList:
            x = location[0]
            y = location[1]
            surroundList = self.__field[x][y].getsurroundList()

            for value in surroundList:
                if not (value[0]<0 or value[1]<0 or value[0]>15 or value[1]>15): #cheking if x or y value is outside the field
                    try:
                        self.__field[value[0]][value[1]].increaseNumber()
                    except:
                        continue

    def isLightUpChanger(self,x,y):
        '''
        Checks if isLightup attribute and changes isLightup of a tile object.
  
        Parameters:
            x (int): Index of x-axe
            y (int): Index of y-axe
          
        Returns:
            - "Bomb" - If bomb object was lighted up during function process
            - "You Win" - If all number objects are lighted up
        '''
        x,y = int(x),int(y)
        tile = self.__field[x][y]
        
        if isinstance(tile,Bomb) == True:
            return "Bomb"
        elif tile.getisLightUp() == False:
            #checking and adding
            self.__openedTileCount += 1
            if tile.getNumber() == 0:
                tile.changeisLightUp()
                self.blankOpener(x,y) 
            else: 
                tile.changeisLightUp()

            if self.__openedTileCount == (self.__fieldSize - self.__bombCount):
                return "You Win"
                              
    def blankOpener(self,x,y):
        '''
        Checks each surrounding tile object for number attribute if its zero switch isLightUp to true
        
        Parameters:
            x (int): Index of x-axe
            y (int): Index of y-axe
            
        '''
        surroundList = self.__field[x][y].getsurroundList()
        for value in surroundList:
            if not (value[0]<0 or value[1]<0 or value[0]>15 or value[1]>15): #cheking if x or y value is outside the field
                try:
                    if self.__field[value[0]][value[1]].getisLightUp() == False:
                        self.isLightUpChanger(value[0],value[1])
                except:
                    pass

    def toJSON(self):
        '''Gets data from GameField and GameFiled.field and returns as a JSON formatted string'''
        gfJson = dict()
        # send islightup value
        fieldList = list()
        for row in self.__field:
            for value in row:
                tempDict = {}
                x,y = value.getLocation()
                className = type(value).__name__
                tempDict["x"], tempDict['y'] = x,y
                tempDict['index'] = value.getIndex()
                tempDict['className'] = className
                if className == 'Number':
                    tempDict['number'] = value.getNumber()
                    tempDict['isLightUp'] = value.getisLightUp()
                fieldList.append(tempDict)


        gfJson['Gamefield'] = {
            'fieldSize':self.__fieldSize,
            'fieldSizeX':self.__fieldSizeX,
            'fieldSizeY':self.__fieldSizeY,
            'field': fieldList
            }
        
        return json.dumps(gfJson)

    def getFieldSize(self):
        '''returns size of field'''
        return self.__fieldSize
    
    def getFieldSizeX(self):
        '''return size of X-axe from field'''
        return self.__fieldSizeX
    
    def getFieldSizeY(self):
        '''return size of Y-axe from field'''
        return self.__fieldSizeY
    
    def getBombLocationList(self):
        '''returns list with bombs inside'''
        return self.__bombLocationList
    
    def getBombCount(self):
        '''return total amount of bombs inside field'''
        return self.__bombCount
    
    def getField(self):
        '''returns the fiel'''
        return self.__field