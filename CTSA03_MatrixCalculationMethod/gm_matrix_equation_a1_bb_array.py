# gm_matrix_equation_a1_bb_arrray: coded by Kinya MIURA 231104
# ---------------------------------------------------------
print('\n*** Matrix Equation with array: aa * xx = bb; xx is given ***')
# ---------------------------------------------------------
print('### --- section_module: importing items from module --- ###')
from numpy import array

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
for i, aai in enumerate(aa):
    bb[i] = sum(aai * xx)
print(f'{aa = }\n{xx = }\n{bb = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** Matrix Equation with array: aa * xx = bb; xx is given ***
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

'''
## usege of list and ndarray
print('\n', '# --- list')
a，b = [0, 1, 2], [3, 4, 5]  # list
print(":: print(f'{a + 3 = }'); error")
print(f'{a * 3 = }')
print(f'{a + b = }')

print('\n', '# --- ndarray')
a, b = array([1, 2, 3]), array([4, 5, 6])  # ndarray
print(f'{a + 2 = }')
print(f'{a * 2 = }')
print(f'{a ** 2 = }')
print(f'{a + b = }')
print(f'{a + b = }')

a, b = array([1, 2, 3]), array([-2, 2, 4])  # ndarray
print(a + 2)
# [3 4 5]
print(a * 2)
# [2 4 6]
print(a ** 2)
# [1 4 9]
print(a + b)
# [5 7 9]
print(a * b)
# [ 4 10 18]
print(abs(b))
# [2 2 4]




'''