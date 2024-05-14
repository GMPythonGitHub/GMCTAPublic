## gm_class_geom_a_vector.py: coded by Kinya MIURA 231107
# ---------------------------------------------------------
print("*** (GMVector) class for vector ***")
# ---------------------------------------------------------
print("### --- section_module: (GMVector) importing items from module --- ###")
from numpy import (
    deg2rad as d2r, rad2deg as r2d, cos, sin, tan, arctan2,
    ndarray, array, inner, outer, cross )
from numpy.linalg import norm
import copy

# ---------------------------------------------------------
print("### --- section_function: (GMVector) defining global functions --- ###")
def gmcos(th: float, deg: bool = False) -> float:
    return cos(d2r(th)) if deg else cos(th)
def gmsin(th: float, deg: bool = False) -> float:
    return sin(d2r(th)) if deg else sin(th)
def gmtan(th: float, deg: bool = False) -> float:
    return tan(d2r(th)) if deg else tan(th)
def gmatan2(yy: float, xx: float, deg=False) -> float:
    return r2d(arctan2(yy, xx)) if deg else arctan2(yy, xx)

# =========================================================
print("### --- section_class: (GMVector) describing class --- ###")
class GMVector():
    ## --- section_ca: (GMVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True ):
        self.__xxyy, self.__unit = array([0.,0.]), 1.
        self.set_vector(xxyy, rrth, unit=unit, cnv=cnv, deg=deg)
    ## --- section_cb: (GMVector) setting and getting functions --- ##
    ## setting functions
    def set_vector(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True ) -> None:
        if unit is not None: self.__unit = unit
        if rrth is not None:
            self.set_rrth(rrth, cnv=cnv, deg=deg)
        elif xxyy is not None:
            self.set_xxyy(xxyy, cnv=cnv)
    def set_xxyy(self, xxyy: tuple, cnv: bool = True) -> None:
        self.__xxyy = array(xxyy) * self.__unit if cnv else array(xxyy)
    def set_rrth(self, rrth: tuple, cnv: bool = True, deg: bool = True) -> None:
        rr, th = rrth
        if cnv: rr *= self.__unit
        self.__xxyy = rr * array(
            (gmcos(th,deg=deg), gmsin(th,deg=deg)) )
    ## getting functions
    def unit(self) -> float:
        return self.__unit
    def xxyy(self, cnv: bool = True) -> ndarray:
        if cnv: return self.__xxyy / self.__unit
        else: return self.__xxyy
    def rrth(self, cnv: bool = True, deg: bool = True) -> ndarray:
        rr = norm(self.__xxyy) / self.__unit if cnv else norm(self.__xxyy)
        th = gmatan2(self.__xxyy[1], self.__xxyy[0], deg=deg)
        return array((rr, th))
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: (GMVector) string function for print() --- ##
    def __str__(self) -> str:
        xxyy = self.xxyy(cnv=True); rrth = self.rrth(cnv=True, deg=True)
        return (
            f'xxyy = {xxyy} : rrth = {rrth} : unit = {self.__unit:g}' )
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMVector ::\n  ' + self.__str__()
    ## --- section_cd: (GMVector) functions for properties --- ##
    def leng(self, cnv: bool = False) -> float:
        val = norm(self.__xxyy)
        return val / self.__unit if cnv else val
    def dirc(self, deg: bool = False) -> float:
        return gmatan2(self.__xxyy[1], self.__xxyy[0], deg=deg)
    def unitvect(self) -> tuple:
        return self.__xxyy / norm(self.__xxyy)
    ## --- section_ce: (GMVector) functions for analyzing vectors --- ##
    def inner_vect(self, vect: object, cnv: bool = False) -> ndarray:  # inner product
        return inner(self.xxyy(cnv), vect.xxyy(cnv))
    def outer_vect(self, vect: object, cnv: bool = False) -> ndarray:  # outer product
        return outer(self.xxyy(cnv), vect.xxyy(cnv))
    def cross_vect(self, vect: object, cnv: bool = False) -> ndarray:  # cross product
        return cross(self.xxyy(cnv), vect.xxyy(cnv))
    ## --- section_cf: (GMVector) functions for vector arithmetics --- ##
    def conv(self, vect) -> object:
        if isinstance(vect, (int, float, complex)): return vect
        elif isinstance(vect, (tuple, list, ndarray)): return array(vect)
        elif isinstance(vect, GMVector): return vect.xxyy()
        else: return None
    def add(self, vct: object) -> None: self.__xxyy = self.__xxyy + self.conv(vct)
    def sub(self, vct: object) -> None: self.__xxyy = self.__xxyy - self.conv(vct)
    def rsub(self, vct: object) -> None: self.__xxyy = self.conv(vct) - self.__xxyy
    def mul(self, vct: object) -> None: self.__xxyy = self.__xxyy * self.conv(vct)
    def div(self, vct: object) -> None: self.__xxyy = self.__xxyy / self.conv(vct)
    def rdiv(self, vct: object) -> None: self.__xxyy = self.conv(vct) / self.__xxyy
    ## --- section_cg: functions for vector operator --- ##
    def __pos__(self): return GMVector(xxyy=+self.__xxyy)
    def __neg__(self): return GMVector(xxyy=-self.__xxyy)
    def __add__(self, vct): return GMVector(xxyy=self.__xxyy+self.conv(vct))
    def __radd__(self, vct): return GMVector(xxyy=self.conv(vct)+self.__xxyy)
    def __sub__(self, vct): return GMVector(xxyy=self.__xxyy-self.conv(vct))
    def __rsub__(self, vct): return GMVector(xxyy=self.conv(vct)-self.__xxyy)
    def __mul__(self, vct): return GMVector(xxyy=self.__xxyy*self.conv(vct))
    def __rmul__(self, vct): return GMVector(xxyy=self.conv(vct)*self.__xxyy)
    def __truediv__(self, vct): return GMVector(xxyy=self.__xxyy/self.conv(vct))
    def __rtruediv__(self, vct): return GMVector(xxyy=self.conv(vct)/self.__xxyy)
    # cumulative assignment operaters
    def __iadd__(self, vct): self.__xxyy = self.__xxyy+self.conv(vct); return self
    def __isub__(self, vct): self.__xxyy = self.__xxyy-self.conv(vct); return self
    def __imul__(self, vct): self.__xxyy = self.__xxyy*self.conv(vct); return self
    def __itruediv__(self, vct): self.__xxyy = self.__xxyy/self.conv(vct); return self

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMVector) main process --- ###")
    print()
    ## --- section_ma: (GMVector) creating class instances --- ##
    vecta = GMVector(xxyy=(1.,0.), unit=1.); print(vecta.classprop('vecta -> '))
    vectb = GMVector(xxyy=(0.,1.), unit=1.); print(vectb.classprop('vectb -> '))
    print()
    ## --- section_mb: (GMVector) calculating vector properties --- ##
    print(f'{vecta.leng() = }')
    print(f'{vecta.dirc() = }')
    print(f'{vecta.unitvect() = }')
    print()
    ## --- section_mc: (GMVector) calculating vector products --- ##
    print(f'{vecta.inner_vect(vectb) = }')
    print(f'{vecta.outer_vect(vectb) = }')
    print(f'{vecta.cross_vect(vectb) = }')
    print()
    ## --- section_md: (GMVector) calculating vector arithmetics --- ##
    vecta.add((1.,1.)); print(vecta.classprop('vecta -> '))
    vectb.add((1.,1.)); print(vectb.classprop('vectb -> '))
    vectc = vecta + vectb; print('vecta + vectb = ', vectc)
    vectc = vecta - vectb; print('vecta - vectb = ', vectc)
    vectc = vecta * vectb; print('vecta * vectb = ', vectc)
    vectc = vecta / vectb; print('vecta / vectb = ', vectc)

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_function: (GMVector) defining global functions --- ###
    ### --- section_class: (GMVector) describing class --- ###
    ### --- section_main: (GMVector) main process --- ###

    vecta -> :: GMVector ::
      xxyy = [1. 0.] : rrth = [1. 0.] : unit = 1
    vectb -> :: GMVector ::
      xxyy = [0. 1.] : rrth = [ 1. 90.] : unit = 1
    vecta.leng() = 1.0
    vecta.dirc() = 0.0
    vecta.unitvect() = array([1., 0.])
    vecta.inner2v(vectb) = 0.0
    vecta.outer2v(vectb) = array([[0., 1.], [0., 0.]])
    vecta.cross2v(vectb) = array(1.)

    vecta -> :: GMVector ::
      xxyy = [2. 1.] : rrth = [ 2.23606798 26.56505118] : unit = 1
    vectb -> :: GMVector ::
      xxyy = [1. 2.] : rrth = [ 2.23606798 63.43494882] : unit = 1
    vecta + vectb =  xxyy = [3. 3.] : rrth = [ 4.24264069 45.        ] : unit = 1
    vecta - vectb =  xxyy = [ 1. -1.] : rrth = [  1.41421356 -45.        ] : unit = 1
    vecta * vectb =  xxyy = [2. 2.] : rrth = [ 2.82842712 45.        ] : unit = 1
    vecta / vectb =  xxyy = [2.  0.5] : rrth = [ 2.06155281 14.03624347] : unit = 1
    '''
