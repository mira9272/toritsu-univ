#%%

import numpy as np
from numpy.lib.function_base import vectorize

class EstimateSLF:

    def __init__(self, estparam, N1, N2):
        self.vector = estparam
        self.rowsize = N1
        self.colsize = N2

    def vector2matrix(self):

        slf_matrix = np.zeros((self.rowsize, self.colsize))

        for i in range(1, self.rowsize + 1):
            for j in range(1, self.colsize + 1):

                k = i + (j - 1) * self.rowsize
                slf_matrix[i-1, j-1] = self.vector[k-1, 0]

        return slf_matrix

#%%
sample_vector = np.random.randn(100,1)
# %%
sampleclass = EstimateSLF(sample_vector,10,10)
# %%
