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
    
    '''
    def __init__(self, x, y,number = 0):
        self.__number = number
        super().__init__(x, y)

    def getNumber(self):
        '''returns __number'''
        return self.__number

    def increaseNumber(self):
        '''adds one to __number'''
        self.__number += 1