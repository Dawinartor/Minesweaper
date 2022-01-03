from matplotlib import pyplot as plt

self.test = np.zeros((16,16))
        for x in range(0,self.fieldSizeX):
            for y in range(0,self.fieldSizeY):
                self.test[x][y] = self.__field[x][y].getNumber()

plt.imshow(game.test, interpolation='nearest')
plt.show()