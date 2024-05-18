# gm_matrix_equation_c2_fixity_array_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; solve with fixity ***')
# ---------------------------------------------------------
## --- importing item from module ---
from numpy import (array, dot, ix_, linalg, logical_not as loginot)

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
xx1 = (1, None, None, 4)
bb1 = (None, 12, 16, None)
cnd_xx1 = (True, False, False, True)
cnd_bb1 = (False, True, True, False)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
xx2 = (None, 2, None, 4)
bb2 = (None, 13, None, 13)
cnd_xx2 = (False, True, False, True)
cnd_bb2 = (False, True, False, True)

aa = array(aa1, dtype='float64')
xx = array(xx1, dtype='float64')
bb = array(bb1, dtype='float64')
cnd_xx = cnd_xx1
cnd_bb = cnd_bb1

# =========================================================
print('### --- section_solving --- ###')
#  setting partial matrix equation
aa_wk = aa[ix_(cnd_bb,loginot(cnd_xx))]
bb_wk = bb[ix_(cnd_bb)] - dot(aa[ix_(cnd_bb,cnd_xx)], xx[ix_(cnd_xx)])
#  Gaussian elimination method
xx_wk = linalg.solve(aa_wk, bb_wk)  # solving matrix equation
xx[ix_(loginot(cnd_xx))] = xx_wk
## calculating vectors
bb = dot(aa, xx)
print(f'{aa = }\n{xx = }\n{bb = }\n{cnd_xx = }\n{cnd_bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array func: aa * xx = bb; solve with fixity ***
### --- section_setting --- ###
### --- section_solving --- ###
aa = array([[1., 1., 1., 1.],
       [1., 2., 1., 1.],
       [1., 1., 3., 1.],
       [1., 1., 1., 4.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])
cnd_xx = (True, False, False, True)
cnd_bb = (False, True, True, False)
'''