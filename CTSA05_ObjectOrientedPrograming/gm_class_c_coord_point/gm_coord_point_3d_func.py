# gm_coord_point_3d_func.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point movement in 3d with function ***')
# ---------------------------------------------------------
## --- importing items from module ---
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- function ---
def shift(xx, yy, zz, ssx, ssy, ssz) -> tuple:  # shifting point
    xx += ssx; yy += ssy; zz += ssz
    print(
        f'ssx = {ssx:g}, ssy = {ssy:g}, ssz = {ssz:g} >> '
        f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
    return xx, yy, zz
def scale(xx, yy, zz, ccx, ccy, ccz) -> tuple:  # scaling point
    xx *= ccx; yy *= ccy; zz *= ccz
    print(
        f'ccx = {ccx:g}, ccy = {ccy:g}, ccz = {ccz:g} >> '
        f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
    return xx, yy, zz
def revolvex(xx, yy, zz, psx) -> tuple:  # revolving point around x-axis
    yy, zz = yy * cos(psx) - zz * sin(psx), yy * sin(psx) + zz * cos(psx)
    print(f'psx = {r2d(psx):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
    return xx, yy, zz
def revolvey(xx, yy, zz, psy) -> tuple:  # revolving point around y-axis
    zz, xx = zz * cos(psy) - xx * sin(psy), zz * sin(psy) + xx * cos(psy)
    print(f'psy = {r2d(psy):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
    return xx, yy, zz
def revolvez(xx, yy, zz, psz) -> tuple:  # revolving point around z-axis
    xx, yy = xx * cos(psz) - yy * sin(psz), xx * sin(psz) + yy * cos(psz)
    print(f'psz = {r2d(psz):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
    return xx, yy, zz

# =========================================================
## --- main process ---
xx, yy, zz = 3, 4, 5  # setting point
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5
xx, yy, zz = shift(xx, yy, zz, ssx=2, ssy=1, ssz=0)  # shifting point
# ssx = 2, ssy = 1, ssz = 0 >> xx = 5, yy = 5, zz = 5
xx, yy, zz = scale(xx, yy, zz, ccx=2, ccy=3, ccz=1)  # scaling point
# ccx = 2, ccy = 3, ccz = 3 >> xx = 10, yy = 15, zz = 5
xx, yy, zz = revolvex(xx, yy, zz, psx=d2r(90))  # revolving point around y-axis
# psx = 90 >> xx = 10, yy = -5, zz = 15
xx, yy, zz = revolvey(xx, yy, zz, psy=d2r(90))  # revolving point around y-axis
# psy = 90 >> xx = 15, yy = -5, zz = -10
xx, yy, zz = revolvez(xx, yy, zz, psz=d2r(90))  # revolving point around z-axis
# psz = 90 >> xx = 5, yy = 15, zz = -10
