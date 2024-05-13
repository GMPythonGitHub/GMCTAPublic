# gm_class_vector_d.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorD: operating vector ***')
print('   *** with vector calculation ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorD) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)
import copy

# ---------------------------------------------------------
print("### --- section_functions: (GMVectorD) defining global functions --- ###")
def gmsrsq(xx, yy): return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False):
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht

# =========================================================
print('### --- section_class: (GMVectorD) describing class --- ###')
class GMVectorD():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        self.__xxyy = array([1, 1])
        self.set_vect(xxyy=xxyy, rrth=rrth, deg=deg)
    ## --- section_cb: setting and getting functions --- ##
    ## setting functions
    def set_vect(self,
            xxyy: tuple = None, rrth: tuple = None, deg: bool = True) -> None:
        if xxyy is not None: self.__xxyy = array(xxyy)
        if rrth is not None:
            rr, th = rrth
            if deg: th = d2r(th)
            self.__xxyy = array([rr * cos(th), rr * sin(th)])
    ## getting functions
    def xxyy(self) -> ndarray:
        return self.__xxyy
    def rrth(self, deg: bool = False) -> ndarray:
        xx, yy = self.__xxyy
        return array([gmsrsq(xx,yy), gmatan2(yy,xx,deg=deg)])
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorD): xx = {xx:g}, yy = {yy:g}, '
            f'rr = {rr:g}, th(deg) = {th:g}' )
    ## --- section_cd: functions for properties --- ##
    def leng(self) -> float:
        return self.rrth()[0]
    def dirc(self, deg: bool = False) -> float:
        return self.rrth(deg=deg)[1]
    def unitvect(self) -> ndarray:
        return self.__xxyy / self.leng()
    ## --- section_ce: functions for vector analysis --- ##
    def inner(self, vect: object) -> float:
        return inner(self.__xxyy, vect.xxyy())
    def outer(self, vect: object) -> ndarray:
        return outer(self.__xxyy, vect.xxyy())
    def cross(self, vect: object) -> float:
        return float(cross(self.__xxyy, vect.xxyy()))
    ## --- section_cf: functions for vector operation --- ##
    def conv(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVectorD): return vect.xxyy()
        else: return None
    def add(self, vct: object) -> None: self.__xxyy = self.__xxyy + self.conv(vct)
    def sub(self, vct: object) -> None: self.__xxyy = self.__xxyy - self.conv(vct)
    def rsub(self, vct: object) -> None: self.__xxyy = self.conv(vct) - self.__xxyy
    def mul(self, vct: object) -> None: self.__xxyy = self.__xxyy * self.conv(vct)
    def div(self, vct: object) -> None: self.__xxyy = self.__xxyy / self.conv(vct)
    def rdiv(self, vct: object) -> None: self.__xxyy = self.conv(vct) / self.__xxyy
    ## --- section_cg: functions for vector operator --- ##
    def __pos__(self): return GMVectorD(xxyy=+self.__xxyy)
    def __neg__(self): return GMVectorD(xxyy=-self.__xxyy)
    def __add__(self, vct): return GMVectorD(xxyy=self.__xxyy+self.conv(vct))
    def __radd__(self, vct): return GMVectorD(xxyy=self.conv(vct)+self.__xxyy)
    def __sub__(self, vct): return GMVectorD(xxyy=self.__xxyy-self.conv(vct))
    def __rsub__(self, vct): return GMVectorD(xxyy=self.conv(vct)-self.__xxyy)
    def __mul__(self, vct): return GMVectorD(xxyy=self.__xxyy*self.conv(vct))
    def __rmul__(self, vct): return GMVectorD(xxyy=self.conv(vct)*self.__xxyy)
    def __truediv__(self, vct): return GMVectorD(xxyy=self.__xxyy/self.conv(vct))
    def __rtruediv__(self, vct): return GMVectorD(xxyy=self.conv(vct)/self.__xxyy)
    # cumulative assignment operaters
    def __iadd__(self, vct): self.__xxyy = self.__xxyy+self.conv(vct); return self
    def __isub__(self, vct): self.__xxyy = self.__xxyy-self.conv(vct); return self
    def __imul__(self, vct): self.__xxyy = self.__xxyy*self.conv(vct); return self
    def __itruediv__(self, vct): self.__xxyy = self.__xxyy/self.conv(vct); return self

# =========================================================
print('### --- section_main: (GMVectorD) main process --- ###')
## --- section_ma: functions for vector calculations --- ##
vecta = GMVectorD(xxyy=(5,3))  # creating instance
print('vecta:', vecta)
vectb = GMVectorD(xxyy=(2,1))  # creating instance
print('vectb:', vectb)

