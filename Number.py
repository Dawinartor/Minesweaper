'''
    File name: Number.py 
    Author: Mehmet Şahin Üçeş & David Melamed
    Mehmet's GitHub: https://github.com/memo1918 
    David's GitHub: https://github.com/Dawinartor
    Date created: 4/01/2022
    Date last modified: 18/01/2022
    Python Version: 3.8.10
'''

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
    def __init__(self, x, y,index,number = 0):
        self.__number = number
        self.__isLightUp = False
        
        super().__init__(x, y,index)

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