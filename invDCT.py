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

        F_matrix = np.zeros(N, N)

        for nx in range(self.Nx):
            for ny in range(self.Ny):
                for nz in range(self.Nz):
                    for nt in range(self.Nt):

                        for kx in range(self.Nx):
                            for ky in range(self.Ny):
                                for kz in range(self.Nz):
                                    for kt in range(self.Nt):

                                        k = (kx - 1) * self.Ny * self.Nz * self.Nt + \
                                            (ky - 1) * self.Nz * self.Nt * \
                                            (kz - 1) * self.Nt * kt

                                        n = (nx - 1) * self.Ny * self.Nz * self.Nt + \
                                            (ny - 1) * self.Nz * self.Nt * \
                                            (nz - 1) * self.Nt * nt

                                        if kx == 1:
                                            a1 = 1 / math.sqrt(self.Nx)
                                        else:
                                            a1 = math.sqrt(2 / self.Nx)

                                        if ky == 1:
                                            a2 = 1 / math.sqrt(self.Ny)
                                        else:
                                            a2 = math.sqrt(2 / self.Ny)

                                        if kz == 1:
                                            a3 = 1 / math.sqrt(self.Nz)
                                        else:
                                            a3 = math.sqrt(2 / self.Nz)

                                        if kt == 1:
                                            a4 = 1 / math.sqrt(self.Nt)
                                        else:
                                            a4 = math.sqrt(2 / self.Nt)

                                        
                                        F_matrix[n-1, k-1] = a1 * a2 * a3 * a4 *\
                                            math.cos(math.pi * (2 * nx - 1) * (kx - 1) / (2 * self.Nx)) *\
                                            math.cos(math.pi * (2 * ny - 1) * (ky - 1) / (2 * self.Ny)) *\
                                            math.cos(math.pi * (2 * nz - 1) * (kz - 1) / (2 * self.Nz)) *\
                                            math.cos(math.pi * (2 * nt - 1) * (kt - 1) / (2 * self.Nt))

        return F_matrix