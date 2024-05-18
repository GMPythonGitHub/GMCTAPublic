# gm_class_vector_c.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorC: operating vector ***')
print('   *** with ndarray from numpy ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorC) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr,
    cos, sin, arctan2, rad2deg as r2d, deg2rad as d2r)
from numpy import(ndarray, array, inner, outer, cross)

# ---------------------------------------------------------
print("### --- section_function: (GMVectorC) defining global functions --- ###")
def gmsrsq(xx, yy): return sr(sq(xx)+sq(yy))
def gmatan2(yy, xx, deg=False):
    tht = arctan2(yy,xx); return r2d(tht) if deg else tht

# =========================================================
print('### --- section_class: (GMVectorC) describing class --- ###')
class GMVectorC():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1, 1), rrth: tuple = None, deg: bool = True) -> None:
        self.__xxyy = None
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
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        xx, yy = self.__xxyy; rr, th = self.rrth(True)
        return (
            f'(GMVectorC): xx = {xx:g}, yy = {yy:g}, '
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

# =========================================================
print('### --- section_main: (GMVectorC) main process --- ###')
## --- section_ma: creating instances --- ##
vecta = GMVectorC(xxyy=(3,4))  # creating instance
print('vecta:', vecta)
vectb = GMVectorC(xxyy=(-4,3))  # creating instance
print('vectb:', vectb)
## --- section_mb: calculating vector products --- ##
print(f'{vecta.inner(vectb) = }')
print(f'{vecta.outer(vectb) = }')
print(f'{vecta.cross(vectb) = }')
print(f'{vectb.inner(vecta) = }')
print(f'{vectb.outer(vecta) = }')
print(f'{vectb.cross(vecta) = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorC: operating vector ***
   *** with ndarray from numpy ***
### --- section_module: (GMVectorC) importing items from module --- ###
### --- section_class: (GMVectorC) describing class --- ###
### --- section_main: (GMVectorC) main process --- ###
vecta: (GMVectorC): xx = 3, yy = 4, rr = 5, th(deg) = 53.1301
vectb: (GMVectorC): xx = -4, yy = 3, rr = 5, th(deg) = 143.13
vecta.inner(vectb) = 0.0
vecta.outer(vectb) = array([[-12.,   9.],
       [-16.,  12.]])
vecta.cross(vectb) = 25.0
vectb.inner(vecta) = 0.0
vectb.outer(vecta) = array([[-12., -16.],
       [  9.,  12.]])
vectb.cross(vecta) = -25.0
'''
