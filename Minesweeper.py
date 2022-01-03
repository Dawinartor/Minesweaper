import numpy as np
import random
from collections import Counter

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

            
    def placeBombs(self):
        '''Create random generated list of tuples and place out of them Bombs in filed'''

        #TODO: - check lists for duplications
        #TODO:  -> if duplication found: replace duplication by create new number which is not in list
        
        #~ create random int generator
        def generateRandomInt():
            randi = random.randint(0, 15) # 16 in total
            return randi
        
        #~ create tuple with using random int generator
        def createTuple():
            # generate x and y random integers
            x = generateRandomInt()
            y = generateRandomInt()
            bombCoordinates = (x, y)
            return bombCoordinates
        
        #~ assign bomb to locationList
        def createBombLocations():
            for bomb in range(0, ):
                newBombLocation = createTuple()
                self.__bombLocationList.append(newBombLocation)
                
        #~ check bombLocationList for duplicated tuples
        def removeDuplications():
            for tile in self.__bombLocationList:
                pass
                
        #Counter()
        #set() # create a new set
        
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
        createBombLocations()
        removeDuplications()
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
    

game = Gamefield()
