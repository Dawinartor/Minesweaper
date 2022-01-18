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
    __field : numpy.ndarray
        empty numpy array with objects that represents field
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
    toJSON(): 
        Gets data from GameField and GameFiled.field and returns as a JSON formatted string
    getFieldSize():
        Returns size of field
    getBombLocationList():
        Returns list with bombs inside
    getBombCount():
        Returns total amount of bombs inside field
    getField():
        returns __field
    """
    def __init__(self):
        self.__field = np.empty((16,16), dtype=object)
        self.__fieldSize = self.__field.size
        self.fieldSizeX = np.size(self.__field, 0) # starts from 0
        self.fieldSizeY  = np.size(self.__field, 1)
        self.__bombLocationList = [] # define return of placeBombs (tuple list)
        self.__bombCount = 40 # based on 40 bombs for 256 Tiles 
        self.__openedTileCount = 0
        
        self.placeTiles()
        self.placeBombs()
        self.addValue()
    
    def placeBombs(self): #X
        '''Create random generated list of tuples and place out of them Bombs in filed'''
        
        def createBombLocationList(): #TODO: Explain what happens here
            '''Create'''
            rangeX = range(self.fieldSizeX)
            rangeY = range(self.fieldSizeY)
            GamefieldTotalSize = product(rangeX, rangeY, repeat=1)
            gamefieldList = list(GamefieldTotalSize)
            self.__bombLocationList = sample(gamefieldList, k=self.__bombCount)
            
                
        def placeBombs():
            '''Iterates through __bombLocationList and creates bomb objects at that coordinate
            '''
            for mockupBomb in self.__bombLocationList:
                #* define x & y coordinates
                x = mockupBomb[0]
                y = mockupBomb[1]

                index = y+((x)* self.fieldSizeY)
                self.__field[x][y] = Bomb(x, y,index) 
        
        #~ use main created methods
        createBombLocationList()
        placeBombs()

    def placeTiles(self): #X
        '''Fills field array with number objects
        '''
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):

                if isinstance(self.__field[x][y],Bomb) == True:
                    continue
                index = y+((x)* self.fieldSizeY)
                self.__field[x][y] = Number(x,y,index)

    def addValue(self): #X
        '''Manipulates number objects around bombs.

        Iterates bombLocationList and calls increaseNumber() method of each surrounding Number objects'''

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

    def isLightUpChanger(self,x,y): #X
        '''Checks and changes isLightup of a given tile.

        If the tile is not bomb it changes isLightUp and also If the tile is "blank" it calls blankOpener()'''
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
                              
    def blankOpener(self,x,y): #X
        '''Check the surrounding of the given tile for isLightUp and calls back isLightUpChanger()'''
        surroundList = self.__field[x][y].getsurroundList()
        for value in surroundList:
            if not (value[0]<0 or value[1]<0 or value[0]>15 or value[1]>15): #cheking if x or y value is outside the field
                try:
                    if self.__field[value[0]][value[1]].getisLightUp() == False:
                        self.isLightUpChanger(value[0],value[1])
                except:
                    pass

    def toJSON(self): #X
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
            'fieldSizeX':self.fieldSizeX,
            'fieldSizeY':self.fieldSizeY,
            'field': fieldList
            }
        
        return json.dumps(gfJson)

    def getFieldSize(self):
        '''returns __fieldSize'''
        return self.__fieldSize
    
    def getBombLocationList(self):
        '''returns __bombLocationList'''
        return self.__bombLocationList
    
    def getBombCount(self):
        '''return __bombCount'''
        return self.__bombCount
    
    def getField(self):
        '''returns __field'''
        return self.__field