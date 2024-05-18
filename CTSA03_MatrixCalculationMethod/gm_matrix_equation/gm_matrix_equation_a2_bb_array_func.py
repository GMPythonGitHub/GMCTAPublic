# gm_matrix_equation_a2_bb_arrray_func: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array func: aa * xx = bb; xx is given ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import (array, dot)

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
xx = (1, 2, 3, 4)
bb = (None, None, None, None)

aa = array(aa1, dtype='float64')
xx = array(xx, dtype='float64')
bb = array(bb, dtype='float64')

# =========================================================
print('### --- section_solving --- ###')
bb = dot(aa, xx)
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array func: aa * xx = bb; xx is given ***
### --- section_module: importing items from module --- ###
### --- section_setting --- ###
### --- section_solving --- ###
aa = array([[1., 1., 1., 1.],
       [1., 2., 1., 1.],
       [1., 1., 3., 1.],
       [1., 1., 1., 4.]])
xx = array([1., 2., 3., 4.])
bb = array([10., 12., 16., 22.])
'''