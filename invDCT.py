#%%

import numpy as np
import math

class InvDCT:

    def __init__(self, Nx, Ny):
        self.Nx = Nx
        self.Ny = Ny
        self.Nz = 1
        self.Nt = 1

    def InvDCTmatrix(self):

        N = self.Nx * self.Ny * self.Nz * self.Nt

        F_matrix = np.zeros((N, N))

        for nx in range(1, self.Nx + 1):
            for ny in range(1, self.Ny + 1):
                for nz in range(1, self.Nz + 1):
                    for nt in range(1, self.Nt + 1):

                        for kx in range(1, self.Nx + 1):
                            for ky in range(1, self.Ny + 1):
                                for kz in range(1, self.Nz + 1):
                                    for kt in range(1, self.Nt + 1):

                                        k = (kx - 1) * self.Ny * self.Nz * self.Nt + \
                                            (ky - 1) * self.Nz * self.Nt + \
                                            (kz - 1) * self.Nt + kt

                                        n = (nx - 1) * self.Ny * self.Nz * self.Nt + \
                                            (ny - 1) * self.Nz * self.Nt + \
                                            (nz - 1) * self.Nt + nt

                                        a1 = 1 / math.sqrt(self.Nx) if kx == 1 else math.sqrt(2 / self.Nx)

                                        a2 = 1 / math.sqrt(self.Ny) if ky == 1 else math.sqrt(2 / self.Ny)
                                            
                                        a3 = 1 / math.sqrt(self.Nz) if kz == 1 else math.sqrt(2 / self.Nz)

                                        a4 = 1 / math.sqrt(self.Nt) if kt == 1 else math.sqrt(2 / self.Nt)

                                        
                                        F_matrix[n-1, k-1] = a1 * a2 * a3 * a4 *\
                                                math.cos(math.pi * (2 * nx - 1) * (kx - 1) / (2 * self.Nx)) *\
                                                math.cos(math.pi * (2 * ny - 1) * (ky - 1) / (2 * self.Ny)) *\
                                                math.cos(math.pi * (2 * nz - 1) * (kz - 1) / (2 * self.Nz)) *\
                                                math.cos(math.pi * (2 * nt - 1) * (kt - 1) / (2 * self.Nt))
        return F_matrix
# %%
sample = InvDCT(20,20)
# %%
X = sample.InvDCTmatrix()
# %%
