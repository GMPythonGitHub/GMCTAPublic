# gm_class_geom_b_point.py: coded by Kinya MIURA 230518
# ---------------------------------------------------------
print("*** (GMPoint) class for point ***")
print("   *** class GMVector is inherited ***")
# ---------------------------------------------------------
print("### --- section_module: (GMPoint) importing items from module --- ###")
from numpy import ndarray
import copy
from gm_class_geom_a_vector import GMVector

# =========================================================
print("### --- section_class: (GMPoint) describing class --- ###")
class GMPoint(GMVector):  # inheriting class GMVector
    ## --- section_ca: (GMPoint) initializing class instance --- ##
    def __init__(self,
            xxyy: tuple = (0., 0.), rrth: tuple = None, unit: float = 1.,
            cnv: bool = True, deg: bool = True ):
        super().__init__(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
    ## --- section_cb: (GMPoint) setting and getting functions --- ##
    ## setting functions
    def set_point(self,
            xxyy: tuple = None, rrth: tuple = None, unit: float = None,
            cnv: bool = True, deg: bool = True) -> None:
        self.set_vector(xxyy=xxyy, rrth=rrth, unit=unit, cnv=cnv, deg=deg)
    ## getting functions
    def copy(self) -> object:
        return copy.deepcopy(self)
    ## --- section_cc: (GMPoint) string function for print() --- ##
    def __str__(self) -> str:
        return '(GMVector) ' + super().__str__()
    def classprop(self, idx: str = '') -> str:
        return idx + ':: GMPoint ::\n  ' + self.__str__()
    ## --- section_cd: (GMPoint) functions for analyzing points --- ##
    def vect_p2pint(self, pint: object) -> GMVector:
        return pint - self
    def dist_p2pint(self, pint: object, cnv: bool = False) -> float:
        vct = self.vect_p2pint(pint)
        return vct.leng(cnv)
    def dirc_p2pint(self, pint: object, deg: bool = False) -> float:
        vct = self.vect_p2pint(pint)
        return vct.dirc(deg)
    def unitvect_p2pint(self, pint: object) -> ndarray:
        vct = self.vect_p2pint(pint)
        return vct.unitvect()
    ## --- section_ce: (GMVector) functions for analyzing vectors --- ##
    def inner_op_vect(self, vect: object, cnv: bool = False) -> ndarray:  # inner product
        return self.inner_vect(vect, cnv=cnv)
    def outer_op_vect(self, vect: object, cnv: bool = False) -> ndarray:  # outer product
        return self.outer_vect(vect, cnv=cnv)
    def cross_op_vect(self, vect: object, cnv: bool = False) -> ndarray:  # cross product
        return self.cross_vect(vect, cnv=cnv)

# =========================================================
if __name__ == '__main__':
    print("### --- section_main: (GMPoint) main process --- ###")
    ## --- section_ma: (GMPoint) creating class instances --- ##
    pinta = GMPoint(xxyy=(1., 2.), unit=1.); print(pinta.classprop('pinta -> '))
    pintb = GMPoint(xxyy=(2., 1.), unit=1.); print(pintb.classprop('pintb -> '))
    print()
    ## --- section_mb: (GMPoint) calculating vector properties --- ##
    print(f'{pinta.unitvect() = }')  # GMVector
    print(pinta.vect_p2pint(pintb).classprop('inta.vect_p2pint(pintb) -> '))
    print(f'{pinta.dist_p2pint(pintb) = }')
    print(f'{pinta.dirc_p2pint(pintb, deg=True) = }')
    print(f'{pinta.unitvect_p2pint(pintb) = }')

    # =========================================================
    # terminal log / terminal log / terminal log /
    '''
    *** (GMPoint) class for point ***
       *** class GMVector is inherited ***
    ### --- section_module: (GMPoint) importing items from module --- ###
    *** (GMVector) class for vector ***
    ### --- section_module: (GMVector) importing items from module --- ###
    ### --- section_function: (GMVector) defining global functions --- ###
    ### --- section_class: (GMVector) describing class --- ###
    ### --- section_class: (GMPoint) describing class --- ###
    ### --- section_main: (GMPoint) main process --- ###

    pinta -> :: GMPoint ::
      (GMVector) xxyy = [1. 2.] : rrth = [ 2.23606798 63.43494882] : unit = 1
    pintb -> :: GMPoint ::
      (GMVector) xxyy = [2. 1.] : rrth = [ 2.23606798 26.56505118] : unit = 1
    pinta.unitvect() = array([0.4472136 , 0.89442719])

    inta.vect2p(pintb) -> :: GMVector ::
      xxyy = [ 1. -1.] : rrth = [  1.41421356 -45.        ] : unit = 1
    pinta.dist2p(pintb) = 1.4142135623730951
    pinta.dirc2p(pintb, deg=True) = -45.0
    pinta.unitvect2p(pintb) = array([ 0.70710678, -0.70710678])
    '''
