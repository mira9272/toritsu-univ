#%%

import numpy

class EstimateSLF:

    def __init__(self, estparam, N1, N2):
        self.vector = estparam
        self.rowsize = N1
        self.colsize = N2

    def vector2matrix(self):

        slf_matrix = numpy.zeros((self.rowsize, self.colsize))

        for i in range(self.rowsize):
            for j in range(self.colsize):

                k = i + (j - 1) * self.rowsize
                slf_matrix[i-1, j-1] = self.vector[k-1, 0]

        return slf_matrix
