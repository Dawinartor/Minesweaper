from Tile import Tile
class Number(Tile):
    '''
    A class represent tile contains number.
    ...
    
    Inherit
    -------
    Tile class

    Attributes
    ----------
    number: int,defualt=0

    isLightUp: boolen
        defines if tile is showing
    
    '''
    def __init__(self, x, y,number = 0):
        self.__number = number
        self.__isLightUp = False
        
        super().__init__(x, y)

    def getNumber(self):
        '''returns __number'''
        return self.__number

    def increaseNumber(self):
        '''adds one to __number'''
        self.__number += 1
   
    def getisLightUp(self):
        '''returns __isLightUp'''
        return self.__isLightUp
    
    def changeisLightUp(self):
        '''changes current state of __isLightUp'''
        self.__isLightUp = not self.__isLightUp