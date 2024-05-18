# gm_class_vector_a.py: coded by Kinya MIURA 230418
# ---------------------------------------------------------
print('*** class GMVectorA: operating vector ***')
print('   *** basic version ***')
# ---------------------------------------------------------
print('### --- section_module: (GMVectorA) importing items from module --- ###')
from numpy import(
    square as sq, sqrt as sr, arctan2 as atan2, rad2deg as r2d)

# =========================================================
print('### --- section_class: (GMVectorA) describing class --- ###')
class GMVectorA():
    ## --- section_ca: initializing class instance --- ##
    def __init__(self,
            xx: float = 1, yy: float = 1) -> None:
        self.__xx, self.__yy = None, None
        self.set_xxyy(xx=xx, yy=yy)
    ## --- section_cb: setting and getting functions --- ##
    ## setting function
    def set_xxyy(self,
            xx: float = None, yy: float = None) -> None:
        if xx is not None: self.__xx = xx
        if yy is not None: self.__yy = yy
    ## getting functions
    def xxyy(self) -> tuple:
        return self.__xx, self.__yy
    ## --- section_cc: string function for print() --- ##
    def __str__(self) -> str:
        return f'(GMVectorA): xx = {self.__xx:g}, yy = {self.__yy:g}'
    ## --- section_cd: functions for properties --- ##
    def leng(self) -> float:
        return sr(sq(self.__xx)+sq(self.__yy))
    def dirc(self, deg: bool = True) -> float:
        th = atan2(self.__yy, self.__xx)
        if deg: th = r2d(th)
        return th
    def unitvect(self) -> tuple:
        leng = self.leng()
        return self.__xx / leng, self.__yy / leng

# =========================================================
print('### --- section_main: (GMVectorA) main process --- ###')
### --- section_main: (GMVectorA) calculating vectors --- ###
## --- section_ma: vector properties --- ##
vect = GMVectorA(xx=4, yy=3)  # creating instance
print(vect, f'\n{vect.unitvect() = }')
## --- section_mb: vector properties --- ##
vect.set_xxyy(xx=5, yy=5)  # setting instance variables
print(vect, f'\n{vect.unitvect() = }')

# =========================================================
# terminal log / terminal log / terminal log /
'''
*** class GMVectorA: operating vector ***
   *** basic version ***
### --- section_module: (GMVectorA) importing items from module --- ###
### --- section_class: (GMVectorA) describing class --- ###
### --- section_main: (GMVectorA) main process --- ###
(GMVectorA): xx = 4, yy = 3 
vect.unitvect() = (0.8, 0.6)
(GMVectorA): xx = 5, yy = 5 
vect.unitvect() = (0.7071067811865475, 0.7071067811865475)
'''
