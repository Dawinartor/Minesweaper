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