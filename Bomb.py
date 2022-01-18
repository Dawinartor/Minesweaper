'''
    File name: Bomb.py 
    Author: Mehmet Şahin Üçeş & David Melamed
    Mehmet's GitHub: https://github.com/memo1918 
    David's GitHub: https://github.com/Dawinartor
    Date created: 4/01/2022
    Date last modified: 18/01/2022
    Python Version: 3.8.10
'''

from Tile import Tile
class Bomb(Tile):
    '''
    A class represent tile contains number.
    ...
    
    Inherit
    -------
    Tile class
    '''
    def __init__(self, x, y,index):
        super().__init__(x, y,index)