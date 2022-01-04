from Tile import Tile
class Bomb(Tile):
    '''
    A class represent tile contains number.
    ...
    
    Inherit
    -------
    Tile class
    '''
    def __init__(self, x, y):
        super().__init__(x, y)
        
    # this is for testing purpose
    def getNumber(self):
        return