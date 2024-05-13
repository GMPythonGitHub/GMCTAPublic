# gm_coord_point_3d_class.py: coded by Kinya MIURA 231113
# --------------------------------------------------------
print('*** introducing class and class ***')
print('   *** coordinate point movement in 3d with class ***')
# ---------------------------------------------------------
## --- importing items from module --- ##
from numpy import (cos, sin, rad2deg as r2d, deg2rad as d2r)

# =========================================================
## --- class --- ##
class GMTrans:
    def __init__(self, xx = 0, yy = 0, zz = 0) -> None:
        self.xx, self.yy, self.zz = None, None, None
        # initializing xx, yy, zz: instance variables
        self.set_xxyyzz(xx, yy, zz)
    def set_xxyyzz(self, xx, yy, zz) -> None:  # setting point
        self.xx, self.yy, self.zz = xx, yy, zz
        self.xxyyzz()
    def xxyyzz(self) -> tuple:  # getting point
        print(f'xx = {self.xx:g}, yy = {self.yy:g}, zz = {self.zz:g}')
        return self.xx, self.yy, self.zz
    def shift(self, ssx, ssy, ssz) -> tuple:  # shifting point
        self.xx += ssx; self.yy += ssy; self.zz += ssz
        print(f'ssx = {ssx:g}, ssy = {ssy:g}, ssz = {ssz:g} >> ', end='')
        return self.xxyyzz()
    def scale(self, ccx, ccy, ccz) -> tuple:  # scaling point
        self.xx *= ccx; self.yy *= ccy; self.zz *= ccz
        print(f'ccx = {ccx:g}, ccy = {ccy:g}, ccz = {ccz:g} >> ', end='')
        return self.xxyyzz()
    def revolvex(self, psx) -> tuple:  # revolving point around x-axis
        self.yy, self.zz = (
            self.yy * cos(psx) - self.zz * sin(psx),
            self.yy * sin(psx) + self.zz * cos(psx) )
        print(f'psx = {r2d(psx):g} >> ', end = '')
        return self.xxyyzz()
    def revolvey(self, psy) -> tuple:  # revolving point around y-axis
        self.zz, self.xx = (
            self.zz * cos(psy) - self.xx * sin(psy),
            self.zz * sin(psy) + self.xx * cos(psy) )
        print(f'psy = {r2d(psy):g} >> ', end = '')
        return self.xxyyzz()
    def revolvez(self, psz) -> tuple:  # revolving point around z-axis
        self.xx, self.yy = (
            self.xx * cos(psz) - self.yy * sin(psz),
            self.xx * sin(psz) + self.yy * cos(psz) )
        print(f'psz = {r2d(psz):g} >> ', end = '')
        return self.xxyyzz()

# =========================================================
## --- main process --- ##
trans = GMTrans(xx=3, yy=4, zz=5)  # creating instance of GMTrans
# xx = 3, yy = 4, zz = 5
trans.shift(ssx=2, ssy=1, ssz=0)  # shifting point
# ssx = 2, ssy = 1, ssz = 0 >> xx = 5, yy = 5, zz = 5
trans.scale(ccx=2, ccy=3, ccz=1)  # scaling point
# ccx = 2, ccy = 3, ccz = 3 >> xx = 10, yy = 15, zz = 5
trans.revolvex(psx=d2r(90))  # revolving point around x-axis
# psx = 90 >> xx = 10, yy = -5, zz = 15
trans.revolvey(psy=d2r(90))  # revolving point around y-axis
# psy = 90 >> xx = 15, yy = -5, zz = -10
trans.revolvez(psz=d2r(90))  # revolving point around z-axis
# psz = 90 >> xx = 5, yy = 15, zz = -10
