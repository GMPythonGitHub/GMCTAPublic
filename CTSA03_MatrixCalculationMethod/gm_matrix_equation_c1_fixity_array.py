# gm_matrix_equation_c1_fixity_array: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array: aa * xx = bb; solve with fixity ***')
# ---------------------------------------------------------
## --- importing item from module ---
from numpy import (array, diag)
import copy

# =========================================================
print('### --- section_setting --- ###')
aa1 = ( (1, 1, 1, 1), (1, 2, 1, 1),
        (1, 1, 3, 1), (1, 1, 1, 4) )
bb1 = (None, 12, 16, None)
xx1 = (1, None, None, 4)
cnd_bb1 = (False, True, True, False)
cnd_xx1 = (True, False, False, True)
aa2 = ( (1, 1, 1, 1), (1, 1, 2, 1),
        (1, 3, 1, 1), (4, 1, 1, 1) )
bb2 = (None, 13, None, 13)
xx2 = (None, 2, None, 4)
cnd_bb2 = (False, True, False, True)
cnd_xx2 = (False, True, False, True)

aa = array(aa1, dtype='float64')
xx = array(xx1, dtype='float64')
bb = array(bb1, dtype='float64')
cnd_xx = cnd_xx1
cnd_bb = cnd_bb1

# =========================================================
print('### --- section_solving --- ###')
# setting partial matrix equation
bb_knwn, bb_uknwn = [], []
for i, cnd_bbi in enumerate(cnd_bb):
    if cnd_bbi: bb_knwn.append(i)
    else: bb_uknwn.append(i)
xx_knwn, xx_uknwn = [], []
for i, cnd_xxi in enumerate(cnd_xx):
    if cnd_xxi: xx_knwn.append(i)
    else: xx_uknwn.append(i)
aa_wk, bb_wk = [], []
for aai, bbi in zip(aa[bb_knwn, :], bb[bb_knwn]):
    aa_wk.append(aai[xx_uknwn])
    bb_wk.append(bbi - sum(aai[xx_knwn] * xx[xx_knwn]))
aa_wk, bb_wk = array(aa_wk), array(bb_wk)
rank_wk = len(bb_wk)
#  Gaussian elimination method
## forward elimination with pivoting
for i in range(rank_wk):
    for j in range(i+1,rank_wk):  # pivotting in line
        if abs(aa_wk[i,i]) < abs(aa_wk[j,i]):
            aa_wk[i,i:], aa_wk[j,i:] = aa_wk[j,i:], copy.copy(aa_wk[i,i:])
            bb_wk[i], bb_wk[j] = bb_wk[j], bb_wk[i]
    for j in range(i+1,rank_wk):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
## backward substitution
for i in range(rank_wk-1,-1,-1):
    for j in range(i-1,-1,-1):
        ratio = aa_wk[j,i] / aa_wk[i,i]
        aa_wk[j,i:] -= aa_wk[i,i:] * ratio
        bb_wk[j] -= bb_wk[i] * ratio
## normalization
xx_wk = bb_wk / diag(aa_wk)
## calculating vectors
jj = 0
for j, xx_uknwnj in enumerate(xx_uknwn):
    xx[xx_uknwnj] = xx_wk[j]
for i, aai in enumerate(aa):
    bb[i] = sum(aai * xx)
print(f'{aa = }\n{xx = }\n{bb = }\n{cnd_xx = }\n{cnd_bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array: aa * xx = bb; solve with fixity ***
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