# gm_class_geom_c_point_vector.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMPointVector) class for position vector ***")
print("   *** class GMPoint is inherited; class GMVector is embedded as vect ***")
# ---------------------------------------------------------
print("### --- section_module: (GMPointVector) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_b_point import (GMPoint, GMVector)

# =========================================================
print("### --- section_class: (GMPointVector) describing class --- ###")
class GMPointVector(GMPoint):  # inheriting GMPoint
    ## --- section_ca: (GMPointVector) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (1., 1.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True,
            vect: GMVector = GMVector(xxyy=(1,0)) ) -> None:
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
        self._vect = None  # vector with initial point: GMVector
        self.set_point_vector(vect=vect)
    ## --- section_cb: (GMPointVector) setting and getting functions --- ##
    ## setting functions
    def set_point_vector(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True,
            vect: GMVector = None) -> None:
        self.set_point(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
        if vect is not None: self._vect = vect
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: (GMPointVector) string function for print() --- ##
    def __str__(self) -> str:
        return '(GMPoint) ' + super().__str__()
    def classprop(self, idx: str = '') -> str:
        return (
            idx + ':: GMPointVector ::\n'
            + self.__str__() + '\n'
            + '  vect: GMVector: ' + self._vect.__str__() + '' )
    ## --- section_cd: (GMPointVector) analysing vectors --- ##
    def vect_ot(self) -> GMVector:
        return  self + self._vect
    def inner_op_pt(self, cnv: bool = True) -> float:
        return self.inner_op_vect(self._vect, cnv)
    def outer_op_pt(self, cnv: bool = True) -> ndarray:
        return self.outer_op_vect(self._vect, cnv)
    def cross_op_pt(self, cnv: bool = True) -> float:
        return self.cross_op_vect(self._vect, cnv)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMPointVector) main process --- ###")
    print()
    ## --- section_ma: (GMPointVector) creating class instances --- ##
    pintvecta = GMPointVector(xxyy=(1., 2.), unit=1.)
    pintvecta._vect.set_vector(xxyy=(2., -1.), unit=1.)
    print(pintvecta.classprop('pintvecta -> '))
    print()
    ## --- section_mb: (GMPointVector) calculating vector properties --- ##
    print(pintvecta.vect_ot().classprop('pintvecta.vect_2t() -> '))
    print(f'{pintvecta.inner_op_pt() = }')
    print(f'{pintvecta.outer_op_pt() = }')
    print(f'{pintvecta.cross_op_pt() = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPointVector) class for position vector ***
       *** class GMPoint is inherited; class GMVector is embedded as vect ***
    ### --- section_module: (GMPointVector) importing items from module --- ###
    *** (GMPoint) class for point ***
       *** class GMVector is inherited ***
    ### --- section_module: (GMPoint) importing items from module --- ###
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_class: (GMVector) declaring class --- ###
    ### --- section_a: (GMPoint) declaring class --- ###
    ### --- section_class: (GMPointVector) declaring class --- ###
    ### --- section_main: (GMPointVector) main process --- ###
    
    pintvecta -> :: GMPointVector ::
    (GMPoint) (GMVector) xxyy = [1. 2.] : rrth = [ 2.23606798 63.43494882] : unit = 1
      vect: GMVector: xxyy = [ 2. -1.] : rrth = [  2.23606798 -26.56505118] : unit = 1

    pintvecta.vect2tip() = array([3., 1.])
    pintvecta.inner_pint2vect() = 0.0
    pintvecta.outer_pint2vect() = array([[ 2., -1.], [ 4., -2.]])
    pintvecta.cross_pint2vect() = array(-5.)
    '''
