#%%

import numpy
import numpy as np
import matplotlib.pyplot as plt

class Channel:
    def __init__(self,x,N1,N2):
        self.estslf_ = x
        self.row_ = N1
        self.col_ = N2
        self.passloss_ = 2

    def drawSLF(self):

        slf_size = numpy.zeros((self.row_ + 1, self.col_ + 1))

        for i in range(self.row_):
            for j in range(self.col_):
                slf_size[i-1, j-1] = self.estslf_

        for k in range(self.row_ + 1):
            for l in range(self.col_ + 1):
                M1, M2 = np.meshgrid(k, l)

        plt.pcolormesh(M1, M2, slf_size, cmap='Glays')
        plt.gca().set_aspect('equal', adjustable = 'box')
        
        plt.title('estimated SLF')
        plt.xlabel('X', fontsize=18)
        plt.ylabel('Y', fontsize=18)

        plt.show()