print('\n-- functions')
print('  ------  : vect = vecta.copy()')
vect = vecta.copy(); vect.add(2); print('vect.add(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.add((4,4)); print('vect.add((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.add(vectb); print('vect.add(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.sub(2); print('vect.sub(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.sub((4,4)); print('vect.sub((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.sub(vectb); print('vect.sub(vectb2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub(2); print('vect.rsub(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub((4,4)); print('vect.rsub((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rsub(vectb); print('vect.rsub(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.mul(2); print('vect.mul(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.mul((4,4)); print('vect.mul((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.mul(vectb); print('vect.mul(vectb2): ', f'{vect.xxyy() = }')
print()
vect = vecta.copy(); vect.div(2); print('vect.div(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.div((4,4)); print('vect.div((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.div(vectb); print('vect.div(vectb2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv(2); print('vect.rdiv(2): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv((4,4)); print('vect.rdiv((4,4)): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect.rdiv(vectb); print('vect.rdiv(vectb2): ', f'{vect.xxyy() = }')

## --- section_mb: operators for vector calculation --- ##
print('\n-- operators')
vect = vecta + 2; print('vect = vecta + 2: ', f'{vect.xxyy() = }')
vect = vecta + (4,4); print('vect = vecta + (4,4): ', f'{vect.xxyy() = }')
vect = vecta + vectb; print('vect = vecta + vectb: ', f'{vect.xxyy() = }')
vect = - vecta + 2; print('vect = - vecta + 2: ', f'{vect.xxyy() = }')
vect = - vecta + (4,4); print('vect = - vecta + (4,4): ', f'{vect.xxyy() = }')
vect = - vecta + vectb; print('vect = - vecta + vectb: ', f'{vect.xxyy() = }')
vect = 2 + vecta; print('vect = 2 + vecta: ', f'{vect.xxyy() = }')
vect = (4,4) + vecta; print('vect = (4,4) + vecta: ', f'{vect.xxyy() = }')
vect = vectb + vecta; print('vect = vectb + vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta - 2; print('vect = vecta - 2: ', f'{vect.xxyy() = }')
vect = vecta - (4,4); print('vect = vecta - (4,4): ', f'{vect.xxyy() = }')
vect = vecta - vectb; print('vect = vecta - vectb: ', f'{vect.xxyy() = }')
vect = - vecta - 2; print('vect = - vecta - 2: ', f'{vect.xxyy() = }')
vect = - vecta - (4,4); print('vect = - vecta - (4,4): ', f'{vect.xxyy() = }')
vect = - vecta - vectb; print('vect = - vecta - vectb: ', f'{vect.xxyy() = }')
vect = 2 - vecta; print('vect = 2 - vecta: ', f'{vect.xxyy() = }')
vect = (4,4) - vecta; print('vect = (4,4) - vecta: ', f'{vect.xxyy() = }')
vect = vectb - vecta; print('vect = vectb - vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta * 2; print('vect = vecta * 2: ', f'{vect.xxyy() = }')
vect = vecta * (4,4); print('vect = vecta * (4,4): ', f'{vect.xxyy() = }')
vect = vecta * vectb; print('vect = vecta * vectb: ', f'{vect.xxyy() = }')
vect = 2 * vecta; print('vect = 2 * vecta: ', f'{vect.xxyy() = }')
vect = (4,4) * vecta; print('vect = (4,4) * vecta: ', f'{vect.xxyy() = }')
vect = vectb * vecta; print('vect = vectb * vecta: ', f'{vect.xxyy() = }')
print()
vect = vecta / 2; print('vect = vecta / 2: ', f'{vect.xxyy() = }')
vect = vecta / (4,4); print('vect = vecta / (4,4): ', f'{vect.xxyy() = }')
vect = vecta / vectb; print('vect = vecta / vectb: ', f'{vect.xxyy() = }')
vect = 2 / vecta; print('vect = 2 / vecta: ', f'{vect.xxyy() = }')
vect = (4,4) / vecta; print('vect = (4,4) / vecta: ', f'{vect.xxyy() = }')
vect = vectb / vecta; print('vect = vectb / vecta: ', f'{vect.xxyy() = }')

print('\n-- cumulative assigment operator')
print('  ------  : vect = vecta.copy()')
vect = vecta.copy(); vect += 2; print('vect += 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect += (4,4); print('vect += (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect += vectb; print('vect += vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= 2; print('vect -= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= (4,4); print('vect -= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect -= vectb; print('vect -= vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= 2; print('vect *= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= (4,4); print('vect *= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect *= vectb; print('vect *= vectb: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= 2; print('vect /= 2: ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= (4,4); print('vect /= (4,4): ', f'{vect.xxyy() = }')
vect = vecta.copy(); vect /= vectb; print('vect /= vectb: ', f'{vect.xxyy() = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorD: operating vector ***
   *** with vector calculation ***
### --- section_module: (GMVectorD) importing items from module --- ###
### --- section_class: (GMVectorD) describing class --- ###
### --- section_main: (GMVectorD) main process --- ###
vecta: (GMVectorD): xx = 5, yy = 3, rr = 5.83095, th(deg) = 30.9638
vectb: (GMVectorD): xx = 2, yy = 1, rr = 2.23607, th(deg) = 26.5651

-- functions
  ------  : vect = vecta.copy()
vect.add(2):  vect.xxyy() = array([7, 5])
vect.add((4,4)):  vect.xxyy() = array([9, 7])
vect.add(vectb2):  vect.xxyy() = array([7, 4])

vect.sub(2):  vect.xxyy() = array([3, 1])
vect.sub((4,4)):  vect.xxyy() = array([ 1, -1])
vect.sub(vectb2):  vect.xxyy() = array([3, 2])
vect.rsub(2):  vect.xxyy() = array([-3, -1])
vect.rsub((4,4)):  vect.xxyy() = array([-1,  1])
vect.rsub(vectb2):  vect.xxyy() = array([-3, -2])

vect.mul(2):  vect.xxyy() = array([10,  6])
vect.mul((4,4)):  vect.xxyy() = array([20, 12])
vect.mul(vectb2):  vect.xxyy() = array([10,  3])

vect.div(2):  vect.xxyy() = array([2.5, 1.5])
vect.div((4,4)):  vect.xxyy() = array([1.25, 0.75])
vect.div(vectb2):  vect.xxyy() = array([2.5, 3. ])
vect.rdiv(2):  vect.xxyy() = array([0.4       , 0.66666667])
vect.rdiv((4,4)):  vect.xxyy() = array([0.8       , 1.33333333])
vect.rdiv(vectb2):  vect.xxyy() = array([0.4       , 0.33333333])

-- operators
vect = vecta + 2:  vect.xxyy() = array([7, 5])
vect = vecta + (4,4):  vect.xxyy() = array([9, 7])
vect = vecta + vectb:  vect.xxyy() = array([7, 4])
vect = - vecta + 2:  vect.xxyy() = array([-3, -1])
vect = - vecta + (4,4):  vect.xxyy() = array([-1,  1])
vect = - vecta + vectb:  vect.xxyy() = array([-3, -2])
vect = 2 + vecta:  vect.xxyy() = array([7, 5])
vect = (4,4) + vecta:  vect.xxyy() = array([9, 7])
vect = vectb + vecta:  vect.xxyy() = array([7, 4])

vect = vecta - 2:  vect.xxyy() = array([3, 1])
vect = vecta - (4,4):  vect.xxyy() = array([ 1, -1])
vect = vecta - vectb:  vect.xxyy() = array([3, 2])
vect = - vecta - 2:  vect.xxyy() = array([-7, -5])
vect = - vecta - (4,4):  vect.xxyy() = array([-9, -7])
vect = - vecta - vectb:  vect.xxyy() = array([-7, -4])
vect = 2 - vecta:  vect.xxyy() = array([-3, -1])
vect = (4,4) - vecta:  vect.xxyy() = array([-1,  1])
vect = vectb - vecta:  vect.xxyy() = array([-3, -2])

vect = vecta * 2:  vect.xxyy() = array([10,  6])
vect = vecta * (4,4):  vect.xxyy() = array([20, 12])
vect = vecta * vectb:  vect.xxyy() = array([10,  3])
vect = 2 * vecta:  vect.xxyy() = array([10,  6])
vect = (4,4) * vecta:  vect.xxyy() = array([20, 12])
vect = vectb * vecta:  vect.xxyy() = array([10,  3])

vect = vecta / 2:  vect.xxyy() = array([2.5, 1.5])
vect = vecta / (4,4):  vect.xxyy() = array([1.25, 0.75])
vect = vecta / vectb:  vect.xxyy() = array([2.5, 3. ])
vect = 2 / vecta:  vect.xxyy() = array([0.4       , 0.66666667])
vect = (4,4) / vecta:  vect.xxyy() = array([0.8       , 1.33333333])
vect = vectb / vecta:  vect.xxyy() = array([0.4       , 0.33333333])

-- cumulative assigment operator
  ------  : vect = vecta.copy()
vect += 2:  vect.xxyy() = array([7, 5])
vect += (4,4):  vect.xxyy() = array([9, 7])
vect += vectb:  vect.xxyy() = array([7, 4])
vect -= 2:  vect.xxyy() = array([3, 1])
vect -= (4,4):  vect.xxyy() = array([ 1, -1])
vect -= vectb:  vect.xxyy() = array([3, 2])
vect *= 2:  vect.xxyy() = array([10,  6])
vect *= (4,4):  vect.xxyy() = array([20, 12])
vect *= vectb:  vect.xxyy() = array([10,  3])
vect /= 2:  vect.xxyy() = array([2.5, 1.5])
vect /= (4,4):  vect.xxyy() = array([1.25, 0.75])
vect /= vectb:  vect.xxyy() = array([2.5, 3. ])
'''
