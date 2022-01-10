class Tile:
    '''
    A class to represent a Tile.
    ...

    Attributes
    ----------
    __x : int
        x coordinate
    __y : int
        y coordinate
    width : int
        width of the tile
    height: int
        height of the tile

    Methods
    -------
    getLocation():
        returns __x and __y

    '''
    def __init__(self,x,y):
        '''"""
        Constructs all the necessary attributes for the tile object.

        Parameters
        ----------
        x: int
            x coordinate of the tile
        y: int
            y coordinate of the tile

        Attrubutes
        ----------
        surroundList: list
            contains all neigbhor tile's coordinates
        '''
        self.__x = x
        self.__y = y
        self.width = 16
        self.height = 16
        self.__surroundList = [(x+1,y),(x+1,y+1),(x,y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1)]
        self.__tileIndex = 0

    def getLocation(self):
        '''returns __x and __y'''
        return self.__x,self.__y

    def getsurroundList(self):
        '''returns __surroundList'''
        return self.__surroundList