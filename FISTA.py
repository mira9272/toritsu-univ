#%%

import math
import numpy as np
import numpy.linalg as LA

def FISTA(map_A, estimate_y, opt_lambda):

    # 初期値の設定
    N = map_A.shape[0]
    init_x = np.zeros((N, 1))
    init_w = np.zeros((N, 1))
    init_beta = 1

    # リプシッツ定数Lの計算
    L = np.linalg.eigvals(np.array(map_A).T * map_A)
    Lipschitz_L = np.linalg.norm(L, ord = 2) / opt_lambda

    # FISTAのアルゴリズム
    while 1 :
        
        # 変数の更新
        init_x = new_x
        init_w = new_w
        init_beta = new_beta


        output = init_x + np.array(map_A).T * (estimate_y - map_A * init_w) / Lipschitz_L * opt_lambda

        # 軟判定しきい値関数
        new_x = soft_threashold(output, 1 / Lipschitz_L)
        

        if np.linalg.norm(new_x - init_x) < 1E-6:
            
            return new_x


        new_beta = 1 / 2 (1 + math.sqrt(1 + 4(init_beta) ^ 2))

        new_w = new_x + (init_beta - 1) * (new_x - init_x) / new_beta

    # 軟判定しきい値関数
def soft_threashold(y, alpha):
    return np.sign(y) * np.maximum(np.abs(y) - alpha, 0.0)

#%%
import math
import numpy as np
import numpy.linalg as LA
# %%
