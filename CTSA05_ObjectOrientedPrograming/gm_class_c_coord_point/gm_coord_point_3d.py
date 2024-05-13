# gm_coord_point_3d.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and function ***')
print('   *** coordinate point movement in 3d ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- main process --- ##
xx, yy, zz = 3, 4, 5  # setting point
print(f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}')
# xx = 3, yy = 4, zz = 5
ssx, ssy, ssz = 2, 1, 0  # shifting point
xx += ssx; yy += ssy; zz += ssz
print(
    f'ssx = {ssx:g}, ssy = {ssy:g}, ssz = {ssz:g} >> '
    f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
# ssx = 2, ssy = 1, ssz = 0 >> xx = 5, yy = 5, zz = 5

ccx, ccy, ccz = 2, 3, 1  # scaling point
xx *= ccx; yy *= ccy; zz *= ccz
print(
    f'ccx = {ccx:g}, ccy = {ccy:g}, ccz = {ccz:g} >> '
    f'xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
# ccx = 2, ccy = 3, ccz = 3 >> xx = 10, yy = 15, zz = 5

psx = d2r(90)  # revolving point around x-axis
yy, zz = yy * cos(psx) - zz * sin(psx), yy * sin(psx) + zz * cos(psx)
print(f'psx = {r2d(psx):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
# psx = 90 >> xx = 10, yy = -5, zz = 15
psy = d2r(90)  # revolving point around y-axis
zz, xx = zz * cos(psy) - xx * sin(psy), zz * sin(psy) + xx * cos(psy)
print(f'psy = {r2d(psy):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
# psy = 90 >> xx = 15, yy = -5, zz = -10
psz = d2r(90)  # revolving point around z-axis
xx, yy = xx * cos(psz) - yy * sin(psz), xx * sin(psz) + yy * cos(psz)
print(f'psz = {r2d(psz):g} >> xx = {xx:g}, yy = {yy:g}, zz = {zz:g}' )
# psz = 90 >> xx = 5, yy = 15, zz = -10
